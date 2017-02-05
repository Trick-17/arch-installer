
print(" >> Setting hostname")

open('/mnt/etc/hostname', 'w').write(user_input['hostname'])

# TODO:
#sed -i "/^127/ s/$/ ${USER_HOSTNAME}/" /mnt/etc/hosts
#sed -i "/^::1/ s/$/ ${USER_HOSTNAME}/" /mnt/etc/hosts