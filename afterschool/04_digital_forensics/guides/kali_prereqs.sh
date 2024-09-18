#!/bin/bash
# This script installs necessary dependencies on Debian/Kali Linux
# Requires elevated privileges

# Turning on repositories for specific packages
echo "Turning on only necessary repositories for apt..."
sudo sed -Ei '/^# deb-src .* main/ s/^# //' /etc/apt/sources.list
if [[ $? -ne 0 ]]; then
    echo "Failed to turn on necessary repositories" >>/dev/stderr
    exit 1
fi

echo "Updating package list..."
sudo apt update

# Install required dependencies without affecting desktop environment
echo "Installing all apt dependencies..."
sudo apt -y install \
    openjdk-17-jdk openjdk-17-jre \
    build-essential autoconf libtool automake git zip wget ant \
    libde265-dev libheif-dev \
    libpq-dev \
    testdisk libafflib-dev libewf-dev libvhdi-dev libvmdk-dev \
    libgstreamer1.0-0 gstreamer1.0-plugins-base gstreamer1.0-plugins-good \
    libgstreamer1.0-dev  # Add only relevant gstreamer packages

if [[ $? -ne 0 ]]; then
    echo "Failed to install necessary dependencies" >>/dev/stderr
    exit 1
fi

# Check if desktop environment is intact
echo "Checking if GNOME desktop is installed..."
if ! dpkg -l | grep -q "kali-desktop-gnome"; then
    echo "GNOME desktop not found, reinstalling..."
    sudo apt -y install kali-desktop-gnome
fi

echo "Cleaning up..."
sudo apt autoremove -y
sudo apt clean

echo "Autopsy prerequisites installed."
echo "Java 17 installation: "
update-java-alternatives -l | grep java-1.17
