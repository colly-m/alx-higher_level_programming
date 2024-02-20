#!/bin/bash
# Script to take URL and display all HTTP methods accepted by server
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
