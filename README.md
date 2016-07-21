Arch Installer
==============

This project aims to create an arch distro custom to the authors' needs.
It is based on archiso and takes inspiration from https://blog.chendry.org/automating-arch-linux-installation/,
where you may also find some descriptions to the various scripts etc.


Procedure
---------

The scripts are called by *install.sh* one after another. This should happen automatically due to
*autorun.sh*, which is called on EFI startup of the live iso. 

Note that 02-setup-partitions.sh requires a partition called *Arch*, since this procedure is primarily
intended for re-installation onto a pre-existing partition.