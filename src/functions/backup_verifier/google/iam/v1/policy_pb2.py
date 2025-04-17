# -*- coding: utf-8 -*-

# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/iam/v1/policy.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.type import expr_pb2 as google_dot_type_dot_expr__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1agoogle/iam/v1/policy.proto\x12\rgoogle.iam.v1\x1a\x16google/type/expr.proto"\x84\x01\n\x06Policy\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12(\n\x08\x62indings\x18\x04 \x03(\x0b\x32\x16.google.iam.v1.Binding\x12\x31\n\raudit_configs\x18\x06 \x03(\x0b\x32\x1a.google.iam.v1.AuditConfig\x12\x0c\n\x04\x65tag\x18\x03 \x01(\x0c"N\n\x07\x42inding\x12\x0c\n\x04role\x18\x01 \x01(\t\x12\x0f\n\x07members\x18\x02 \x03(\t\x12$\n\tcondition\x18\x03 \x01(\x0b\x32\x11.google.type.Expr"X\n\x0b\x41uditConfig\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x38\n\x11\x61udit_log_configs\x18\x03 \x03(\x0b\x32\x1d.google.iam.v1.AuditLogConfig"\xb7\x01\n\x0e\x41uditLogConfig\x12\x37\n\x08log_type\x18\x01 \x01(\x0e\x32%.google.iam.v1.AuditLogConfig.LogType\x12\x18\n\x10\x65xempted_members\x18\x02 \x03(\t"R\n\x07LogType\x12\x18\n\x14LOG_TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nADMIN_READ\x10\x01\x12\x0e\n\nDATA_WRITE\x10\x02\x12\r\n\tDATA_READ\x10\x03"\x80\x01\n\x0bPolicyDelta\x12\x33\n\x0e\x62inding_deltas\x18\x01 \x03(\x0b\x32\x1b.google.iam.v1.BindingDelta\x12<\n\x13\x61udit_config_deltas\x18\x02 \x03(\x0b\x32\x1f.google.iam.v1.AuditConfigDelta"\xbd\x01\n\x0c\x42indingDelta\x12\x32\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32".google.iam.v1.BindingDelta.Action\x12\x0c\n\x04role\x18\x02 \x01(\t\x12\x0e\n\x06member\x18\x03 \x01(\t\x12$\n\tcondition\x18\x04 \x01(\x0b\x32\x11.google.type.Expr"5\n\x06\x41\x63tion\x12\x16\n\x12\x41\x43TION_UNSPECIFIED\x10\x00\x12\x07\n\x03\x41\x44\x44\x10\x01\x12\n\n\x06REMOVE\x10\x02"\xbd\x01\n\x10\x41uditConfigDelta\x12\x36\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32&.google.iam.v1.AuditConfigDelta.Action\x12\x0f\n\x07service\x18\x02 \x01(\t\x12\x17\n\x0f\x65xempted_member\x18\x03 \x01(\t\x12\x10\n\x08log_type\x18\x04 \x01(\t"5\n\x06\x41\x63tion\x12\x16\n\x12\x41\x43TION_UNSPECIFIED\x10\x00\x12\x07\n\x03\x41\x44\x44\x10\x01\x12\n\n\x06REMOVE\x10\x02\x42|\n\x11\x63om.google.iam.v1B\x0bPolicyProtoP\x01Z)cloud.google.com/go/iam/apiv1/iampb;iampb\xf8\x01\x01\xaa\x02\x13Google.Cloud.Iam.V1\xca\x02\x13Google\\Cloud\\Iam\\V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "google.iam.v1.policy_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\021com.google.iam.v1B\013PolicyProtoP\001Z)cloud.google.com/go/iam/apiv1/iampb;iampb\370\001\001\252\002\023Google.Cloud.Iam.V1\312\002\023Google\\Cloud\\Iam\\V1"
    _globals["_POLICY"]._serialized_start = 70
    _globals["_POLICY"]._serialized_end = 202
    _globals["_BINDING"]._serialized_start = 204
    _globals["_BINDING"]._serialized_end = 282
    _globals["_AUDITCONFIG"]._serialized_start = 284
    _globals["_AUDITCONFIG"]._serialized_end = 372
    _globals["_AUDITLOGCONFIG"]._serialized_start = 375
    _globals["_AUDITLOGCONFIG"]._serialized_end = 558
    _globals["_AUDITLOGCONFIG_LOGTYPE"]._serialized_start = 476
    _globals["_AUDITLOGCONFIG_LOGTYPE"]._serialized_end = 558
    _globals["_POLICYDELTA"]._serialized_start = 561
    _globals["_POLICYDELTA"]._serialized_end = 689
    _globals["_BINDINGDELTA"]._serialized_start = 692
    _globals["_BINDINGDELTA"]._serialized_end = 881
    _globals["_BINDINGDELTA_ACTION"]._serialized_start = 828
    _globals["_BINDINGDELTA_ACTION"]._serialized_end = 881
    _globals["_AUDITCONFIGDELTA"]._serialized_start = 884
    _globals["_AUDITCONFIGDELTA"]._serialized_end = 1073
    _globals["_AUDITCONFIGDELTA_ACTION"]._serialized_start = 828
    _globals["_AUDITCONFIGDELTA_ACTION"]._serialized_end = 881
# @@protoc_insertion_point(module_scope)
