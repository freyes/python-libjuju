# Copyright 2023 Canonical Ltd.
# Licensed under the Apache V2, see LICENCE file for details.
from __future__ import annotations

import logging
import sys
import warnings

if sys.version_info >= (3, 11):
    from enum import StrEnum
else:
    from backports.strenum import StrEnum

from .client import client

log = logging.getLogger(__name__)


class StatusStr(StrEnum):
    """Recognised status values.

    Please keep this set exact same as the severity map below.
    """

    error = "error"
    blocked = "blocked"
    waiting = "waiting"
    maintenance = "maintenance"
    active = "active"
    terminated = "terminated"
    unknown = "unknown"


""" severity_map holds status values with a severity measure.
Status values with higher severity are used in preference to others.
"""
severity_map: dict[StatusStr, int] = {
    # FIXME: Juju defines a lot more status values #1204
    StatusStr.error: 100,
    StatusStr.blocked: 90,
    StatusStr.waiting: 80,
    StatusStr.maintenance: 70,
    StatusStr.active: 60,
    StatusStr.terminated: 50,
    StatusStr.unknown: 40,
}


def derive_status(statuses: list[str | StatusStr]) -> StatusStr:
    """Derive status from a set.

    derive_status is used to determine the application status from a set of unit
    status values.

    :param statuses: list of known unit workload statuses
    """
    current: StatusStr = StatusStr.unknown
    for status in statuses:
        try:
            status = StatusStr(status)
        except ValueError:
            # Unknown Juju status, let's assume it's least important
            continue

        if severity_map[status] > severity_map[current]:
            current = status
    return current


async def formatted_status(model, target=None, raw=False, filters=None):
    """Returns a string that mimics the content of the information
    returned in the juju status command. If the raw parameter is
    enabled, the function returns a FullStatus object.
    :param Model model: model object to be used
    :param Fileobject target: if set expects a file object such as
        sys.stdout or a file descriptor. The obtained status will
        be sent to the file using the write function. If set to
        `None`, this function returns a string with the formatted
        status.
    :param bool raw: if `true` this functions returns the raw
        `FullStatus` object returned by Juju. This is similar to
        invoking `get_status`.
    :param str filters: Optional list of applications, units, or machines
        to include, which can use wildcards ('*').
    """
    warnings.warn(
        "juju.status.formatted_status is deprecated, the implementation is likely broken",
        DeprecationWarning,
        stacklevel=2,
    )
    client_facade = client.ClientFacade.from_connection(model.connection())
    result_status = await client_facade.FullStatus(patterns=filters)

    if raw:
        result_str = str(result_status)
    else:
        result_str = _print_status_model(result_status)
        result_str += "\n"
        result_str += _print_status_apps(result_status)
        result_str += "\n"
        result_str += _print_status_units(result_status)
        result_str += "\n"
        result_str += _print_status_machines(result_status)
        result_str += "\n"
    if target is None:
        return result_str

    try:
        target.write(result_str)
    except Exception as e:
        logging.error(e)

    return None


def _print_status_model(result_status):
    """Private function to print the status of a model"""
    m = result_status.model
    # print model
    result_str = "{:<25} {:<25} {:<15} {:<15} {:<30} {:<30}\n".format(
        "Model", "Cloud/Region", "Version", "SLA", "Timestamp", "Notes"
    )
    sla = m.unknown_fields["sla"]
    cloud = m.cloud_tag.split("-")[1]
    timestamp = result_status.controller_timestamp
    if m.available_version is not None and m.available_version != "":
        available_version = f"upgrade available: {m.available_version}"
    else:
        available_version = ""
    result_str += "{:<25} {:<25} {:<15} {:<15} {:<30} {:<30}".format(
        m.name, cloud + "/" + m.region, m.version, sla, timestamp, available_version
    )
    result_str += "\n"
    return result_str


def _print_status_apps(result_status):
    """Auxiliary function to print the apps received
    in a status result
    """
    apps = result_status.applications
    if apps is None or len(apps) == 0:
        return ""

    limits = "{:<25} {:<10} {:<10} {:<5} {:<20} {:<8}"
    # print header
    result_str = limits.format("App", "Version", "Status", "Scale", "Charm", "Channel")

    for name, app in apps.items():
        # extract charm name from the path
        # like in ch:amd64/trusty/mediawiki-28
        charm_name = app.charm.split("/")[-1]
        charm_name = charm_name.split("-")[0]
        work_ver = "NA" if app.workload_version is None else app.workload_version
        charm_channel = "NA" if app.charm_channel is None else app.charm_channel
        app_units = "NA" if app.units is None else len(app.units)
        app_status = "NA" if app.status.status is None else app.status.status
        result_str += "\n"
        result_str += limits.format(
            name, work_ver, app_status, app_units, charm_name, charm_channel
        )
    result_str += "\n"
    return result_str


def _print_status_units(result_status):
    """Auxiliary function to print the units received
    in a status result
    """
    apps = result_status.applications
    if apps is None or len(apps) == 0:
        return

    limits = "{:<15} {:<15} {:<20} {:<10} {:<15} {:<10} {:<30}"
    summary = ""
    for app in apps.values():
        units = app.units
        if units is None or len(units) == 0:
            continue

        for name, unit in units.items():
            addr = unit.public_address
            if addr is None:
                addr = ""

            if unit.opened_ports is None:
                opened_ports = ""
            else:
                opened_ports = ",".join(unit.opened_ports)

            info = unit.workload_status.info
            if info is None:
                info = ""

            step = limits.format(
                name,
                unit.workload_status.status,
                unit.agent_status.status,
                unit.machine,
                addr,
                opened_ports,
                info,
            )
            if summary == "":
                summary = step
            else:
                summary = summary + "\n" + step

    if len(summary) == 0:
        return ""
    result_str = limits.format(
        "Unit", "Workload", "Agent", "Machine", "Public address", "Ports", "Message"
    )
    result_str += "\n"
    result_str += summary
    result_str += "\n"
    return result_str


def _print_status_machines(result_status):
    machines = result_status.machines
    if machines is None or len(machines) == 0:
        return

    limits = "{:<15} {:<15} {:<15} {:<20} {:<15} {:<30}"
    summary = ""
    for name, machine in machines.items():
        dns = machine.dns_name
        if dns is None:
            dns = ""
        step = limits.format(
            name,
            machine.agent_status.status,
            dns,
            machine.instance_id,
            machine.series,
            machine.agent_status.info,
        )
        if summary == "":
            summary = step
        else:
            summary = summary + "\n" + step

    if summary == "":
        return
    result_str = limits.format(
        "Machine", "State", "DNS", "Inst id", "Series", "Message"
    )
    result_str += "\n"
    result_str += summary
    result_str += "\n"
    return result_str
