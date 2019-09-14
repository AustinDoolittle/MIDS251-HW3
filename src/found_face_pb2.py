# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: found_face.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='found_face.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10\x66ound_face.proto\"\xbd\x01\n\tFoundFace\x12\x11\n\tsource_id\x18\x01 \x01(\t\x12\x12\n\nsession_id\x18\x02 \x01(\t\x12\x12\n\nimage_data\x18\x03 \x01(\x0c\x12\x14\n\x0c\x66rame_number\x18\x04 \x01(\x05\x12$\n\x04\x62\x62ox\x18\x05 \x01(\x0b\x32\x16.FoundFace.BoundingBox\x1a\x39\n\x0b\x42oundingBox\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01w\x18\x03 \x01(\x02\x12\t\n\x01h\x18\x04 \x01(\x02\x62\x06proto3')
)




_FOUNDFACE_BOUNDINGBOX = _descriptor.Descriptor(
  name='BoundingBox',
  full_name='FoundFace.BoundingBox',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='FoundFace.BoundingBox.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='FoundFace.BoundingBox.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='w', full_name='FoundFace.BoundingBox.w', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='h', full_name='FoundFace.BoundingBox.h', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=153,
  serialized_end=210,
)

_FOUNDFACE = _descriptor.Descriptor(
  name='FoundFace',
  full_name='FoundFace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source_id', full_name='FoundFace.source_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='session_id', full_name='FoundFace.session_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image_data', full_name='FoundFace.image_data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frame_number', full_name='FoundFace.frame_number', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bbox', full_name='FoundFace.bbox', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FOUNDFACE_BOUNDINGBOX, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=210,
)

_FOUNDFACE_BOUNDINGBOX.containing_type = _FOUNDFACE
_FOUNDFACE.fields_by_name['bbox'].message_type = _FOUNDFACE_BOUNDINGBOX
DESCRIPTOR.message_types_by_name['FoundFace'] = _FOUNDFACE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FoundFace = _reflection.GeneratedProtocolMessageType('FoundFace', (_message.Message,), {

  'BoundingBox' : _reflection.GeneratedProtocolMessageType('BoundingBox', (_message.Message,), {
    'DESCRIPTOR' : _FOUNDFACE_BOUNDINGBOX,
    '__module__' : 'found_face_pb2'
    # @@protoc_insertion_point(class_scope:FoundFace.BoundingBox)
    })
  ,
  'DESCRIPTOR' : _FOUNDFACE,
  '__module__' : 'found_face_pb2'
  # @@protoc_insertion_point(class_scope:FoundFace)
  })
_sym_db.RegisterMessage(FoundFace)
_sym_db.RegisterMessage(FoundFace.BoundingBox)


# @@protoc_insertion_point(module_scope)