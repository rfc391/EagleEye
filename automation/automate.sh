
#!/bin/bash

echo "Starting automated tests and packaging..."

# Run unit tests
echo "Running tests..."
python -m unittest discover -s tests
if [ $? -ne 0 ]; then
    echo "Tests failed. Aborting."
    exit 1
fi

# Package the project
echo "Packaging project..."
zip -r EagleEye-latest.zip . -x "*.git*" "*.DS_Store"

echo "Automation complete. Project packaged as EagleEye-latest.zip."
