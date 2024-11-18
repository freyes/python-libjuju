# DO NOT CHANGE THIS FILE! This file is auto-generated by facade.py.
# Changes will be overwritten/lost when the file is regenerated.

from juju.client._definitions import *
from juju.client.facade import ReturnMapping, Type


class ClientFacade(Type):
    name = "Client"
    version = 8
    schema = {
        "definitions": {
            "AllWatcherId": {
                "additionalProperties": False,
                "properties": {"watcher-id": {"type": "string"}},
                "required": ["watcher-id"],
                "type": "object",
            },
            "ApplicationOfferStatus": {
                "additionalProperties": False,
                "properties": {
                    "active-connected-count": {"type": "integer"},
                    "application-name": {"type": "string"},
                    "charm": {"type": "string"},
                    "endpoints": {
                        "patternProperties": {
                            ".*": {"$ref": "#/definitions/RemoteEndpoint"}
                        },
                        "type": "object",
                    },
                    "err": {"$ref": "#/definitions/Error"},
                    "offer-name": {"type": "string"},
                    "total-connected-count": {"type": "integer"},
                },
                "required": [
                    "offer-name",
                    "application-name",
                    "charm",
                    "endpoints",
                    "active-connected-count",
                    "total-connected-count",
                ],
                "type": "object",
            },
            "ApplicationStatus": {
                "additionalProperties": False,
                "properties": {
                    "base": {"$ref": "#/definitions/Base"},
                    "can-upgrade-to": {"type": "string"},
                    "charm": {"type": "string"},
                    "charm-channel": {"type": "string"},
                    "charm-profile": {"type": "string"},
                    "charm-version": {"type": "string"},
                    "endpoint-bindings": {
                        "patternProperties": {".*": {"type": "string"}},
                        "type": "object",
                    },
                    "err": {"$ref": "#/definitions/Error"},
                    "exposed": {"type": "boolean"},
                    "exposed-endpoints": {
                        "patternProperties": {
                            ".*": {"$ref": "#/definitions/ExposedEndpoint"}
                        },
                        "type": "object",
                    },
                    "int": {"type": "integer"},
                    "life": {"type": "string"},
                    "meter-statuses": {
                        "patternProperties": {
                            ".*": {"$ref": "#/definitions/MeterStatus"}
                        },
                        "type": "object",
                    },
                    "provider-id": {"type": "string"},
                    "public-address": {"type": "string"},
                    "relations": {
                        "patternProperties": {
                            ".*": {"items": {"type": "string"}, "type": "array"}
                        },
                        "type": "object",
                    },
                    "status": {"$ref": "#/definitions/DetailedStatus"},
                    "subordinate-to": {"items": {"type": "string"}, "type": "array"},
                    "units": {
                        "patternProperties": {
                            ".*": {"$ref": "#/definitions/UnitStatus"}
                        },
                        "type": "object",
                    },
                    "workload-version": {"type": "string"},
                },
                "required": [
                    "charm",
                    "charm-version",
                    "charm-profile",
                    "base",
                    "exposed",
                    "life",
                    "relations",
                    "can-upgrade-to",
                    "subordinate-to",
                    "units",
                    "meter-statuses",
                    "status",
                    "workload-version",
                    "endpoint-bindings",
                    "public-address",
                ],
                "type": "object",
            },
            "Base": {
                "additionalProperties": False,
                "properties": {
                    "channel": {"type": "string"},
                    "name": {"type": "string"},
                },
                "required": ["name", "channel"],
                "type": "object",
            },
            "BranchStatus": {
                "additionalProperties": False,
                "properties": {
                    "assigned-units": {
                        "patternProperties": {
                            ".*": {"items": {"type": "string"}, "type": "array"}
                        },
                        "type": "object",
                    },
                    "created": {"type": "integer"},
                    "created-by": {"type": "string"},
                },
                "required": ["assigned-units", "created", "created-by"],
                "type": "object",
            },
            "DetailedStatus": {
                "additionalProperties": False,
                "properties": {
                    "data": {
                        "patternProperties": {
                            ".*": {"additionalProperties": True, "type": "object"}
                        },
                        "type": "object",
                    },
                    "err": {"$ref": "#/definitions/Error"},
                    "info": {"type": "string"},
                    "kind": {"type": "string"},
                    "life": {"type": "string"},
                    "since": {"format": "date-time", "type": "string"},
                    "status": {"type": "string"},
                    "version": {"type": "string"},
                },
                "required": [
                    "status",
                    "info",
                    "data",
                    "since",
                    "kind",
                    "version",
                    "life",
                ],
                "type": "object",
            },
            "EndpointStatus": {
                "additionalProperties": False,
                "properties": {
                    "application": {"type": "string"},
                    "name": {"type": "string"},
                    "role": {"type": "string"},
                    "subordinate": {"type": "boolean"},
                },
                "required": ["application", "name", "role", "subordinate"],
                "type": "object",
            },
            "EntityStatus": {
                "additionalProperties": False,
                "properties": {
                    "data": {
                        "patternProperties": {
                            ".*": {"additionalProperties": True, "type": "object"}
                        },
                        "type": "object",
                    },
                    "info": {"type": "string"},
                    "since": {"format": "date-time", "type": "string"},
                    "status": {"type": "string"},
                },
                "required": ["status", "info", "since"],
                "type": "object",
            },
            "Error": {
                "additionalProperties": False,
                "properties": {
                    "code": {"type": "string"},
                    "info": {
                        "patternProperties": {
                            ".*": {"additionalProperties": True, "type": "object"}
                        },
                        "type": "object",
                    },
                    "message": {"type": "string"},
                },
                "required": ["message", "code"],
                "type": "object",
            },
            "ExposedEndpoint": {
                "additionalProperties": False,
                "properties": {
                    "expose-to-cidrs": {"items": {"type": "string"}, "type": "array"},
                    "expose-to-spaces": {"items": {"type": "string"}, "type": "array"},
                },
                "type": "object",
            },
            "FilesystemAttachmentDetails": {
                "additionalProperties": False,
                "properties": {
                    "FilesystemAttachmentInfo": {
                        "$ref": "#/definitions/FilesystemAttachmentInfo"
                    },
                    "life": {"type": "string"},
                    "mount-point": {"type": "string"},
                    "read-only": {"type": "boolean"},
                },
                "required": ["FilesystemAttachmentInfo"],
                "type": "object",
            },
            "FilesystemAttachmentInfo": {
                "additionalProperties": False,
                "properties": {
                    "mount-point": {"type": "string"},
                    "read-only": {"type": "boolean"},
                },
                "type": "object",
            },
            "FilesystemDetails": {
                "additionalProperties": False,
                "properties": {
                    "filesystem-tag": {"type": "string"},
                    "info": {"$ref": "#/definitions/FilesystemInfo"},
                    "life": {"type": "string"},
                    "machine-attachments": {
                        "patternProperties": {
                            ".*": {"$ref": "#/definitions/FilesystemAttachmentDetails"}
                        },
                        "type": "object",
                    },
                    "status": {"$ref": "#/definitions/EntityStatus"},
                    "storage": {"$ref": "#/definitions/StorageDetails"},
                    "unit-attachments": {
                        "patternProperties": {
                            ".*": {"$ref": "#/definitions/FilesystemAttachmentDetails"}
                        },
                        "type": "object",
                    },
                    "volume-tag": {"type": "string"},
                },
                "required": ["filesystem-tag", "info", "status"],
                "type": "object",
            },
            "FilesystemInfo": {
                "additionalProperties": False,
                "properties": {
                    "filesystem-id": {"type": "string"},
                    "pool": {"type": "string"},
                    "size": {"type": "integer"},
                },
                "required": ["filesystem-id", "pool", "size"],
                "type": "object",
            },
            "FullStatus": {
                "additionalProperties": False,
                "properties": {
                    "applications": {
                        "patternProperties": {
                            ".*": {"$ref": "#/definitions/ApplicationStatus"}
                        },
                        "type": "object",
                    },
                    "branches": {
                        "patternProperties": {
                            ".*": {"$ref": "#/definitions/BranchStatus"}
                        },
                        "type": "object",
                    },
                    "controller-timestamp": {"format": "date-time", "type": "string"},
                    "filesystems": {
                        "items": {"$ref": "#/definitions/FilesystemDetails"},
                        "type": "array",
                    },
                    "machines": {
                        "patternProperties": {
                            ".*": {"$ref": "#/definitions/MachineStatus"}
                        },
                        "type": "object",
                    },
                    "model": {"$ref": "#/definitions/ModelStatusInfo"},
                    "offers": {
                        "patternProperties": {
                            ".*": {"$ref": "#/definitions/ApplicationOfferStatus"}
                        },
                        "type": "object",
                    },
                    "relations": {
                        "items": {"$ref": "#/definitions/RelationStatus"},
                        "type": "array",
                    },
                    "remote-applications": {
                        "patternProperties": {
                            ".*": {"$ref": "#/definitions/RemoteApplicationStatus"}
                        },
                        "type": "object",
                    },
                    "storage": {
                        "items": {"$ref": "#/definitions/StorageDetails"},
                        "type": "array",
                    },
                    "volumes": {
                        "items": {"$ref": "#/definitions/VolumeDetails"},
                        "type": "array",
                    },
                },
                "required": [
                    "model",
                    "machines",
                    "applications",
                    "remote-applications",
                    "offers",
                    "relations",
                    "controller-timestamp",
                    "branches",
                ],
                "type": "object",
            },
            "History": {
                "additionalProperties": False,
                "properties": {
                    "error": {"$ref": "#/definitions/Error"},
                    "statuses": {
                        "items": {"$ref": "#/definitions/DetailedStatus"},
                        "type": "array",
                    },
                },
                "required": ["statuses"],
                "type": "object",
            },
            "LXDProfile": {
                "additionalProperties": False,
                "properties": {
                    "config": {
                        "patternProperties": {".*": {"type": "string"}},
                        "type": "object",
                    },
                    "description": {"type": "string"},
                    "devices": {
                        "patternProperties": {
                            ".*": {
                                "patternProperties": {".*": {"type": "string"}},
                                "type": "object",
                            }
                        },
                        "type": "object",
                    },
                },
                "required": ["config", "description", "devices"],
                "type": "object",
            },
            "MachineStatus": {
                "additionalProperties": False,
                "properties": {
                    "agent-status": {"$ref": "#/definitions/DetailedStatus"},
                    "base": {"$ref": "#/definitions/Base"},
                    "constraints": {"type": "string"},
                    "containers": {
                        "patternProperties": {
                            ".*": {"$ref": "#/definitions/MachineStatus"}
                        },
                        "type": "object",
                    },
                    "display-name": {"type": "string"},
                    "dns-name": {"type": "string"},
                    "hardware": {"type": "string"},
                    "has-vote": {"type": "boolean"},
                    "hostname": {"type": "string"},
                    "id": {"type": "string"},
                    "instance-id": {"type": "string"},
                    "instance-status": {"$ref": "#/definitions/DetailedStatus"},
                    "ip-addresses": {"items": {"type": "string"}, "type": "array"},
                    "jobs": {"items": {"type": "string"}, "type": "array"},
                    "lxd-profiles": {
                        "patternProperties": {
                            ".*": {"$ref": "#/definitions/LXDProfile"}
                        },
                        "type": "object",
                    },
                    "modification-status": {"$ref": "#/definitions/DetailedStatus"},
                    "network-interfaces": {
                        "patternProperties": {
                            ".*": {"$ref": "#/definitions/NetworkInterface"}
                        },
                        "type": "object",
                    },
                    "primary-controller-machine": {"type": "boolean"},
                    "wants-vote": {"type": "boolean"},
                },
                "required": [
                    "agent-status",
                    "instance-status",
                    "modification-status",
                    "dns-name",
                    "instance-id",
                    "display-name",
                    "base",
                    "id",
                    "containers",
                    "constraints",
                    "hardware",
                    "jobs",
                    "has-vote",
                    "wants-vote",
                ],
                "type": "object",
            },
            "MeterStatus": {
                "additionalProperties": False,
                "properties": {
                    "color": {"type": "string"},
                    "message": {"type": "string"},
                },
                "required": ["color", "message"],
                "type": "object",
            },
            "ModelStatusInfo": {
                "additionalProperties": False,
                "properties": {
                    "available-version": {"type": "string"},
                    "cloud-tag": {"type": "string"},
                    "meter-status": {"$ref": "#/definitions/MeterStatus"},
                    "model-status": {"$ref": "#/definitions/DetailedStatus"},
                    "name": {"type": "string"},
                    "region": {"type": "string"},
                    "sla": {"type": "string"},
                    "type": {"type": "string"},
                    "version": {"type": "string"},
                },
                "required": [
                    "name",
                    "type",
                    "cloud-tag",
                    "version",
                    "available-version",
                    "model-status",
                    "meter-status",
                    "sla",
                ],
                "type": "object",
            },
            "NetworkInterface": {
                "additionalProperties": False,
                "properties": {
                    "dns-nameservers": {"items": {"type": "string"}, "type": "array"},
                    "gateway": {"type": "string"},
                    "ip-addresses": {"items": {"type": "string"}, "type": "array"},
                    "is-up": {"type": "boolean"},
                    "mac-address": {"type": "string"},
                    "space": {"type": "string"},
                },
                "required": ["ip-addresses", "mac-address", "is-up"],
                "type": "object",
            },
            "RelationStatus": {
                "additionalProperties": False,
                "properties": {
                    "endpoints": {
                        "items": {"$ref": "#/definitions/EndpointStatus"},
                        "type": "array",
                    },
                    "id": {"type": "integer"},
                    "interface": {"type": "string"},
                    "key": {"type": "string"},
                    "scope": {"type": "string"},
                    "status": {"$ref": "#/definitions/DetailedStatus"},
                },
                "required": ["id", "key", "interface", "scope", "endpoints", "status"],
                "type": "object",
            },
            "RemoteApplicationStatus": {
                "additionalProperties": False,
                "properties": {
                    "endpoints": {
                        "items": {"$ref": "#/definitions/RemoteEndpoint"},
                        "type": "array",
                    },
                    "err": {"$ref": "#/definitions/Error"},
                    "life": {"type": "string"},
                    "offer-name": {"type": "string"},
                    "offer-url": {"type": "string"},
                    "relations": {
                        "patternProperties": {
                            ".*": {"items": {"type": "string"}, "type": "array"}
                        },
                        "type": "object",
                    },
                    "status": {"$ref": "#/definitions/DetailedStatus"},
                },
                "required": [
                    "offer-url",
                    "offer-name",
                    "endpoints",
                    "life",
                    "relations",
                    "status",
                ],
                "type": "object",
            },
            "RemoteEndpoint": {
                "additionalProperties": False,
                "properties": {
                    "interface": {"type": "string"},
                    "limit": {"type": "integer"},
                    "name": {"type": "string"},
                    "role": {"type": "string"},
                },
                "required": ["name", "role", "interface", "limit"],
                "type": "object",
            },
            "StatusHistoryFilter": {
                "additionalProperties": False,
                "properties": {
                    "date": {"format": "date-time", "type": "string"},
                    "delta": {"type": "integer"},
                    "exclude": {"items": {"type": "string"}, "type": "array"},
                    "size": {"type": "integer"},
                },
                "required": ["size", "date", "delta", "exclude"],
                "type": "object",
            },
            "StatusHistoryRequest": {
                "additionalProperties": False,
                "properties": {
                    "filter": {"$ref": "#/definitions/StatusHistoryFilter"},
                    "historyKind": {"type": "string"},
                    "size": {"type": "integer"},
                    "tag": {"type": "string"},
                },
                "required": ["historyKind", "size", "filter", "tag"],
                "type": "object",
            },
            "StatusHistoryRequests": {
                "additionalProperties": False,
                "properties": {
                    "requests": {
                        "items": {"$ref": "#/definitions/StatusHistoryRequest"},
                        "type": "array",
                    }
                },
                "required": ["requests"],
                "type": "object",
            },
            "StatusHistoryResult": {
                "additionalProperties": False,
                "properties": {
                    "error": {"$ref": "#/definitions/Error"},
                    "history": {"$ref": "#/definitions/History"},
                },
                "required": ["history"],
                "type": "object",
            },
            "StatusHistoryResults": {
                "additionalProperties": False,
                "properties": {
                    "results": {
                        "items": {"$ref": "#/definitions/StatusHistoryResult"},
                        "type": "array",
                    }
                },
                "required": ["results"],
                "type": "object",
            },
            "StatusParams": {
                "additionalProperties": False,
                "properties": {
                    "include-storage": {"type": "boolean"},
                    "patterns": {"items": {"type": "string"}, "type": "array"},
                },
                "required": ["patterns"],
                "type": "object",
            },
            "StorageAttachmentDetails": {
                "additionalProperties": False,
                "properties": {
                    "life": {"type": "string"},
                    "location": {"type": "string"},
                    "machine-tag": {"type": "string"},
                    "storage-tag": {"type": "string"},
                    "unit-tag": {"type": "string"},
                },
                "required": ["storage-tag", "unit-tag", "machine-tag"],
                "type": "object",
            },
            "StorageDetails": {
                "additionalProperties": False,
                "properties": {
                    "attachments": {
                        "patternProperties": {
                            ".*": {"$ref": "#/definitions/StorageAttachmentDetails"}
                        },
                        "type": "object",
                    },
                    "kind": {"type": "integer"},
                    "life": {"type": "string"},
                    "owner-tag": {"type": "string"},
                    "persistent": {"type": "boolean"},
                    "status": {"$ref": "#/definitions/EntityStatus"},
                    "storage-tag": {"type": "string"},
                },
                "required": [
                    "storage-tag",
                    "owner-tag",
                    "kind",
                    "status",
                    "persistent",
                ],
                "type": "object",
            },
            "UnitStatus": {
                "additionalProperties": False,
                "properties": {
                    "address": {"type": "string"},
                    "agent-status": {"$ref": "#/definitions/DetailedStatus"},
                    "charm": {"type": "string"},
                    "leader": {"type": "boolean"},
                    "machine": {"type": "string"},
                    "opened-ports": {"items": {"type": "string"}, "type": "array"},
                    "provider-id": {"type": "string"},
                    "public-address": {"type": "string"},
                    "subordinates": {
                        "patternProperties": {
                            ".*": {"$ref": "#/definitions/UnitStatus"}
                        },
                        "type": "object",
                    },
                    "workload-status": {"$ref": "#/definitions/DetailedStatus"},
                    "workload-version": {"type": "string"},
                },
                "required": [
                    "agent-status",
                    "workload-status",
                    "workload-version",
                    "machine",
                    "opened-ports",
                    "public-address",
                    "charm",
                    "subordinates",
                ],
                "type": "object",
            },
            "VolumeAttachmentDetails": {
                "additionalProperties": False,
                "properties": {
                    "VolumeAttachmentInfo": {
                        "$ref": "#/definitions/VolumeAttachmentInfo"
                    },
                    "bus-address": {"type": "string"},
                    "device-link": {"type": "string"},
                    "device-name": {"type": "string"},
                    "life": {"type": "string"},
                    "plan-info": {"$ref": "#/definitions/VolumeAttachmentPlanInfo"},
                    "read-only": {"type": "boolean"},
                },
                "required": ["VolumeAttachmentInfo"],
                "type": "object",
            },
            "VolumeAttachmentInfo": {
                "additionalProperties": False,
                "properties": {
                    "bus-address": {"type": "string"},
                    "device-link": {"type": "string"},
                    "device-name": {"type": "string"},
                    "plan-info": {"$ref": "#/definitions/VolumeAttachmentPlanInfo"},
                    "read-only": {"type": "boolean"},
                },
                "type": "object",
            },
            "VolumeAttachmentPlanInfo": {
                "additionalProperties": False,
                "properties": {
                    "device-attributes": {
                        "patternProperties": {".*": {"type": "string"}},
                        "type": "object",
                    },
                    "device-type": {"type": "string"},
                },
                "type": "object",
            },
            "VolumeDetails": {
                "additionalProperties": False,
                "properties": {
                    "info": {"$ref": "#/definitions/VolumeInfo"},
                    "life": {"type": "string"},
                    "machine-attachments": {
                        "patternProperties": {
                            ".*": {"$ref": "#/definitions/VolumeAttachmentDetails"}
                        },
                        "type": "object",
                    },
                    "status": {"$ref": "#/definitions/EntityStatus"},
                    "storage": {"$ref": "#/definitions/StorageDetails"},
                    "unit-attachments": {
                        "patternProperties": {
                            ".*": {"$ref": "#/definitions/VolumeAttachmentDetails"}
                        },
                        "type": "object",
                    },
                    "volume-tag": {"type": "string"},
                },
                "required": ["volume-tag", "info", "status"],
                "type": "object",
            },
            "VolumeInfo": {
                "additionalProperties": False,
                "properties": {
                    "hardware-id": {"type": "string"},
                    "persistent": {"type": "boolean"},
                    "pool": {"type": "string"},
                    "size": {"type": "integer"},
                    "volume-id": {"type": "string"},
                    "wwn": {"type": "string"},
                },
                "required": ["volume-id", "size", "persistent"],
                "type": "object",
            },
        },
        "properties": {
            "FullStatus": {
                "description": "FullStatus gives the "
                "information needed for juju "
                "status over the api",
                "properties": {
                    "Params": {"$ref": "#/definitions/StatusParams"},
                    "Result": {"$ref": "#/definitions/FullStatus"},
                },
                "type": "object",
            },
            "StatusHistory": {
                "description": "StatusHistory returns a "
                "slice of past statuses for "
                "several entities.",
                "properties": {
                    "Params": {"$ref": "#/definitions/StatusHistoryRequests"},
                    "Result": {"$ref": "#/definitions/StatusHistoryResults"},
                },
                "type": "object",
            },
            "WatchAll": {
                "description": "WatchAll initiates a watcher for "
                "entities in the connected model.",
                "properties": {"Result": {"$ref": "#/definitions/AllWatcherId"}},
                "type": "object",
            },
        },
        "type": "object",
    }

    @ReturnMapping(FullStatus)
    async def FullStatus(self, include_storage=None, patterns=None):
        """FullStatus gives the information needed for juju status over the api

        include_storage : bool
        patterns : typing.Sequence[str]
        Returns -> FullStatus
        """
        if include_storage is not None and not isinstance(include_storage, bool):
            raise Exception(
                f"Expected include_storage to be a bool, received: {type(include_storage)}"
            )

        if patterns is not None and not isinstance(patterns, (bytes, str, list)):
            raise Exception(
                f"Expected patterns to be a Sequence, received: {type(patterns)}"
            )

        # map input types to rpc msg
        _params = dict()
        msg = dict(type="Client", request="FullStatus", version=8, params=_params)
        _params["include-storage"] = include_storage
        _params["patterns"] = patterns
        reply = await self.rpc(msg)
        return reply

    @ReturnMapping(StatusHistoryResults)
    async def StatusHistory(self, requests=None):
        """StatusHistory returns a slice of past statuses for several entities.

        requests : typing.Sequence[~StatusHistoryRequest]
        Returns -> StatusHistoryResults
        """
        if requests is not None and not isinstance(requests, (bytes, str, list)):
            raise Exception(
                f"Expected requests to be a Sequence, received: {type(requests)}"
            )

        # map input types to rpc msg
        _params = dict()
        msg = dict(type="Client", request="StatusHistory", version=8, params=_params)
        _params["requests"] = requests
        reply = await self.rpc(msg)
        return reply

    @ReturnMapping(AllWatcherId)
    async def WatchAll(self):
        """WatchAll initiates a watcher for entities in the connected model.

        Returns -> AllWatcherId
        """
        # map input types to rpc msg
        _params = dict()
        msg = dict(type="Client", request="WatchAll", version=8, params=_params)

        reply = await self.rpc(msg)
        return reply
