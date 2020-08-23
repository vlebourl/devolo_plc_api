# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: devolo_idl_proto_deviceapi_wifinetwork.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='devolo_idl_proto_deviceapi_wifinetwork.proto',
  package='device.api',
  syntax='proto3',
  serialized_pb=_b('\n,devolo_idl_proto_deviceapi_wifinetwork.proto\x12\ndevice.api\".\n\x11WifiParametersSet\x12\x0c\n\x04ssid\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\"C\n\x19WifiParametersSetResponse\x12&\n\x06result\x18\x01 \x01(\x0e\x32\x16.device.api.WifiResult\"6\n\x12WifiGuestAccessSet\x12\x0e\n\x06\x65nable\x18\x01 \x01(\x08\x12\x10\n\x08\x64uration\x18\x02 \x01(\r\"D\n\x1aWifiGuestAccessSetResponse\x12&\n\x06result\x18\x01 \x01(\x0e\x32\x16.device.api.WifiResult\"\\\n\x12WifiGuestAccessGet\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x1a\n\x12remaining_duration\x18\x02 \x01(\r\x12\x0c\n\x04ssid\x18\x03 \x01(\t\x12\x0b\n\x03key\x18\x04 \x01(\t\"\xe9\x01\n\x12WifiNeighborAPsGet\x12\x43\n\x0cneighbor_aps\x18\x01 \x03(\x0b\x32-.device.api.WifiNeighborAPsGet.NeighborAPInfo\x1a\x8d\x01\n\x0eNeighborAPInfo\x12\x13\n\x0bmac_address\x18\x01 \x01(\t\x12\x0c\n\x04ssid\x18\x02 \x01(\t\x12\"\n\x04\x62\x61nd\x18\x03 \x01(\x0e\x32\x14.device.api.WifiBand\x12\x0f\n\x07\x63hannel\x18\x04 \x01(\r\x12\x0e\n\x06signal\x18\x05 \x01(\x05\x12\x13\n\x0bsignal_bars\x18\x06 \x01(\x05\"\xf7\x01\n\x12WifiRepeatedAPsGet\x12\x43\n\x0crepeated_aps\x18\x01 \x03(\x0b\x32-.device.api.WifiRepeatedAPsGet.RepeatedAPInfo\x1a\x9b\x01\n\x0eRepeatedAPInfo\x12\x13\n\x0bmac_address\x18\x01 \x01(\t\x12\x0c\n\x04ssid\x18\x02 \x01(\t\x12\"\n\x04\x62\x61nd\x18\x03 \x01(\x0e\x32\x14.device.api.WifiBand\x12\x0f\n\x07\x63hannel\x18\x04 \x01(\r\x12\x0c\n\x04rate\x18\x05 \x01(\r\x12\x0e\n\x06signal\x18\x06 \x01(\x05\x12\x13\n\x0bsignal_bars\x18\x07 \x01(\x05\"\x90\x02\n\x18WifiConnectedStationsGet\x12U\n\x12\x63onnected_stations\x18\x01 \x03(\x0b\x32\x39.device.api.WifiConnectedStationsGet.ConnectedStationInfo\x1a\x9c\x01\n\x14\x43onnectedStationInfo\x12\x13\n\x0bmac_address\x18\x01 \x01(\t\x12)\n\x08vap_type\x18\x02 \x01(\x0e\x32\x17.device.api.WifiVAPType\x12\"\n\x04\x62\x61nd\x18\x03 \x01(\x0e\x32\x14.device.api.WifiBand\x12\x0f\n\x07rx_rate\x18\x04 \x01(\r\x12\x0f\n\x07tx_rate\x18\x05 \x01(\r\"u\n\x19WifiRepeaterParametersSet\x12\x0c\n\x04ssid\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x11\n\tcrossband\x18\x03 \x01(\x08\x12*\n\x0cprimary_band\x18\x04 \x01(\x0e\x32\x14.device.api.WifiBand\"K\n!WifiRepeaterParametersSetResponse\x12&\n\x06result\x18\x01 \x01(\x0e\x32\x16.device.api.WifiResult\"9\n\x0fWifiWpsPbcStart\x12&\n\x06result\x18\x01 \x01(\x0e\x32\x16.device.api.WifiResult\"F\n\x1cWifiRepeaterWpsClonePbcStart\x12&\n\x06result\x18\x01 \x01(\x0e\x32\x16.device.api.WifiResult*z\n\nWifiResult\x12\x10\n\x0cWIFI_SUCCESS\x10\x00\x12\x15\n\x11WIFI_INVALID_SSID\x10\x01\x12\x14\n\x10WIFI_INVALID_KEY\x10\x02\x12\x14\n\x10WIFI_IS_DISABLED\x10\x03\x12\x17\n\x12WIFI_UNKNOWN_ERROR\x10\xff\x01*E\n\x08WifiBand\x12\x15\n\x11WIFI_BAND_UNKNOWN\x10\x00\x12\x10\n\x0cWIFI_BAND_2G\x10\x01\x12\x10\n\x0cWIFI_BAND_5G\x10\x02*f\n\x0bWifiVAPType\x12\x14\n\x10WIFI_VAP_UNKNOWN\x10\x00\x12\x14\n\x10WIFI_VAP_MAIN_AP\x10\x01\x12\x15\n\x11WIFI_VAP_GUEST_AP\x10\x02\x12\x14\n\x10WIFI_VAP_STATION\x10\x03\x42\x15\n\x06\x64\x65viceB\x0bwifinetworkb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_WIFIRESULT = _descriptor.EnumDescriptor(
  name='WifiResult',
  full_name='device.api.WifiResult',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WIFI_SUCCESS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WIFI_INVALID_SSID', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WIFI_INVALID_KEY', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WIFI_IS_DISABLED', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WIFI_UNKNOWN_ERROR', index=4, number=255,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1485,
  serialized_end=1607,
)
_sym_db.RegisterEnumDescriptor(_WIFIRESULT)

