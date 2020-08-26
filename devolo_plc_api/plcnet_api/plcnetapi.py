import logging

from httpx import Client

from ..clients.protobuf import Protobuf
from . import devolo_idl_proto_plcnetapi_getnetworkoverview_pb2


class PlcNetApi(Protobuf):
    """
    Implementation of the devolo plcnet API.

    :param ip: IP address of the device to communicate with
    :param session: HTTP client session
    :param path: Path to send queries to
    :param version: Version of the API to use
    """

    def __init__(self, ip: str, session: Client, path: str, version: str):
        self._ip = ip
        self._port = 47219
        self._session = session
        self._path = path
        self._version = version
        self._user = None  # PLC APi is not password protected.
        self._password = None  # PLC APi is not password protected.
        self._logger = logging.getLogger(self.__class__.__name__)


    async def async_get_network_overview(self) -> dict:
        """ Get a PLC network overview asynchronously. """
        self._logger.debug("Getting network overview")
        network_overview = devolo_idl_proto_plcnetapi_getnetworkoverview_pb2.GetNetworkOverview()
        response = await self.async_get("GetNetworkOverview")
        network_overview.ParseFromString(await response.aread())
        return network_overview

    def get_network_overview(self) -> dict:
        """ Get a PLC network overview synchronously. """
        self._logger.debug("Getting network overview")
        network_overview = devolo_idl_proto_plcnetapi_getnetworkoverview_pb2.GetNetworkOverview()
        response = self.get("GetNetworkOverview")
        network_overview.ParseFromString(response.content)
        return network_overview
