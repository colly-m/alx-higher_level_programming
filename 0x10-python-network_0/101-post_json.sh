#!/bin/bash
# Script to send a JSON POST request to URL passed as first arg and displays response
curl -s -X POST -H "Content-Type: application/json" --data-binary "@$filename" "$url"