WifiResult = enum_type_wrapper.EnumTypeWrapper(_WIFIRESULT)
_WIFIBAND = _descriptor.EnumDescriptor(
  name='WifiBand',
  full_name='device.api.WifiBand',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WIFI_BAND_UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WIFI_BAND_2G', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WIFI_BAND_5G', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1609,
  serialized_end=1678,
)
_sym_db.RegisterEnumDescriptor(_WIFIBAND)

WifiBand = enum_type_wrapper.EnumTypeWrapper(_WIFIBAND)
_WIFIVAPTYPE = _descriptor.EnumDescriptor(
  name='WifiVAPType',
  full_name='device.api.WifiVAPType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WIFI_VAP_UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WIFI_VAP_MAIN_AP', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WIFI_VAP_GUEST_AP', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WIFI_VAP_STATION', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1680,
  serialized_end=1782,
)
_sym_db.RegisterEnumDescriptor(_WIFIVAPTYPE)

WifiVAPType = enum_type_wrapper.EnumTypeWrapper(_WIFIVAPTYPE)
WIFI_SUCCESS = 0
WIFI_INVALID_SSID = 1
WIFI_INVALID_KEY = 2
WIFI_IS_DISABLED = 3
WIFI_UNKNOWN_ERROR = 255
WIFI_BAND_UNKNOWN = 0
WIFI_BAND_2G = 1
WIFI_BAND_5G = 2
WIFI_VAP_UNKNOWN = 0
WIFI_VAP_MAIN_AP = 1
WIFI_VAP_GUEST_AP = 2
WIFI_VAP_STATION = 3



_WIFIPARAMETERSSET = _descriptor.Descriptor(
  name='WifiParametersSet',
  full_name='device.api.WifiParametersSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ssid', full_name='device.api.WifiParametersSet.ssid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key', full_name='device.api.WifiParametersSet.key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=106,
)


_WIFIPARAMETERSSETRESPONSE = _descriptor.Descriptor(
  name='WifiParametersSetResponse',
  full_name='device.api.WifiParametersSetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='device.api.WifiParametersSetResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=108,
  serialized_end=175,
)


_WIFIGUESTACCESSSET = _descriptor.Descriptor(
  name='WifiGuestAccessSet',
  full_name='device.api.WifiGuestAccessSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enable', full_name='device.api.WifiGuestAccessSet.enable', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='duration', full_name='device.api.WifiGuestAccessSet.duration', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=177,
  serialized_end=231,
)


_WIFIGUESTACCESSSETRESPONSE = _descriptor.Descriptor(
  name='WifiGuestAccessSetResponse',
  full_name='device.api.WifiGuestAccessSetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='device.api.WifiGuestAccessSetResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=233,
  serialized_end=301,
)


