#!/usr/bin/env sh
PROTO_PATH=addressbook/proto

mkdir -p ${PROTO_PATH}/build

docker run \
	--rm \
	-v $(realpath ${PROTO_PATH}):/user-src:rw \
	-u 1000:1000 \
	-w /user-src \
	znly/protoc --python_out=build/ -I. src/addressbook.proto