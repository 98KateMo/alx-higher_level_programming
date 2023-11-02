#!/bin/bash
# will send a request to a URL, and displays only the status code of the reply.
curl -s -o /dev/null -w "%{http_code}" "$1"
