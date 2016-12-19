#!/bin/bash

echo "--------------------------------------------------------------------------"
echo " "
echo " Arch-Linux - Automated Setup "
echo " "
echo " version 1.0 "
echo " "
echo "--------------------------------------------------------------------------"
echo " "
echo "Waiting for network connection... "
while true
do
   ping -c1 www.google.com &> /dev/null && break
done
echo "done."
echo "---"
echo " "
echo "Downloading install-scripts... "
git clone https://github.com/Trick-17/arch-installer.git
echo "done."
echo "---"
echo " "
echo "Executing Install-scripts... "
echo " "
echo " "
echo "=========================================================================="
./arch-installer/install.sh
