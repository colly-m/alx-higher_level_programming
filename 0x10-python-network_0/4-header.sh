#!/bin/bash
# Script to take URl as arg, send a GET request then displays the response
curl -s -H "X-School-User-Id: 98" "$1"
