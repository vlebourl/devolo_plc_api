import logging
from typing import Union

from httpx import AsyncClient, Client

from ..clients.protobuf import Protobuf
from . import (devolo_idl_proto_plcnetapi_getnetworkoverview_pb2,
               devolo_idl_proto_plcnetapi_identifydevice_pb2,
               devolo_idl_proto_plcnetapi_setuserdevicename_pb2)


class PlcNetApi(Protobuf):
    """
    Implementation of the devolo plcnet API.

    :param ip: IP address of the device to communicate with
    :param port: Port to communicate with
    :param session: HTTP client session
    :param path: Path to send queries to
    :param version: Version of the API to use
    :param mac: Mac address of the to communicate with
    """

    def __init__(self,
                 ip: str,
                 port: int,
                 session: Union[AsyncClient, Client],
                 path: str,
                 version: str,
                 mac: str):
        self._ip = ip
        self._port = port
        self._session = session
        self._path = path
        self._version = version
        self._mac = mac
        self._user = ""  # PLC API is not password protected.
        self._password = ""  # PLC API is not password protected.
        self._logger = logging.getLogger(self.__class__.__name__)


    async def async_get_network_overview(self) -> dict:
        """
        Get a PLC network overview asynchronously.

        :return: Network overview
        """
        self._logger.debug("Getting network overview")
        network_overview = devolo_idl_proto_plcnetapi_getnetworkoverview_pb2.GetNetworkOverview()
        response = await self._async_get("GetNetworkOverview")
        network_overview.ParseFromString(await response.aread())
        return self._message_to_dict(network_overview)

    def get_network_overview(self) -> dict:
        """
        Get a PLC network overview synchronously.

        :return: Network overview
        """
        self._logger.debug("Getting network overview")
        network_overview = devolo_idl_proto_plcnetapi_getnetworkoverview_pb2.GetNetworkOverview()
        response = self._get("GetNetworkOverview")
        network_overview.ParseFromString(response.read())
        return self._message_to_dict(network_overview)

    async def async_identify_device_start(self):
        """
        Make PLC LED of a device blick to identify it asynchronously.

        :return: True, if identifying was successfully started, otherwise False
        """
        identify_device = devolo_idl_proto_plcnetapi_identifydevice_pb2.IdentifyDeviceStart()
        identify_device.mac_address = self._mac
        query = await self._async_post("IdentifyDeviceStart", content=identify_device.SerializeToString())
        response = devolo_idl_proto_plcnetapi_identifydevice_pb2.IdentifyDeviceResponse()
        response.FromString(await query.aread())  # pylint: disable=no-member
        return bool(not response.result)  # pylint: disable=no-member

    def identify_device_start(self):
        """
        Make PLC LED of a device blick to identify it synchronously.

        :return: True, if identifying was successfully started, otherwise False
        """
        identify_device = devolo_idl_proto_plcnetapi_identifydevice_pb2.IdentifyDeviceStart()
        identify_device.mac_address = self._mac
        query = self._post("IdentifyDeviceStart", content=identify_device.SerializeToString())
        response = devolo_idl_proto_plcnetapi_identifydevice_pb2.IdentifyDeviceResponse()
        response.FromString(query.read())  # pylint: disable=no-member
        return bool(not response.result)  # pylint: disable=no-member

    async def async_identify_device_stop(self):
        """
        Stop the PLC LED blicking asynchronously.

        :return: True, if identifying was successfully stopped, otherwise False
        """
        identify_device = devolo_idl_proto_plcnetapi_identifydevice_pb2.IdentifyDeviceStop()
        identify_device.mac_address = self._mac
        query = await self._async_post("IdentifyDeviceStop", content=identify_device.SerializeToString())
        response = devolo_idl_proto_plcnetapi_identifydevice_pb2.IdentifyDeviceResponse()
        response.FromString(await query.aread())  # pylint: disable=no-member
        return bool(not response.result)  # pylint: disable=no-member

    def identify_device_stop(self):
        """
        Stop the PLC LED blicking synchronously.

        :return: True, if identifying was successfully stopped, otherwise False
        """
        identify_device = devolo_idl_proto_plcnetapi_identifydevice_pb2.IdentifyDeviceStop()
        identify_device.mac_address = self._mac
        query = self._post("IdentifyDeviceStop", content=identify_device.SerializeToString())
        response = devolo_idl_proto_plcnetapi_identifydevice_pb2.IdentifyDeviceResponse()
        response.FromString(query.read())  # pylint: disable=no-member
        return bool(not response.result)  # pylint: disable=no-member

    async def async_set_user_device_name(self, name):
        """
        Set device name asynchronously.

        :param name: Name, the device shall have
        :return: True, if the device was successfully renamed, otherwise False
        """
        set_user_name = devolo_idl_proto_plcnetapi_setuserdevicename_pb2.SetUserDeviceName()
        set_user_name.mac_address = self._mac
        set_user_name.user_device_name = name
        query = await self._async_post("SetUserDeviceName", content=set_user_name.SerializeToString(), timeout=10.0)
        response = devolo_idl_proto_plcnetapi_setuserdevicename_pb2.SetUserDeviceNameResponse()
        response.FromString(await query.aread())  # pylint: disable=no-member
        return bool(not response.result)  # pylint: disable=no-member

    def set_user_device_name(self, name):
        """
        Set device name synchronously.

        :param name: Name, the device shall have
        :return: True, if the device was successfully renamed, otherwise False
        """
        set_user_name = devolo_idl_proto_plcnetapi_setuserdevicename_pb2.SetUserDeviceName()
        set_user_name.mac_address = self._mac
        set_user_name.user_device_name = name
        query = self._post("SetUserDeviceName", content=set_user_name.SerializeToString(), timeout=10.0)
        response = devolo_idl_proto_plcnetapi_setuserdevicename_pb2.SetUserDeviceNameResponse()
        response.FromString(query.read())  # pylint: disable=no-member
        return bool(not response.result)  # pylint: disable=no-member
