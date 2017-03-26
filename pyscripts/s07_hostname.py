
print(" >> Setting hostname")

def setup_hostname(user_input):
    with open('/mnt/etc/hostname', 'w') as text_file:
        text_file.write(user_input['hostname'])
    
    with open('/mnt/etc/hosts', 'a') as text_file:
        text_file.write('\n127.0.1.1\t' + user_input['hostname'])

# TODO:
#sed -i "/^127/ s/$/ ${USER_HOSTNAME}/" /mnt/etc/hosts
#sed -i "/^::1/ s/$/ ${USER_HOSTNAME}/" /mnt/etc/hosts