_WIFIGUESTACCESSGET = _descriptor.Descriptor(
  name='WifiGuestAccessGet',
  full_name='device.api.WifiGuestAccessGet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enabled', full_name='device.api.WifiGuestAccessGet.enabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remaining_duration', full_name='device.api.WifiGuestAccessGet.remaining_duration', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ssid', full_name='device.api.WifiGuestAccessGet.ssid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key', full_name='device.api.WifiGuestAccessGet.key', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=303,
  serialized_end=395,
)


_WIFINEIGHBORAPSGET_NEIGHBORAPINFO = _descriptor.Descriptor(
  name='NeighborAPInfo',
  full_name='device.api.WifiNeighborAPsGet.NeighborAPInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mac_address', full_name='device.api.WifiNeighborAPsGet.NeighborAPInfo.mac_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ssid', full_name='device.api.WifiNeighborAPsGet.NeighborAPInfo.ssid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='band', full_name='device.api.WifiNeighborAPsGet.NeighborAPInfo.band', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channel', full_name='device.api.WifiNeighborAPsGet.NeighborAPInfo.channel', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signal', full_name='device.api.WifiNeighborAPsGet.NeighborAPInfo.signal', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signal_bars', full_name='device.api.WifiNeighborAPsGet.NeighborAPInfo.signal_bars', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=490,
  serialized_end=631,
)

_WIFINEIGHBORAPSGET = _descriptor.Descriptor(
  name='WifiNeighborAPsGet',
  full_name='device.api.WifiNeighborAPsGet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='neighbor_aps', full_name='device.api.WifiNeighborAPsGet.neighbor_aps', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_WIFINEIGHBORAPSGET_NEIGHBORAPINFO, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=398,
  serialized_end=631,
)


_WIFIREPEATEDAPSGET_REPEATEDAPINFO = _descriptor.Descriptor(
  name='RepeatedAPInfo',
  full_name='device.api.WifiRepeatedAPsGet.RepeatedAPInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mac_address', full_name='device.api.WifiRepeatedAPsGet.RepeatedAPInfo.mac_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ssid', full_name='device.api.WifiRepeatedAPsGet.RepeatedAPInfo.ssid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='band', full_name='device.api.WifiRepeatedAPsGet.RepeatedAPInfo.band', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channel', full_name='device.api.WifiRepeatedAPsGet.RepeatedAPInfo.channel', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rate', full_name='device.api.WifiRepeatedAPsGet.RepeatedAPInfo.rate', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signal', full_name='device.api.WifiRepeatedAPsGet.RepeatedAPInfo.signal', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signal_bars', full_name='device.api.WifiRepeatedAPsGet.RepeatedAPInfo.signal_bars', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=726,
  serialized_end=881,
)

_WIFIREPEATEDAPSGET = _descriptor.Descriptor(
  name='WifiRepeatedAPsGet',
  full_name='device.api.WifiRepeatedAPsGet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='repeated_aps', full_name='device.api.WifiRepeatedAPsGet.repeated_aps', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_WIFIREPEATEDAPSGET_REPEATEDAPINFO, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=634,
  serialized_end=881,
)


_WIFICONNECTEDSTATIONSGET_CONNECTEDSTATIONINFO = _descriptor.Descriptor(
  name='ConnectedStationInfo',
  full_name='device.api.WifiConnectedStationsGet.ConnectedStationInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mac_address', full_name='device.api.WifiConnectedStationsGet.ConnectedStationInfo.mac_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vap_type', full_name='device.api.WifiConnectedStationsGet.ConnectedStationInfo.vap_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='band', full_name='device.api.WifiConnectedStationsGet.ConnectedStationInfo.band', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rx_rate', full_name='device.api.WifiConnectedStationsGet.ConnectedStationInfo.rx_rate', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tx_rate', full_name='device.api.WifiConnectedStationsGet.ConnectedStationInfo.tx_rate', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1000,
  serialized_end=1156,
)

_WIFICONNECTEDSTATIONSGET = _descriptor.Descriptor(
  name='WifiConnectedStationsGet',
  full_name='device.api.WifiConnectedStationsGet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='connected_stations', full_name='device.api.WifiConnectedStationsGet.connected_stations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_WIFICONNECTEDSTATIONSGET_CONNECTEDSTATIONINFO, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=884,
  serialized_end=1156,
)


