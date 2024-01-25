#!/bin/bash
# Script to send DELETE request to URL passed as first arg and displays response
curl -X DELETE -s "$1"
