import pytest

from devolo_plc_api.device import Device

from ..mocks.mock_service_browser import ServiceBrowser
from ..mocks.mock_zeroconf import Zeroconf


@pytest.fixture()
def mock_device(request):
    device = Device(ip=request.cls.ip)
    device._info = request.cls.device_info
    device._session = None
    device._zeroconf = None
    return device


@pytest.fixture()
def mock_service_browser(mocker):
    mocker.patch("zeroconf.ServiceBrowser.__init__", ServiceBrowser.__init__)
    mocker.patch("zeroconf.ServiceBrowser.cancel", ServiceBrowser.cancel)


@pytest.fixture()
def mock_zeroconf(mocker):
    mocker.patch("zeroconf.Zeroconf.get_service_info", Zeroconf.get_service_info)