_WIFIREPEATERPARAMETERSSET = _descriptor.Descriptor(
  name='WifiRepeaterParametersSet',
  full_name='device.api.WifiRepeaterParametersSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ssid', full_name='device.api.WifiRepeaterParametersSet.ssid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key', full_name='device.api.WifiRepeaterParametersSet.key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='crossband', full_name='device.api.WifiRepeaterParametersSet.crossband', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='primary_band', full_name='device.api.WifiRepeaterParametersSet.primary_band', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1158,
  serialized_end=1275,
)


_WIFIREPEATERPARAMETERSSETRESPONSE = _descriptor.Descriptor(
  name='WifiRepeaterParametersSetResponse',
  full_name='device.api.WifiRepeaterParametersSetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='device.api.WifiRepeaterParametersSetResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1277,
  serialized_end=1352,
)


_WIFIWPSPBCSTART = _descriptor.Descriptor(
  name='WifiWpsPbcStart',
  full_name='device.api.WifiWpsPbcStart',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='device.api.WifiWpsPbcStart.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1354,
  serialized_end=1411,
)


_WIFIREPEATERWPSCLONEPBCSTART = _descriptor.Descriptor(
  name='WifiRepeaterWpsClonePbcStart',
  full_name='device.api.WifiRepeaterWpsClonePbcStart',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='device.api.WifiRepeaterWpsClonePbcStart.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1413,
  serialized_end=1483,
)

_WIFIPARAMETERSSETRESPONSE.fields_by_name['result'].enum_type = _WIFIRESULT
_WIFIGUESTACCESSSETRESPONSE.fields_by_name['result'].enum_type = _WIFIRESULT
_WIFINEIGHBORAPSGET_NEIGHBORAPINFO.fields_by_name['band'].enum_type = _WIFIBAND
_WIFINEIGHBORAPSGET_NEIGHBORAPINFO.containing_type = _WIFINEIGHBORAPSGET
_WIFINEIGHBORAPSGET.fields_by_name['neighbor_aps'].message_type = _WIFINEIGHBORAPSGET_NEIGHBORAPINFO
_WIFIREPEATEDAPSGET_REPEATEDAPINFO.fields_by_name['band'].enum_type = _WIFIBAND
_WIFIREPEATEDAPSGET_REPEATEDAPINFO.containing_type = _WIFIREPEATEDAPSGET
_WIFIREPEATEDAPSGET.fields_by_name['repeated_aps'].message_type = _WIFIREPEATEDAPSGET_REPEATEDAPINFO
_WIFICONNECTEDSTATIONSGET_CONNECTEDSTATIONINFO.fields_by_name['vap_type'].enum_type = _WIFIVAPTYPE
_WIFICONNECTEDSTATIONSGET_CONNECTEDSTATIONINFO.fields_by_name['band'].enum_type = _WIFIBAND
_WIFICONNECTEDSTATIONSGET_CONNECTEDSTATIONINFO.containing_type = _WIFICONNECTEDSTATIONSGET
_WIFICONNECTEDSTATIONSGET.fields_by_name['connected_stations'].message_type = _WIFICONNECTEDSTATIONSGET_CONNECTEDSTATIONINFO
_WIFIREPEATERPARAMETERSSET.fields_by_name['primary_band'].enum_type = _WIFIBAND
_WIFIREPEATERPARAMETERSSETRESPONSE.fields_by_name['result'].enum_type = _WIFIRESULT
_WIFIWPSPBCSTART.fields_by_name['result'].enum_type = _WIFIRESULT
_WIFIREPEATERWPSCLONEPBCSTART.fields_by_name['result'].enum_type = _WIFIRESULT
DESCRIPTOR.message_types_by_name['WifiParametersSet'] = _WIFIPARAMETERSSET
DESCRIPTOR.message_types_by_name['WifiParametersSetResponse'] = _WIFIPARAMETERSSETRESPONSE
DESCRIPTOR.message_types_by_name['WifiGuestAccessSet'] = _WIFIGUESTACCESSSET
DESCRIPTOR.message_types_by_name['WifiGuestAccessSetResponse'] = _WIFIGUESTACCESSSETRESPONSE
DESCRIPTOR.message_types_by_name['WifiGuestAccessGet'] = _WIFIGUESTACCESSGET
DESCRIPTOR.message_types_by_name['WifiNeighborAPsGet'] = _WIFINEIGHBORAPSGET
DESCRIPTOR.message_types_by_name['WifiRepeatedAPsGet'] = _WIFIREPEATEDAPSGET
DESCRIPTOR.message_types_by_name['WifiConnectedStationsGet'] = _WIFICONNECTEDSTATIONSGET
DESCRIPTOR.message_types_by_name['WifiRepeaterParametersSet'] = _WIFIREPEATERPARAMETERSSET
DESCRIPTOR.message_types_by_name['WifiRepeaterParametersSetResponse'] = _WIFIREPEATERPARAMETERSSETRESPONSE
DESCRIPTOR.message_types_by_name['WifiWpsPbcStart'] = _WIFIWPSPBCSTART
DESCRIPTOR.message_types_by_name['WifiRepeaterWpsClonePbcStart'] = _WIFIREPEATERWPSCLONEPBCSTART
DESCRIPTOR.enum_types_by_name['WifiResult'] = _WIFIRESULT
DESCRIPTOR.enum_types_by_name['WifiBand'] = _WIFIBAND
DESCRIPTOR.enum_types_by_name['WifiVAPType'] = _WIFIVAPTYPE

