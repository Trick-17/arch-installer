#!/bin/bash

/bin/cp -rf /usr/share/archiso/configs/releng/. .
echo "git" >> packages.both
echo "reflector" >> packages.both

sudo ./build.sh -v