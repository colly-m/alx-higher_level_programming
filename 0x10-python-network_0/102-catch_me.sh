#!/bin/bash
# Script to make a request to 0.0.0.0:5000/catch_me to cause a You got me! response
curl -s -X PUT "$url=http://0.0.0.0:5000/catch_me" -d "user_id=123"
