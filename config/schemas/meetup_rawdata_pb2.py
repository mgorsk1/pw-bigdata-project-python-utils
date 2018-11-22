# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: meetup-rawdata.proto

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
  name='meetup-rawdata.proto',
  package='project.bd.pw',
  syntax='proto2',
  serialized_pb=_b('\n\x14meetup-rawdata.proto\x12\rproject.bd.pw\"\xb9\n\n\x03MSG\x12\'\n\x05venue\x18\x01 \x01(\x0b\x32\x18.project.bd.pw.MSG.VENUE\x12\x12\n\nvisibility\x18\x02 \x02(\t\x12\x10\n\x08response\x18\x03 \x02(\t\x12\x0e\n\x06guests\x18\x04 \x02(\x01\x12)\n\x06member\x18\x05 \x02(\x0b\x32\x19.project.bd.pw.MSG.MEMBER\x12\x0f\n\x07rsvp_id\x18\x06 \x02(\x01\x12\r\n\x05mtime\x18\x07 \x02(\x01\x12\'\n\x05\x65vent\x18\x08 \x02(\x0b\x32\x18.project.bd.pw.MSG.EVENT\x12\'\n\x05group\x18\n \x02(\x0b\x32\x18.project.bd.pw.MSG.GROUP\x1aG\n\x05VENUE\x12\x12\n\nvenue_name\x18\x01 \x01(\t\x12\x0b\n\x03lon\x18\x02 \x02(\x01\x12\x0b\n\x03lat\x18\x03 \x02(\x01\x12\x10\n\x08venue_id\x18\x04 \x02(\x01\x1a\xfe\x04\n\x06MEMBER\x12\x11\n\tmember_id\x18\x01 \x02(\x01\x12@\n\x0eother_services\x18\x02 \x01(\x0b\x32(.project.bd.pw.MSG.MEMBER.OTHER_SERVICES\x12\r\n\x05photo\x18\x03 \x01(\t\x12\x13\n\x0bmember_name\x18\x04 \x02(\t\x1a\xfa\x03\n\x0eOTHER_SERVICES\x12\x41\n\x07twitter\x18\x01 \x01(\x0b\x32\x30.project.bd.pw.MSG.MEMBER.OTHER_SERVICES.TWITTER\x12\x43\n\x08\x66\x61\x63\x65\x62ook\x18\x02 \x01(\x0b\x32\x31.project.bd.pw.MSG.MEMBER.OTHER_SERVICES.FACEBOOK\x12?\n\x06tumblr\x18\x03 \x01(\x0b\x32/.project.bd.pw.MSG.MEMBER.OTHER_SERVICES.TUMBLR\x12?\n\x06\x66lickr\x18\x04 \x01(\x0b\x32/.project.bd.pw.MSG.MEMBER.OTHER_SERVICES.FLICKR\x12\x43\n\x08linkedin\x18\x05 \x01(\x0b\x32\x31.project.bd.pw.MSG.MEMBER.OTHER_SERVICES.LINKEDIN\x1a\x1d\n\x07TWITTER\x12\x12\n\nidentifier\x18\x01 \x02(\t\x1a\x1e\n\x08\x46\x41\x43\x45\x42OOK\x12\x12\n\nidentifier\x18\x01 \x02(\t\x1a\x1c\n\x06TUMBLR\x12\x12\n\nidentifier\x18\x01 \x02(\t\x1a\x1c\n\x06\x46LICKR\x12\x12\n\nidentifier\x18\x01 \x02(\t\x1a\x1e\n\x08LINKEDIN\x12\x12\n\nidentifier\x18\x01 \x02(\t\x1aN\n\x05\x45VENT\x12\x12\n\nevent_name\x18\x01 \x02(\t\x12\x10\n\x08\x65vent_id\x18\x02 \x02(\t\x12\x0c\n\x04time\x18\x03 \x01(\x01\x12\x11\n\tevent_url\x18\x04 \x02(\t\x1a\x9b\x02\n\x05GROUP\x12;\n\x0cgroup_topics\x18\x01 \x03(\x0b\x32%.project.bd.pw.MSG.GROUP.GROUP_TOPICS\x12\x12\n\ngroup_city\x18\x02 \x02(\t\x12\x15\n\rgroup_country\x18\x03 \x02(\t\x12\x10\n\x08group_id\x18\x04 \x02(\x01\x12\x12\n\ngroup_name\x18\x05 \x02(\t\x12\x11\n\tgroup_lon\x18\x06 \x02(\x01\x12\x15\n\rgroup_urlname\x18\x07 \x02(\t\x12\x13\n\x0bgroup_state\x18\x08 \x01(\t\x12\x11\n\tgroup_lat\x18\t \x02(\x01\x1a\x32\n\x0cGROUP_TOPICS\x12\x0e\n\x06urlkey\x18\x01 \x02(\t\x12\x12\n\ntopic_name\x18\x02 \x02(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MSG_VENUE = _descriptor.Descriptor(
  name='VENUE',
  full_name='project.bd.pw.MSG.VENUE',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='venue_name', full_name='project.bd.pw.MSG.VENUE.venue_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lon', full_name='project.bd.pw.MSG.VENUE.lon', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lat', full_name='project.bd.pw.MSG.VENUE.lat', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='venue_id', full_name='project.bd.pw.MSG.VENUE.venue_id', index=3,
      number=4, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=299,
  serialized_end=370,
)

