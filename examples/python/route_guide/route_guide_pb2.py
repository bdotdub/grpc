# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: route_guide.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='route_guide.proto',
  package='routeguide',
  syntax='proto3',
  serialized_pb=b'\n\x11route_guide.proto\x12\nrouteguide\",\n\x05Point\x12\x10\n\x08latitude\x18\x01 \x01(\x05\x12\x11\n\tlongitude\x18\x02 \x01(\x05\"I\n\tRectangle\x12\x1d\n\x02lo\x18\x01 \x01(\x0b\x32\x11.routeguide.Point\x12\x1d\n\x02hi\x18\x02 \x01(\x0b\x32\x11.routeguide.Point\"<\n\x07\x46\x65\x61ture\x12\x0c\n\x04name\x18\x01 \x01(\t\x12#\n\x08location\x18\x02 \x01(\x0b\x32\x11.routeguide.Point\"A\n\tRouteNote\x12#\n\x08location\x18\x01 \x01(\x0b\x32\x11.routeguide.Point\x12\x0f\n\x07message\x18\x02 \x01(\t\"b\n\x0cRouteSummary\x12\x13\n\x0bpoint_count\x18\x01 \x01(\x05\x12\x15\n\rfeature_count\x18\x02 \x01(\x05\x12\x10\n\x08\x64istance\x18\x03 \x01(\x05\x12\x14\n\x0c\x65lapsed_time\x18\x04 \x01(\x05\x32\x85\x02\n\nRouteGuide\x12\x36\n\nGetFeature\x12\x11.routeguide.Point\x1a\x13.routeguide.Feature\"\x00\x12>\n\x0cListFeatures\x12\x15.routeguide.Rectangle\x1a\x13.routeguide.Feature\"\x00\x30\x01\x12>\n\x0bRecordRoute\x12\x11.routeguide.Point\x1a\x18.routeguide.RouteSummary\"\x00(\x01\x12?\n\tRouteChat\x12\x15.routeguide.RouteNote\x1a\x15.routeguide.RouteNote\"\x00(\x01\x30\x01\x42\x0f\n\x07\x65x.grpc\xa2\x02\x03RTGb\x06proto3'
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_POINT = _descriptor.Descriptor(
  name='Point',
  full_name='routeguide.Point',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude', full_name='routeguide.Point.latitude', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='routeguide.Point.longitude', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=33,
  serialized_end=77,
)


_RECTANGLE = _descriptor.Descriptor(
  name='Rectangle',
  full_name='routeguide.Rectangle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lo', full_name='routeguide.Rectangle.lo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hi', full_name='routeguide.Rectangle.hi', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=79,
  serialized_end=152,
)


_FEATURE = _descriptor.Descriptor(
  name='Feature',
  full_name='routeguide.Feature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='routeguide.Feature.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='location', full_name='routeguide.Feature.location', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=154,
  serialized_end=214,
)


_ROUTENOTE = _descriptor.Descriptor(
  name='RouteNote',
  full_name='routeguide.RouteNote',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='location', full_name='routeguide.RouteNote.location', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='routeguide.RouteNote.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=216,
  serialized_end=281,
)


_ROUTESUMMARY = _descriptor.Descriptor(
  name='RouteSummary',
  full_name='routeguide.RouteSummary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='point_count', full_name='routeguide.RouteSummary.point_count', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='feature_count', full_name='routeguide.RouteSummary.feature_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='distance', full_name='routeguide.RouteSummary.distance', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='elapsed_time', full_name='routeguide.RouteSummary.elapsed_time', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=283,
  serialized_end=381,
)

_RECTANGLE.fields_by_name['lo'].message_type = _POINT
_RECTANGLE.fields_by_name['hi'].message_type = _POINT
_FEATURE.fields_by_name['location'].message_type = _POINT
_ROUTENOTE.fields_by_name['location'].message_type = _POINT
DESCRIPTOR.message_types_by_name['Point'] = _POINT
DESCRIPTOR.message_types_by_name['Rectangle'] = _RECTANGLE
DESCRIPTOR.message_types_by_name['Feature'] = _FEATURE
DESCRIPTOR.message_types_by_name['RouteNote'] = _ROUTENOTE
DESCRIPTOR.message_types_by_name['RouteSummary'] = _ROUTESUMMARY

Point = _reflection.GeneratedProtocolMessageType('Point', (_message.Message,), dict(
  DESCRIPTOR = _POINT,
  __module__ = 'route_guide_pb2'
  # @@protoc_insertion_point(class_scope:routeguide.Point)
  ))
_sym_db.RegisterMessage(Point)

