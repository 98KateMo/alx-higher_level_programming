#!/bin/bash
# does display all HTTP methods the server will receive.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