WifiParametersSet = _reflection.GeneratedProtocolMessageType('WifiParametersSet', (_message.Message,), dict(
  DESCRIPTOR = _WIFIPARAMETERSSET,
  __module__ = 'devolo_idl_proto_deviceapi_wifinetwork_pb2'
  # @@protoc_insertion_point(class_scope:device.api.WifiParametersSet)
  ))
_sym_db.RegisterMessage(WifiParametersSet)

WifiParametersSetResponse = _reflection.GeneratedProtocolMessageType('WifiParametersSetResponse', (_message.Message,), dict(
  DESCRIPTOR = _WIFIPARAMETERSSETRESPONSE,
  __module__ = 'devolo_idl_proto_deviceapi_wifinetwork_pb2'
  # @@protoc_insertion_point(class_scope:device.api.WifiParametersSetResponse)
  ))
_sym_db.RegisterMessage(WifiParametersSetResponse)

WifiGuestAccessSet = _reflection.GeneratedProtocolMessageType('WifiGuestAccessSet', (_message.Message,), dict(
  DESCRIPTOR = _WIFIGUESTACCESSSET,
  __module__ = 'devolo_idl_proto_deviceapi_wifinetwork_pb2'
  # @@protoc_insertion_point(class_scope:device.api.WifiGuestAccessSet)
  ))
_sym_db.RegisterMessage(WifiGuestAccessSet)

WifiGuestAccessSetResponse = _reflection.GeneratedProtocolMessageType('WifiGuestAccessSetResponse', (_message.Message,), dict(
  DESCRIPTOR = _WIFIGUESTACCESSSETRESPONSE,
  __module__ = 'devolo_idl_proto_deviceapi_wifinetwork_pb2'
  # @@protoc_insertion_point(class_scope:device.api.WifiGuestAccessSetResponse)
  ))
_sym_db.RegisterMessage(WifiGuestAccessSetResponse)

WifiGuestAccessGet = _reflection.GeneratedProtocolMessageType('WifiGuestAccessGet', (_message.Message,), dict(
  DESCRIPTOR = _WIFIGUESTACCESSGET,
  __module__ = 'devolo_idl_proto_deviceapi_wifinetwork_pb2'
  # @@protoc_insertion_point(class_scope:device.api.WifiGuestAccessGet)
  ))
_sym_db.RegisterMessage(WifiGuestAccessGet)

WifiNeighborAPsGet = _reflection.GeneratedProtocolMessageType('WifiNeighborAPsGet', (_message.Message,), dict(

  NeighborAPInfo = _reflection.GeneratedProtocolMessageType('NeighborAPInfo', (_message.Message,), dict(
    DESCRIPTOR = _WIFINEIGHBORAPSGET_NEIGHBORAPINFO,
    __module__ = 'devolo_idl_proto_deviceapi_wifinetwork_pb2'
    # @@protoc_insertion_point(class_scope:device.api.WifiNeighborAPsGet.NeighborAPInfo)
    ))
  ,
  DESCRIPTOR = _WIFINEIGHBORAPSGET,
  __module__ = 'devolo_idl_proto_deviceapi_wifinetwork_pb2'
  # @@protoc_insertion_point(class_scope:device.api.WifiNeighborAPsGet)
  ))