Rectangle = _reflection.GeneratedProtocolMessageType('Rectangle', (_message.Message,), dict(
  DESCRIPTOR = _RECTANGLE,
  __module__ = 'route_guide_pb2'
  # @@protoc_insertion_point(class_scope:routeguide.Rectangle)
  ))
_sym_db.RegisterMessage(Rectangle)

Feature = _reflection.GeneratedProtocolMessageType('Feature', (_message.Message,), dict(
  DESCRIPTOR = _FEATURE,
  __module__ = 'route_guide_pb2'
  # @@protoc_insertion_point(class_scope:routeguide.Feature)
  ))
_sym_db.RegisterMessage(Feature)

RouteNote = _reflection.GeneratedProtocolMessageType('RouteNote', (_message.Message,), dict(
  DESCRIPTOR = _ROUTENOTE,
  __module__ = 'route_guide_pb2'
  # @@protoc_insertion_point(class_scope:routeguide.RouteNote)
  ))
_sym_db.RegisterMessage(RouteNote)

RouteSummary = _reflection.GeneratedProtocolMessageType('RouteSummary', (_message.Message,), dict(
  DESCRIPTOR = _ROUTESUMMARY,
  __module__ = 'route_guide_pb2'
  # @@protoc_insertion_point(class_scope:routeguide.RouteSummary)
  ))
