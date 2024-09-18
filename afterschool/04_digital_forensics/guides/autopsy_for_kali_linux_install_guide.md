# Overview
As of the writing of this guide, the current version of Autopsy (version 4.21.0) is not easily installed on non-Windows systems. This guide's objective is to provide an easy-way to automate the installation of Autopsy on Kali Linux installations for cybersecurity students who want to learn disk image forensics. The current version of the installation script is tied to the links to Autopsy version 4.21.0 and Sleuthkit version 4.12.1. The script requires sudo permissions to run, because it downloads and installs a programs to you Kali Linux system.
## 
```
#!/bin/bash

#### 111 Downloading the files and scripts 111

wget -P ~/Downloads https://github.com/sleuthkit/autopsy/releases/download/autopsy-4.21.0/autopsy-4.21.0.zip 
wget -P ~/Downloads https://github.com/sleuthkit/sleuthkit/releases/download/sleuthkit-4.12.1/sleuthkit-java_4.12.1-1_amd64.deb
wget -P ~/Downloads https://raw.githubusercontent.com/sleuthkit/autopsy/develop/linux_macos_install_scripts/install_prereqs_ubuntu.sh
chmod +x ~/Downloads/install_prereqs_ubuntu.sh
wget -P ~/Downloads https://raw.githubusercontent.com/sleuthkit/autopsy/develop/linux_macos_install_scripts/install_application.sh
chmod +x ~/Downloads/install_application.sh

#### 222 Running the prereqs script 222
~/Downloads/install_prereqs_ubuntu.sh

#### 333 Removing the current version of the Sleuth kit and replacing it 333
apt remove sleuthkit -y
apt purge sleuthkit -y
apt autoremove -y
apt update -y && apt install ~/Downloads/sleuthkit-java_4.12.1-1_amd64.deb -y

#### 444 Installing Autopsy 444
~/Downloads/install_application.sh -z ~/Downloads/autopsy-4.21.0.zip -i /usr/local/bin/ -j /usr/lib/jvm/java-1.17.0-openjdk-amd64

#### 555 Cleanup 555
rm ~/Downloads/autopsy-4.21.0.zip
rm ~/Downloads/sleuthkit-java_4.12.1-1_amd64.deb
rm ~/Downloads/install_application.sh
rm ~/Downloads/install_prereqs_ubuntu.sh

```
