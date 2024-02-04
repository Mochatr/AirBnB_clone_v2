#!/usr/bin/env bash
# sets up web servers for the deployment of web_static

# Update package
sudo apt-get -y update

# Install nginx
sudo apt-get -y install nginx

# Create the directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "Hello world!" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give the ownership of the /data/ folder to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content
sudo sed -i '/listen 80 default_server;/a location /hbnb_static/ { alias /data/web_static/current/; }' /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx start
