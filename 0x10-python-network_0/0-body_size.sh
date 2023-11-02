#!/bin/bash
# will send request an URL, then display the size of the body of the reply
curl -s "$1" | wc -c
