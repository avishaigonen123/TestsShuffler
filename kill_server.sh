#!/bin/bash

# Search for the Python script process and extract its PID
pid=$(ps aux | grep 'python server/server.py' | grep -v grep | awk '{print $2}')

# If the PID is found, kill the process
if [ -n "$pid" ]; then
    echo "Terminating Python script with PID $pid..."
    kill "$pid"
    echo "Python script terminated."
else
    echo "No Python script process found."
fi

