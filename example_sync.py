from devolo_plc_api.device import Device


# IP of the device to query
IP = "192.168.0.10"

# Password, if the device has one. It is the same as the Web-UI has. It no password is set, you can remove the password
# parameter or set it to None.
PASSWORD = "super_secret"


def run():
    with Device(ip=IP, password=PASSWORD) as dpa:

        # Get LED settings of the device. The state might be LED_ON or LED_OFF.
        # {'state': 'LED_ON'}
        print(dpa.device.get_led_setting())

        # Set LED settings of the device. Set enable to True to them turn on, to False to turn them off.
        # If the state was changed successfully, True is returned, otherwise False.
        print("success" if dpa.device.set_led_setting(enable=True) else "failed")

        # Check for new firmware versions
        # {'result': 'UPDATE_NOT_AVAILABLE', 'new_firmware_version': ''}
        print(dpa.device.check_firmware_available())

        # Start firmware update, if new version is available. Important: The response does not tell you anything about the
        # success of the update itself.
        print("update started" if dpa.device.start_firmware_update() else "no update available")

        # Get details of wifi stations connected to the device: MAC address, wifi band and connection rates.
        # {'connected_stations':
        #   [
        #     {'mac_address': 'AA:BB:CC:DD:EE:FF',
        #      'vap_type': 'WIFI_VAP_MAIN_AP',
        #      'band': 'WIFI_BAND_5G',
        #      'rx_rate': 87800,
        #      'tx_rate': 87800}
        #   ]
        # }
        print(dpa.device.get_wifi_connected_station())

        # Get details about wifi guest access: SSID, Wifi key, state (enabled/disabled) and if time limited, the remaining
        # duration.
        # {'ssid': 'devolo-guest-930', 'key': 'HMANPGBA', 'enabled': False, 'remaining_duration': 0}
        print(dpa.device.get_wifi_guest_access())

        # Enable or disable the wifi guest access. Set enable to True to it turn on, to False to turn it off. Chaning SSID,
        # wifi key or duration is currently not supported. If the state was changed successfully, True is returned, otherwise
        # False.
        print("success" if dpa.device.set_wifi_guest_access(enable=False) else "failed")

        # Get details about other access points in your neighborhood: MAC address, SSID, wifi band, used channel, signal
        # strength in DB and a value from 1 to 5, if you would want to map the signal strenght to a signal bars.
        # {'neighbor_aps':
        #   [
        #     {'mac_address': 'AA:BB:CC:DD:EE:FF',
        #      'ssid': 'wifi',
        #      'band': 'WIFI_BAND_2G',
        #      'channel': 1,
        #      'signal': -73,
        #      'signal_bars': 1}
        #   ]
        # }
        print(dpa.device.get_wifi_neighbor_access_points())


        # Get PLC network overview with enriched information like firmware version,
        # {'network':
        #   {'devices':
        #       [
        #         {'product_name': 'devolo dLAN pro 1200+ WiFi ac',
        #          'product_id': 'MT2730',
        #          'friendly_version': '2.8.0.01',
        #          'full_version': 'MAC-QCA7500-2.8.0.30-01-20190705-CS',
        #          'user_device_name': '',
        #          'mac_address': 'AABBCCDDEEFF',
        #          'topology': 'LOCAL',
        #          'technology': 'HPAV_PANTHER',
        #          'bridged_devices': [],
        #          'user_network_name': '',
        #          'ipv4_address': '',
        #          'attached_to_router': False},
        #         {'product_name': 'devolo dLAN 1200+',
        #          'product_id': 'MT2639',
        #          'friendly_version': '2.8.0.01-1',
        #          'full_version': 'MAC-QCA7500-2.8.0.30-01-20190705-CS',
        #          'user_device_name': '',
        #          'mac_address': 'AABBCCDDEEFF',
        #          'topology': 'REMOTE',
        #          'technology': 'HPAV_PANTHER',
        #          'bridged_devices': [],
        #          'attached_to_router': True,
        #          'user_network_name': '',
        #          'ipv4_address': ''}
        #       ],
        #    'data_rates':
        #      [
        #        {'mac_address_from': 'AABBCCDDEEFF',
        #         'mac_address_to': 'AABBCCDDEEFF',
        #         'tx_rate': 129.9375,
        #         'rx_rate': 124.6875}
        #      ]
        #   }
        # }
        print(dpa.plcnet.get_network_overview())

        # Identify the device by making the PLC LED blink. This call returns directly with True, if identifing was started
        # succcessfully, otherwise False. However, the LED stays blinking for two minutes.
        print("success" if dpa.plcnet.identify_device_start() else "failed")

        # Stop identify the device if you don't want to wait for the timeout.
        print("success" if dpa.plcnet.identify_device_start() else "failed")

        # Set the user device name. If the name was changed successfully, True is returned, otherwise False.
        print("success" if dpa.plcnet.set_user_device_name(name="New name") else "failed")


if __name__ == "__main__":
    run()
