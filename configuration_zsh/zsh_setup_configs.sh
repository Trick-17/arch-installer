setopt EXTENDED_GLOB
for rcfile in /mnt/etc/skel/.zprezto/runcoms/^README.md(.N); do
  ln -s ".zprezto/runcoms/${rcfile:t}" "/mnt/etc/skel/.${rcfile:t}"
done