_MSG_MEMBER_OTHER_SERVICES_TWITTER = _descriptor.Descriptor(
  name='TWITTER',
  full_name='project.bd.pw.MSG.MEMBER.OTHER_SERVICES.TWITTER',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifier', full_name='project.bd.pw.MSG.MEMBER.OTHER_SERVICES.TWITTER.identifier', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=858,
  serialized_end=887,
)

_MSG_MEMBER_OTHER_SERVICES_FACEBOOK = _descriptor.Descriptor(
  name='FACEBOOK',
  full_name='project.bd.pw.MSG.MEMBER.OTHER_SERVICES.FACEBOOK',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifier', full_name='project.bd.pw.MSG.MEMBER.OTHER_SERVICES.FACEBOOK.identifier', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=889,
  serialized_end=919,
)

_MSG_MEMBER_OTHER_SERVICES_TUMBLR = _descriptor.Descriptor(
  name='TUMBLR',
  full_name='project.bd.pw.MSG.MEMBER.OTHER_SERVICES.TUMBLR',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifier', full_name='project.bd.pw.MSG.MEMBER.OTHER_SERVICES.TUMBLR.identifier', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=921,
  serialized_end=949,
)

_MSG_MEMBER_OTHER_SERVICES_FLICKR = _descriptor.Descriptor(
  name='FLICKR',
  full_name='project.bd.pw.MSG.MEMBER.OTHER_SERVICES.FLICKR',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifier', full_name='project.bd.pw.MSG.MEMBER.OTHER_SERVICES.FLICKR.identifier', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=951,
  serialized_end=979,
)

_MSG_MEMBER_OTHER_SERVICES_LINKEDIN = _descriptor.Descriptor(
  name='LINKEDIN',
  full_name='project.bd.pw.MSG.MEMBER.OTHER_SERVICES.LINKEDIN',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifier', full_name='project.bd.pw.MSG.MEMBER.OTHER_SERVICES.LINKEDIN.identifier', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=981,
  serialized_end=1011,
)

_MSG_MEMBER_OTHER_SERVICES = _descriptor.Descriptor(
  name='OTHER_SERVICES',
  full_name='project.bd.pw.MSG.MEMBER.OTHER_SERVICES',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='twitter', full_name='project.bd.pw.MSG.MEMBER.OTHER_SERVICES.twitter', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='facebook', full_name='project.bd.pw.MSG.MEMBER.OTHER_SERVICES.facebook', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tumblr', full_name='project.bd.pw.MSG.MEMBER.OTHER_SERVICES.tumblr', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='flickr', full_name='project.bd.pw.MSG.MEMBER.OTHER_SERVICES.flickr', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='linkedin', full_name='project.bd.pw.MSG.MEMBER.OTHER_SERVICES.linkedin', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_MSG_MEMBER_OTHER_SERVICES_TWITTER, _MSG_MEMBER_OTHER_SERVICES_FACEBOOK, _MSG_MEMBER_OTHER_SERVICES_TUMBLR, _MSG_MEMBER_OTHER_SERVICES_FLICKR, _MSG_MEMBER_OTHER_SERVICES_LINKEDIN, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=505,
  serialized_end=1011,
)

