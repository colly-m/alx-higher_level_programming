#!/bin/bash
# Script to take URL, send a POST request passed URL, and display response
curl -s -X POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
