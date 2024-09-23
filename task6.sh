#!/bin/bash

# Activate the virtual environment (if you are using one)
source venv/bin/activate

# Run pytest and store the exit code
pytest
exit_code=$?

# Deactivate the virtual environment (optional)
deactivate

# Exit with pytest's exit code
if [ $exit_code -eq 0 ]; then
    echo "All tests passed."
    exit 0
else
    echo "Some tests failed or there was an error."
    exit 1
fi