_MSG_MEMBER = _descriptor.Descriptor(
  name='MEMBER',
  full_name='project.bd.pw.MSG.MEMBER',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='member_id', full_name='project.bd.pw.MSG.MEMBER.member_id', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='other_services', full_name='project.bd.pw.MSG.MEMBER.other_services', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='photo', full_name='project.bd.pw.MSG.MEMBER.photo', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='member_name', full_name='project.bd.pw.MSG.MEMBER.member_name', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_MSG_MEMBER_OTHER_SERVICES, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=373,
  serialized_end=1011,
)

_MSG_EVENT = _descriptor.Descriptor(
  name='EVENT',
  full_name='project.bd.pw.MSG.EVENT',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_name', full_name='project.bd.pw.MSG.EVENT.event_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='event_id', full_name='project.bd.pw.MSG.EVENT.event_id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time', full_name='project.bd.pw.MSG.EVENT.time', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='event_url', full_name='project.bd.pw.MSG.EVENT.event_url', index=3,
      number=4, type=9, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1013,
  serialized_end=1091,
)

_MSG_GROUP_GROUP_TOPICS = _descriptor.Descriptor(
  name='GROUP_TOPICS',
  full_name='project.bd.pw.MSG.GROUP.GROUP_TOPICS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='urlkey', full_name='project.bd.pw.MSG.GROUP.GROUP_TOPICS.urlkey', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='topic_name', full_name='project.bd.pw.MSG.GROUP.GROUP_TOPICS.topic_name', index=1,
      number=2, type=9, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1327,
  serialized_end=1377,
)

_MSG_GROUP = _descriptor.Descriptor(
  name='GROUP',
  full_name='project.bd.pw.MSG.GROUP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='group_topics', full_name='project.bd.pw.MSG.GROUP.group_topics', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group_city', full_name='project.bd.pw.MSG.GROUP.group_city', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group_country', full_name='project.bd.pw.MSG.GROUP.group_country', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group_id', full_name='project.bd.pw.MSG.GROUP.group_id', index=3,
      number=4, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group_name', full_name='project.bd.pw.MSG.GROUP.group_name', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group_lon', full_name='project.bd.pw.MSG.GROUP.group_lon', index=5,
      number=6, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group_urlname', full_name='project.bd.pw.MSG.GROUP.group_urlname', index=6,
      number=7, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group_state', full_name='project.bd.pw.MSG.GROUP.group_state', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group_lat', full_name='project.bd.pw.MSG.GROUP.group_lat', index=8,
      number=9, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_MSG_GROUP_GROUP_TOPICS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1094,
  serialized_end=1377,
)

_MSG = _descriptor.Descriptor(
  name='MSG',
  full_name='project.bd.pw.MSG',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='venue', full_name='project.bd.pw.MSG.venue', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='visibility', full_name='project.bd.pw.MSG.visibility', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='response', full_name='project.bd.pw.MSG.response', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='guests', full_name='project.bd.pw.MSG.guests', index=3,
      number=4, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='member', full_name='project.bd.pw.MSG.member', index=4,
      number=5, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rsvp_id', full_name='project.bd.pw.MSG.rsvp_id', index=5,
      number=6, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='project.bd.pw.MSG.mtime', index=6,
      number=7, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='event', full_name='project.bd.pw.MSG.event', index=7,
      number=8, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group', full_name='project.bd.pw.MSG.group', index=8,
      number=10, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_MSG_VENUE, _MSG_MEMBER, _MSG_EVENT, _MSG_GROUP, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=1377,
)