_sym_db.RegisterMessage(RouteSummary)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), b'\n\007ex.grpc\242\002\003RTG')
import abc
from grpc.beta import implementations as beta_implementations
from grpc.early_adopter import implementations as early_adopter_implementations
from grpc.framework.alpha import utilities as alpha_utilities
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
class EarlyAdopterRouteGuideServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def GetFeature(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def ListFeatures(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def RecordRoute(self, request_iterator, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def RouteChat(self, request_iterator, context):
    raise NotImplementedError()
class EarlyAdopterRouteGuideServer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def start(self):
    raise NotImplementedError()
  @abc.abstractmethod
  def stop(self):
    raise NotImplementedError()
class EarlyAdopterRouteGuideStub(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def GetFeature(self, request):
    raise NotImplementedError()
  GetFeature.async = None
  @abc.abstractmethod
  def ListFeatures(self, request):
    raise NotImplementedError()
  ListFeatures.async = None
  @abc.abstractmethod
  def RecordRoute(self, request_iterator):
    raise NotImplementedError()
  RecordRoute.async = None
  @abc.abstractmethod
  def RouteChat(self, request_iterator):
    raise NotImplementedError()
  RouteChat.async = None
def early_adopter_create_RouteGuide_server(servicer, port, private_key=None, certificate_chain=None):
  import route_guide_pb2
  import route_guide_pb2
  import route_guide_pb2
  import route_guide_pb2
  import route_guide_pb2
  import route_guide_pb2
  import route_guide_pb2
  import route_guide_pb2
  method_service_descriptions = {
    "GetFeature": alpha_utilities.unary_unary_service_description(
      servicer.GetFeature,
      route_guide_pb2.Point.FromString,
      route_guide_pb2.Feature.SerializeToString,
    ),
    "ListFeatures": alpha_utilities.unary_stream_service_description(
      servicer.ListFeatures,
      route_guide_pb2.Rectangle.FromString,
      route_guide_pb2.Feature.SerializeToString,
    ),
    "RecordRoute": alpha_utilities.stream_unary_service_description(
      servicer.RecordRoute,
      route_guide_pb2.Point.FromString,
      route_guide_pb2.RouteSummary.SerializeToString,
    ),
    "RouteChat": alpha_utilities.stream_stream_service_description(
      servicer.RouteChat,
      route_guide_pb2.RouteNote.FromString,
      route_guide_pb2.RouteNote.SerializeToString,
    ),
  }
  return early_adopter_implementations.server("routeguide.RouteGuide", method_service_descriptions, port, private_key=private_key, certificate_chain=certificate_chain)
def early_adopter_create_RouteGuide_stub(host, port, metadata_transformer=None, secure=False, root_certificates=None, private_key=None, certificate_chain=None, server_host_override=None):
  import route_guide_pb2
  import route_guide_pb2
  import route_guide_pb2
  import route_guide_pb2
  import route_guide_pb2
  import route_guide_pb2
  import route_guide_pb2
  import route_guide_pb2
  method_invocation_descriptions = {
    "GetFeature": alpha_utilities.unary_unary_invocation_description(
      route_guide_pb2.Point.SerializeToString,
      route_guide_pb2.Feature.FromString,
    ),
    "ListFeatures": alpha_utilities.unary_stream_invocation_description(
      route_guide_pb2.Rectangle.SerializeToString,
      route_guide_pb2.Feature.FromString,
    ),
    "RecordRoute": alpha_utilities.stream_unary_invocation_description(
      route_guide_pb2.Point.SerializeToString,
      route_guide_pb2.RouteSummary.FromString,
    ),
    "RouteChat": alpha_utilities.stream_stream_invocation_description(
      route_guide_pb2.RouteNote.SerializeToString,
      route_guide_pb2.RouteNote.FromString,
    ),
  }
  return early_adopter_implementations.stub("routeguide.RouteGuide", method_invocation_descriptions, host, port, metadata_transformer=metadata_transformer, secure=secure, root_certificates=root_certificates, private_key=private_key, certificate_chain=certificate_chain, server_host_override=server_host_override)

class BetaRouteGuideServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def GetFeature(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def ListFeatures(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def RecordRoute(self, request_iterator, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def RouteChat(self, request_iterator, context):
    raise NotImplementedError()

class BetaRouteGuideStub(object):
  """The interface to which stubs will conform."""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def GetFeature(self, request, timeout):
    raise NotImplementedError()
  GetFeature.future = None
  @abc.abstractmethod
  def ListFeatures(self, request, timeout):
    raise NotImplementedError()
  @abc.abstractmethod
  def RecordRoute(self, request_iterator, timeout):
    raise NotImplementedError()
  RecordRoute.future = None
  @abc.abstractmethod
  def RouteChat(self, request_iterator, timeout):
    raise NotImplementedError()

def beta_create_RouteGuide_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  import route_guide_pb2
  import route_guide_pb2
  import route_guide_pb2
  import route_guide_pb2
  import route_guide_pb2
  import route_guide_pb2
  import route_guide_pb2
  import route_guide_pb2
  request_deserializers = {
    ('routeguide.RouteGuide', 'GetFeature'): route_guide_pb2.Point.FromString,
    ('routeguide.RouteGuide', 'ListFeatures'): route_guide_pb2.Rectangle.FromString,
    ('routeguide.RouteGuide', 'RecordRoute'): route_guide_pb2.Point.FromString,
    ('routeguide.RouteGuide', 'RouteChat'): route_guide_pb2.RouteNote.FromString,
  }
  response_serializers = {
    ('routeguide.RouteGuide', 'GetFeature'): route_guide_pb2.Feature.SerializeToString,
    ('routeguide.RouteGuide', 'ListFeatures'): route_guide_pb2.Feature.SerializeToString,
    ('routeguide.RouteGuide', 'RecordRoute'): route_guide_pb2.RouteSummary.SerializeToString,
    ('routeguide.RouteGuide', 'RouteChat'): route_guide_pb2.RouteNote.SerializeToString,
  }
  method_implementations = {
    ('routeguide.RouteGuide', 'GetFeature'): face_utilities.unary_unary_inline(servicer.GetFeature),
    ('routeguide.RouteGuide', 'ListFeatures'): face_utilities.unary_stream_inline(servicer.ListFeatures),
    ('routeguide.RouteGuide', 'RecordRoute'): face_utilities.stream_unary_inline(servicer.RecordRoute),
    ('routeguide.RouteGuide', 'RouteChat'): face_utilities.stream_stream_inline(servicer.RouteChat),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)

def beta_create_RouteGuide_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  import route_guide_pb2
  import route_guide_pb2
  import route_guide_pb2
  import route_guide_pb2
  import route_guide_pb2
  import route_guide_pb2
  import route_guide_pb2
  import route_guide_pb2
  request_serializers = {
    ('routeguide.RouteGuide', 'GetFeature'): route_guide_pb2.Point.SerializeToString,
    ('routeguide.RouteGuide', 'ListFeatures'): route_guide_pb2.Rectangle.SerializeToString,
    ('routeguide.RouteGuide', 'RecordRoute'): route_guide_pb2.Point.SerializeToString,
    ('routeguide.RouteGuide', 'RouteChat'): route_guide_pb2.RouteNote.SerializeToString,
  }
  response_deserializers = {
    ('routeguide.RouteGuide', 'GetFeature'): route_guide_pb2.Feature.FromString,
    ('routeguide.RouteGuide', 'ListFeatures'): route_guide_pb2.Feature.FromString,
    ('routeguide.RouteGuide', 'RecordRoute'): route_guide_pb2.RouteSummary.FromString,
    ('routeguide.RouteGuide', 'RouteChat'): route_guide_pb2.RouteNote.FromString,
  }
  cardinalities = {
    'GetFeature': cardinality.Cardinality.UNARY_UNARY,
    'ListFeatures': cardinality.Cardinality.UNARY_STREAM,
    'RecordRoute': cardinality.Cardinality.STREAM_UNARY,
    'RouteChat': cardinality.Cardinality.STREAM_STREAM,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'routeguide.RouteGuide', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
