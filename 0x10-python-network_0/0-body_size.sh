#!/bin/bash
# will send request an URL, then display the size of the body of the response
curl -s "$1" | wc -c