_MSG_VENUE.containing_type = _MSG
_MSG_MEMBER_OTHER_SERVICES_TWITTER.containing_type = _MSG_MEMBER_OTHER_SERVICES
_MSG_MEMBER_OTHER_SERVICES_FACEBOOK.containing_type = _MSG_MEMBER_OTHER_SERVICES
_MSG_MEMBER_OTHER_SERVICES_TUMBLR.containing_type = _MSG_MEMBER_OTHER_SERVICES
_MSG_MEMBER_OTHER_SERVICES_FLICKR.containing_type = _MSG_MEMBER_OTHER_SERVICES
_MSG_MEMBER_OTHER_SERVICES_LINKEDIN.containing_type = _MSG_MEMBER_OTHER_SERVICES
_MSG_MEMBER_OTHER_SERVICES.fields_by_name['twitter'].message_type = _MSG_MEMBER_OTHER_SERVICES_TWITTER
_MSG_MEMBER_OTHER_SERVICES.fields_by_name['facebook'].message_type = _MSG_MEMBER_OTHER_SERVICES_FACEBOOK
_MSG_MEMBER_OTHER_SERVICES.fields_by_name['tumblr'].message_type = _MSG_MEMBER_OTHER_SERVICES_TUMBLR
_MSG_MEMBER_OTHER_SERVICES.fields_by_name['flickr'].message_type = _MSG_MEMBER_OTHER_SERVICES_FLICKR
_MSG_MEMBER_OTHER_SERVICES.fields_by_name['linkedin'].message_type = _MSG_MEMBER_OTHER_SERVICES_LINKEDIN
_MSG_MEMBER_OTHER_SERVICES.containing_type = _MSG_MEMBER
_MSG_MEMBER.fields_by_name['other_services'].message_type = _MSG_MEMBER_OTHER_SERVICES
_MSG_MEMBER.containing_type = _MSG
_MSG_EVENT.containing_type = _MSG
_MSG_GROUP_GROUP_TOPICS.containing_type = _MSG_GROUP
_MSG_GROUP.fields_by_name['group_topics'].message_type = _MSG_GROUP_GROUP_TOPICS
_MSG_GROUP.containing_type = _MSG
_MSG.fields_by_name['venue'].message_type = _MSG_VENUE
_MSG.fields_by_name['member'].message_type = _MSG_MEMBER
_MSG.fields_by_name['event'].message_type = _MSG_EVENT
_MSG.fields_by_name['group'].message_type = _MSG_GROUP
DESCRIPTOR.message_types_by_name['MSG'] = _MSG

