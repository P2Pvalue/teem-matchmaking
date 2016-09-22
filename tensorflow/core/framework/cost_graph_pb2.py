# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/framework/cost_graph.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/framework/cost_graph.proto',
  package='tensorflow',
  syntax='proto3',
  serialized_pb=_b('\n*tensorflow/core/framework/cost_graph.proto\x12\ntensorflow\"\xa5\x03\n\x0c\x43ostGraphDef\x12+\n\x04node\x18\x01 \x03(\x0b\x32\x1d.tensorflow.CostGraphDef.Node\x1a\xe7\x02\n\x04Node\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65vice\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\x05\x12;\n\ninput_info\x18\x04 \x03(\x0b\x32\'.tensorflow.CostGraphDef.Node.InputInfo\x12=\n\x0boutput_info\x18\x05 \x03(\x0b\x32(.tensorflow.CostGraphDef.Node.OutputInfo\x12\x1d\n\x15temporary_memory_size\x18\x06 \x01(\x03\x12\x10\n\x08is_final\x18\x07 \x01(\x08\x12\x15\n\rcontrol_input\x18\x08 \x03(\x05\x1a;\n\tInputInfo\x12\x16\n\x0epreceding_node\x18\x01 \x01(\x05\x12\x16\n\x0epreceding_port\x18\x02 \x01(\x05\x1a\x34\n\nOutputInfo\x12\x0c\n\x04size\x18\x01 \x01(\x03\x12\x18\n\x10\x61lias_input_port\x18\x02 \x01(\x03\x42\x30\n\x18org.tensorflow.frameworkB\x0f\x43ostGraphProtosP\x01\xf8\x01\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_COSTGRAPHDEF_NODE_INPUTINFO = _descriptor.Descriptor(
  name='InputInfo',
  full_name='tensorflow.CostGraphDef.Node.InputInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='preceding_node', full_name='tensorflow.CostGraphDef.Node.InputInfo.preceding_node', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='preceding_port', full_name='tensorflow.CostGraphDef.Node.InputInfo.preceding_port', index=1,
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
  serialized_start=367,
  serialized_end=426,
)

_COSTGRAPHDEF_NODE_OUTPUTINFO = _descriptor.Descriptor(
  name='OutputInfo',
  full_name='tensorflow.CostGraphDef.Node.OutputInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='size', full_name='tensorflow.CostGraphDef.Node.OutputInfo.size', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='alias_input_port', full_name='tensorflow.CostGraphDef.Node.OutputInfo.alias_input_port', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=428,
  serialized_end=480,
)

_COSTGRAPHDEF_NODE = _descriptor.Descriptor(
  name='Node',
  full_name='tensorflow.CostGraphDef.Node',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tensorflow.CostGraphDef.Node.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device', full_name='tensorflow.CostGraphDef.Node.device', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='tensorflow.CostGraphDef.Node.id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='input_info', full_name='tensorflow.CostGraphDef.Node.input_info', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_info', full_name='tensorflow.CostGraphDef.Node.output_info', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='temporary_memory_size', full_name='tensorflow.CostGraphDef.Node.temporary_memory_size', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_final', full_name='tensorflow.CostGraphDef.Node.is_final', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='control_input', full_name='tensorflow.CostGraphDef.Node.control_input', index=7,
      number=8, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_COSTGRAPHDEF_NODE_INPUTINFO, _COSTGRAPHDEF_NODE_OUTPUTINFO, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=480,
)

_COSTGRAPHDEF = _descriptor.Descriptor(
  name='CostGraphDef',
  full_name='tensorflow.CostGraphDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node', full_name='tensorflow.CostGraphDef.node', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_COSTGRAPHDEF_NODE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=59,
  serialized_end=480,
)

_COSTGRAPHDEF_NODE_INPUTINFO.containing_type = _COSTGRAPHDEF_NODE
_COSTGRAPHDEF_NODE_OUTPUTINFO.containing_type = _COSTGRAPHDEF_NODE
_COSTGRAPHDEF_NODE.fields_by_name['input_info'].message_type = _COSTGRAPHDEF_NODE_INPUTINFO
_COSTGRAPHDEF_NODE.fields_by_name['output_info'].message_type = _COSTGRAPHDEF_NODE_OUTPUTINFO
_COSTGRAPHDEF_NODE.containing_type = _COSTGRAPHDEF
_COSTGRAPHDEF.fields_by_name['node'].message_type = _COSTGRAPHDEF_NODE
DESCRIPTOR.message_types_by_name['CostGraphDef'] = _COSTGRAPHDEF

CostGraphDef = _reflection.GeneratedProtocolMessageType('CostGraphDef', (_message.Message,), dict(

  Node = _reflection.GeneratedProtocolMessageType('Node', (_message.Message,), dict(

    InputInfo = _reflection.GeneratedProtocolMessageType('InputInfo', (_message.Message,), dict(
      DESCRIPTOR = _COSTGRAPHDEF_NODE_INPUTINFO,
      __module__ = 'tensorflow.core.framework.cost_graph_pb2'
      # @@protoc_insertion_point(class_scope:tensorflow.CostGraphDef.Node.InputInfo)
      ))
    ,

    OutputInfo = _reflection.GeneratedProtocolMessageType('OutputInfo', (_message.Message,), dict(
      DESCRIPTOR = _COSTGRAPHDEF_NODE_OUTPUTINFO,
      __module__ = 'tensorflow.core.framework.cost_graph_pb2'
      # @@protoc_insertion_point(class_scope:tensorflow.CostGraphDef.Node.OutputInfo)
      ))
    ,
    DESCRIPTOR = _COSTGRAPHDEF_NODE,
    __module__ = 'tensorflow.core.framework.cost_graph_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.CostGraphDef.Node)
    ))
  ,
  DESCRIPTOR = _COSTGRAPHDEF,
  __module__ = 'tensorflow.core.framework.cost_graph_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.CostGraphDef)
  ))
_sym_db.RegisterMessage(CostGraphDef)
_sym_db.RegisterMessage(CostGraphDef.Node)
_sym_db.RegisterMessage(CostGraphDef.Node.InputInfo)
_sym_db.RegisterMessage(CostGraphDef.Node.OutputInfo)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\030org.tensorflow.frameworkB\017CostGraphProtosP\001\370\001\001'))
# @@protoc_insertion_point(module_scope)
