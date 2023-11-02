#!/bin/bash
# does send JSON POST request to a URL, and displays the body of the reply.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