_sym_db.RegisterMessage(WifiNeighborAPsGet)
_sym_db.RegisterMessage(WifiNeighborAPsGet.NeighborAPInfo)

WifiRepeatedAPsGet = _reflection.GeneratedProtocolMessageType('WifiRepeatedAPsGet', (_message.Message,), dict(

  RepeatedAPInfo = _reflection.GeneratedProtocolMessageType('RepeatedAPInfo', (_message.Message,), dict(
    DESCRIPTOR = _WIFIREPEATEDAPSGET_REPEATEDAPINFO,
    __module__ = 'devolo_idl_proto_deviceapi_wifinetwork_pb2'
    # @@protoc_insertion_point(class_scope:device.api.WifiRepeatedAPsGet.RepeatedAPInfo)
    ))
  ,
  DESCRIPTOR = _WIFIREPEATEDAPSGET,
  __module__ = 'devolo_idl_proto_deviceapi_wifinetwork_pb2'
  # @@protoc_insertion_point(class_scope:device.api.WifiRepeatedAPsGet)
  ))
_sym_db.RegisterMessage(WifiRepeatedAPsGet)
_sym_db.RegisterMessage(WifiRepeatedAPsGet.RepeatedAPInfo)

WifiConnectedStationsGet = _reflection.GeneratedProtocolMessageType('WifiConnectedStationsGet', (_message.Message,), dict(

  ConnectedStationInfo = _reflection.GeneratedProtocolMessageType('ConnectedStationInfo', (_message.Message,), dict(
    DESCRIPTOR = _WIFICONNECTEDSTATIONSGET_CONNECTEDSTATIONINFO,
    __module__ = 'devolo_idl_proto_deviceapi_wifinetwork_pb2'
    # @@protoc_insertion_point(class_scope:device.api.WifiConnectedStationsGet.ConnectedStationInfo)
    ))
  ,
  DESCRIPTOR = _WIFICONNECTEDSTATIONSGET,
  __module__ = 'devolo_idl_proto_deviceapi_wifinetwork_pb2'
  # @@protoc_insertion_point(class_scope:device.api.WifiConnectedStationsGet)
  ))
_sym_db.RegisterMessage(WifiConnectedStationsGet)
_sym_db.RegisterMessage(WifiConnectedStationsGet.ConnectedStationInfo)

WifiRepeaterParametersSet = _reflection.GeneratedProtocolMessageType('WifiRepeaterParametersSet', (_message.Message,), dict(
  DESCRIPTOR = _WIFIREPEATERPARAMETERSSET,
  __module__ = 'devolo_idl_proto_deviceapi_wifinetwork_pb2'
  # @@protoc_insertion_point(class_scope:device.api.WifiRepeaterParametersSet)
  ))
_sym_db.RegisterMessage(WifiRepeaterParametersSet)

WifiRepeaterParametersSetResponse = _reflection.GeneratedProtocolMessageType('WifiRepeaterParametersSetResponse', (_message.Message,), dict(
  DESCRIPTOR = _WIFIREPEATERPARAMETERSSETRESPONSE,
  __module__ = 'devolo_idl_proto_deviceapi_wifinetwork_pb2'
  # @@protoc_insertion_point(class_scope:device.api.WifiRepeaterParametersSetResponse)
  ))
_sym_db.RegisterMessage(WifiRepeaterParametersSetResponse)

WifiWpsPbcStart = _reflection.GeneratedProtocolMessageType('WifiWpsPbcStart', (_message.Message,), dict(
  DESCRIPTOR = _WIFIWPSPBCSTART,
  __module__ = 'devolo_idl_proto_deviceapi_wifinetwork_pb2'
  # @@protoc_insertion_point(class_scope:device.api.WifiWpsPbcStart)
  ))
_sym_db.RegisterMessage(WifiWpsPbcStart)

WifiRepeaterWpsClonePbcStart = _reflection.GeneratedProtocolMessageType('WifiRepeaterWpsClonePbcStart', (_message.Message,), dict(
  DESCRIPTOR = _WIFIREPEATERWPSCLONEPBCSTART,
  __module__ = 'devolo_idl_proto_deviceapi_wifinetwork_pb2'
  # @@protoc_insertion_point(class_scope:device.api.WifiRepeaterWpsClonePbcStart)
  ))
_sym_db.RegisterMessage(WifiRepeaterWpsClonePbcStart)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\006deviceB\013wifinetwork'))
# @@protoc_insertion_point(module_scope)
