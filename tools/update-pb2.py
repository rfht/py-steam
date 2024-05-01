#!/usr/bin/env python3

import re
import os
import sys
from ast import literal_eval
import google.protobuf.descriptor_pb2

if len(sys.argv) < 2:
    print(f"missing file argument")
    sys.exit(1)

filedir = os.path.dirname(sys.argv[1])

infile = open(sys.argv[1])
serialized_pb = None
name = None
for line in infile:
    m = re.findall("serialized_pb=(b'.*)", line)
    if m:
        serialized_pb = literal_eval(m[0])
    else:
        m = re.findall("name='([^']*)\.proto", line)
        if m:
                name = m[0]

if not serialized_pb or not name:
    print(f"Couldn't find serialized_pb or name info in {sys.argv[1]}. Aborting.")
    sys.exit(1)

fds = google.protobuf.descriptor_pb2.FileDescriptorSet()
fds.file.append(google.protobuf.descriptor_pb2.FileDescriptorProto())
fds.file[0].ParseFromString(serialized_pb)
#open('myproto.txt', 'w').write(str(fds))	# human-readable output
open(f'/tmp/{name}.pb', 'wb').write(fds.SerializeToString())
os.system(f"protoc --python_out={filedir} --descriptor_set_in=/tmp/{name}.pb --proto_path=py-steam/protobufs {name}.proto")
