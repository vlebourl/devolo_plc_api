import logging
from google.protobuf.json_format import MessageToDict

from httpx import Client

from ..clients.protobuf import Protobuf
from . import devolo_idl_proto_plcnetapi_getnetworkoverview_pb2
from . import devolo_idl_proto_plcnetapi_identifydevice_pb2
from . import devolo_idl_proto_plcnetapi_setuserdevicename_pb2


class PlcNetApi(Protobuf):
    """
    Implementation of the devolo plcnet API.

    :param ip: IP address of the device to communicate with
    :param session: HTTP client session
    :param path: Path to send queries to
    :param version: Version of the API to use
    """

    def __init__(self, ip: str, session: Client, path: str, version: str, mac: str):
        self._ip = ip
        self._port = 47219
        self._session = session
        self._path = path
        self._version = version
        self._mac = mac
        self._user = None  # PLC APi is not password protected.
        self._password = None  # PLC APi is not password protected.
        self._logger = logging.getLogger(self.__class__.__name__)


    async def async_get_network_overview(self) -> dict:
        """ Get a PLC network overview asynchronously. """
        self._logger.debug("Getting network overview")
        network_overview = devolo_idl_proto_plcnetapi_getnetworkoverview_pb2.GetNetworkOverview()
        response = await self._async_get("GetNetworkOverview")
        network_overview.ParseFromString(await response.aread())
        return self._message_to_dict(network_overview)

    def get_network_overview(self) -> dict:
        """ Get a PLC network overview synchronously. """
        self._logger.debug("Getting network overview")
        network_overview = devolo_idl_proto_plcnetapi_getnetworkoverview_pb2.GetNetworkOverview()
        response = self._get("GetNetworkOverview")
        network_overview.ParseFromString(response.content)
        return self._message_to_dict(network_overview)

    async def identify_device_start(self):
        identify_device = devolo_idl_proto_plcnetapi_identifydevice_pb2.IdentifyDeviceStart()
        identify_device.mac_address = self._mac
        response = await self._async_post("IdentifyDeviceStart", data=identify_device.SerializeToString())
        r = devolo_idl_proto_plcnetapi_identifydevice_pb2.IdentifyDeviceResponse()
        # TODO: ParseFromString --> AttributeError
        # r.ParseFromstring(await response.aread())
        return MessageToDict(message=r, including_default_value_fields=True, preserving_proto_field_name=True)

    async def identify_device_stop(self):
        identify_device = devolo_idl_proto_plcnetapi_identifydevice_pb2.IdentifyDeviceStop()
        identify_device.mac_address = self._mac
        response = await self._async_post("IdentifyDeviceStop", data=identify_device.SerializeToString())
        # TODO: ParseFromString isn't working.
        identify_device.ParseFromString(await response.aread())
        r = devolo_idl_proto_plcnetapi_identifydevice_pb2.IdentifyDeviceResponse()
        # TODO: ParseFromString --> AttributeError
        # r.ParseFromstring(await response.aread())
        return MessageToDict(message=r, including_default_value_fields=True, preserving_proto_field_name=True)

    async def set_user_device_name(self, name):
        set_user_name = devolo_idl_proto_plcnetapi_setuserdevicename_pb2.SetUserDeviceName()
        set_user_name.mac_address = self._mac
        set_user_name.user_device_name = name
        response = await self._async_post("SetUserDeviceName", data=set_user_name.SerializeToString(), timeout=10.0)
        r = devolo_idl_proto_plcnetapi_setuserdevicename_pb2.SetUserDeviceNameResponse()
        r.ParseFromString(await response.aread())
        return MessageToDict(message=r, including_default_value_fields=True, preserving_proto_field_name=True)
