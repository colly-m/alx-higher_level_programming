#!/bin/bash
# Script to send a request URL passed as an arg and displays only the status code
curl -I -s -o /dev/null -w "%{http_code}" "$1"
