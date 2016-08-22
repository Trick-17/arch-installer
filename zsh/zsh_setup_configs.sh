setopt EXTENDED_GLOB
for rcfile in arch-installer/.zprezto/runcoms/^README.md(.N); do
  cp "$rcfile" "/mnt/etc/skel/.${rcfile:t}"
done