MSG = _reflection.GeneratedProtocolMessageType('MSG', (_message.Message,), dict(

  VENUE = _reflection.GeneratedProtocolMessageType('VENUE', (_message.Message,), dict(
    DESCRIPTOR = _MSG_VENUE,
    __module__ = 'meetup_rawdata_pb2'
    # @@protoc_insertion_point(class_scope:project.bd.pw.MSG.VENUE)
    ))
  ,

  MEMBER = _reflection.GeneratedProtocolMessageType('MEMBER', (_message.Message,), dict(

    OTHER_SERVICES = _reflection.GeneratedProtocolMessageType('OTHER_SERVICES', (_message.Message,), dict(

      TWITTER = _reflection.GeneratedProtocolMessageType('TWITTER', (_message.Message,), dict(
        DESCRIPTOR = _MSG_MEMBER_OTHER_SERVICES_TWITTER,
        __module__ = 'meetup_rawdata_pb2'
        # @@protoc_insertion_point(class_scope:project.bd.pw.MSG.MEMBER.OTHER_SERVICES.TWITTER)
        ))
      ,

      FACEBOOK = _reflection.GeneratedProtocolMessageType('FACEBOOK', (_message.Message,), dict(
        DESCRIPTOR = _MSG_MEMBER_OTHER_SERVICES_FACEBOOK,
        __module__ = 'meetup_rawdata_pb2'
        # @@protoc_insertion_point(class_scope:project.bd.pw.MSG.MEMBER.OTHER_SERVICES.FACEBOOK)
        ))
      ,

      TUMBLR = _reflection.GeneratedProtocolMessageType('TUMBLR', (_message.Message,), dict(
        DESCRIPTOR = _MSG_MEMBER_OTHER_SERVICES_TUMBLR,
        __module__ = 'meetup_rawdata_pb2'
        # @@protoc_insertion_point(class_scope:project.bd.pw.MSG.MEMBER.OTHER_SERVICES.TUMBLR)
        ))
      ,

      FLICKR = _reflection.GeneratedProtocolMessageType('FLICKR', (_message.Message,), dict(
        DESCRIPTOR = _MSG_MEMBER_OTHER_SERVICES_FLICKR,
        __module__ = 'meetup_rawdata_pb2'
        # @@protoc_insertion_point(class_scope:project.bd.pw.MSG.MEMBER.OTHER_SERVICES.FLICKR)
        ))
      ,

      LINKEDIN = _reflection.GeneratedProtocolMessageType('LINKEDIN', (_message.Message,), dict(
        DESCRIPTOR = _MSG_MEMBER_OTHER_SERVICES_LINKEDIN,
        __module__ = 'meetup_rawdata_pb2'
        # @@protoc_insertion_point(class_scope:project.bd.pw.MSG.MEMBER.OTHER_SERVICES.LINKEDIN)
        ))
      ,
      DESCRIPTOR = _MSG_MEMBER_OTHER_SERVICES,
      __module__ = 'meetup_rawdata_pb2'
      # @@protoc_insertion_point(class_scope:project.bd.pw.MSG.MEMBER.OTHER_SERVICES)
      ))
    ,
    DESCRIPTOR = _MSG_MEMBER,
    __module__ = 'meetup_rawdata_pb2'
    # @@protoc_insertion_point(class_scope:project.bd.pw.MSG.MEMBER)
    ))
  ,

  EVENT = _reflection.GeneratedProtocolMessageType('EVENT', (_message.Message,), dict(
    DESCRIPTOR = _MSG_EVENT,
    __module__ = 'meetup_rawdata_pb2'
    # @@protoc_insertion_point(class_scope:project.bd.pw.MSG.EVENT)
    ))
  ,

  GROUP = _reflection.GeneratedProtocolMessageType('GROUP', (_message.Message,), dict(

    GROUP_TOPICS = _reflection.GeneratedProtocolMessageType('GROUP_TOPICS', (_message.Message,), dict(
      DESCRIPTOR = _MSG_GROUP_GROUP_TOPICS,
      __module__ = 'meetup_rawdata_pb2'
      # @@protoc_insertion_point(class_scope:project.bd.pw.MSG.GROUP.GROUP_TOPICS)
      ))
    ,
    DESCRIPTOR = _MSG_GROUP,
    __module__ = 'meetup_rawdata_pb2'
    # @@protoc_insertion_point(class_scope:project.bd.pw.MSG.GROUP)
    ))
  ,
  DESCRIPTOR = _MSG,
  __module__ = 'meetup_rawdata_pb2'
  # @@protoc_insertion_point(class_scope:project.bd.pw.MSG)
  ))
_sym_db.RegisterMessage(MSG)
_sym_db.RegisterMessage(MSG.VENUE)
_sym_db.RegisterMessage(MSG.MEMBER)
_sym_db.RegisterMessage(MSG.MEMBER.OTHER_SERVICES)
_sym_db.RegisterMessage(MSG.MEMBER.OTHER_SERVICES.TWITTER)
_sym_db.RegisterMessage(MSG.MEMBER.OTHER_SERVICES.FACEBOOK)
_sym_db.RegisterMessage(MSG.MEMBER.OTHER_SERVICES.TUMBLR)
_sym_db.RegisterMessage(MSG.MEMBER.OTHER_SERVICES.FLICKR)
_sym_db.RegisterMessage(MSG.MEMBER.OTHER_SERVICES.LINKEDIN)
_sym_db.RegisterMessage(MSG.EVENT)
_sym_db.RegisterMessage(MSG.GROUP)
_sym_db.RegisterMessage(MSG.GROUP.GROUP_TOPICS)


# @@protoc_insertion_point(module_scope)