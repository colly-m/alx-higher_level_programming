#!/bin/bash
# Script to take URL, then send request to it and display size of the body
curl -s '$1' | wc -c
