
#!/bin/bash

# Update package lists
sudo apt-get update

# Install Python3 and pip if not already installed
sudo apt-get install -y python3 python3-pip

# Install necessary Python packages
pip3 install -r requirements.txt

# Download spaCy English model
python3 -m spacy download en_core_web_sm

# Confirm setup completion
echo "Setup completed. All necessary packages are installed."
