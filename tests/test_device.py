from datetime import date
from unittest.mock import patch

import pytest
from asynctest import CoroutineMock

from devolo_plc_api.device_api.deviceapi import DeviceApi
from devolo_plc_api.plcnet_api.plcnetapi import PlcNetApi

from .mocks.mock_service_browser import ServiceBrowser


class TestDevice:

    @pytest.mark.asyncio
    async def test__gather_apis(self, mocker, mock_device):
        with patch("devolo_plc_api.device.Device._get_device_info", new=CoroutineMock()), \
                patch("devolo_plc_api.device.Device._get_plcnet_info", new=CoroutineMock()):
            spy_device_info = mocker.spy(mock_device, "_get_device_info")
            spy_plcnet_info = mocker.spy(mock_device, "_get_plcnet_info")
            await mock_device._gather_apis()

            assert spy_device_info.call_count == 1
            assert spy_plcnet_info.call_count == 1

    @pytest.mark.asyncio
    @pytest.mark.usefixtures("mock_device_api")
    async def test__get_device_info(self, mock_device):
        with patch("devolo_plc_api.device.Device._get_zeroconf_info", new=CoroutineMock()):
            device_info = self.device_info['_dvl-deviceapi._tcp.local.']
            await mock_device._get_device_info()

            assert mock_device.firmware_date == date.fromisoformat(device_info['FirmwareDate'])
            assert mock_device.firmware_version == device_info['FirmwareVersion']
            assert mock_device.serial_number == device_info['SN']
            assert mock_device.mt_number == device_info['MT']
            assert mock_device.product == device_info['Product']
            assert type(mock_device.device) == DeviceApi

    @pytest.mark.asyncio
    @pytest.mark.usefixtures("mock_plcnet_api")
    async def test__get_plcnet_info(self, mock_device):
        with patch("devolo_plc_api.device.Device._get_zeroconf_info", new=CoroutineMock()):
            device_info = self.device_info['_dvl-plcnetapi._tcp.local.']
            await mock_device._get_plcnet_info()

            assert mock_device.mac == device_info['PlcMacAddress']
            assert mock_device.technology == device_info['PlcTechnology']
            assert type(mock_device.plcnet) == PlcNetApi

    @pytest.mark.asyncio
    @pytest.mark.usefixtures("mock_service_browser")
    async def test__get_zeroconf_info(self, mocker, mock_device):
        # TODO: test__get_zeroconf_info failes, because the mock is not applied correctly.
        browser = ServiceBrowser(None, None, None)
        spy_cancel = mocker.spy(browser, "cancel")
        await mock_device._get_zeroconf_info("_dvl-plcnetapi._tcp.local.")

        assert spy_cancel.call_count == 1
