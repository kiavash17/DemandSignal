
#!/bin/bash

# Check if running as root for necessary permissions
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root or use sudo"
  exit
fi

# Install Redis if not installed
if ! command -v redis-server &> /dev/null; then
  echo "Installing Redis..."
  if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    apt-get update
    apt-get install -y redis-server
  elif [[ "$OSTYPE" == "darwin"* ]]; then
    brew install redis
  fi
else
  echo "Redis is already installed."
fi

# Enable Redis to start on boot
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  systemctl enable redis-server
  systemctl start redis-server
elif [[ "$OSTYPE" == "darwin"* ]]; then
  brew services start redis
fi

echo "Setup complete. Redis should now be installed and running."
