#!/bin/bash

# This script sends 310 requests to the API and captures the output.

# Empty file to store results
output_file="curl_outputs.txt"
> "$output_file"  # Clear the file content if it exists

# Send multiple requests in a loop
for i in {1..310}; do
  # Send a POST request and append output to the file
  curl -s -X POST http://localhost:5000/api/jumble/1 \
  -H "Content-Type: application/json" \
  -d '{"message": "test"}' >> "$output_file" &
done

# Wait for all background jobs to finish
wait

# Print the last 10 outputs from the file
tail -n 10 "$output_file"