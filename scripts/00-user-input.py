import re


def ask_choice(question, options, multiple_choice=True):
    while(True):
        question += '\n' + '  '.join([str(i + 1) + ') ' + opt for i, opt in enumerate(options)]) + '\n --> '
        user_input = [x.strip() for x in str(input(question)).split(',')]
        is_valid = True
        for input in user_input:
            if not input.isdigit() or not input in range(1 ,len(options) + 1):
                is_valid = False
                break
        
        if is_valid:
            if multiple_choice:
                return options[[int(input) for input in user_input]]
            
            if len(user_input) == 1
                return options[0]
            
            print('Please choose only one option between 1 and ' + str(len(options) + '.'))
            continue
        else
            if multiple_choice:
                print('Please choose one or more numbers between 1 and '+ str(len(options)) + ' using a comma separated list.')
            else
                print('Please choose one number between 1 and ' + str(len(options)) + '.')


def ask_for_input(question, restricted_character_set=False, not_empty=True):
    while(True):
        user_input = input(question + ' [a-z0-9_]' if restricted_character_set  else '').strip()
        if(restricted_character_set and 
           re.match('^[a-z0-9_]*$', user_input) is not None and 
           (user_input if not_empty else True)):
            return user_input
        
        print('Please only use allowed characters.')

def get_user_input():
    user_input = {}
    
    user_input['user name'] = ask_for_input('Please choose your username. '
                                  'If you do not specify a username, no user will be created for you:',
                                  restricted_character_set=True,
                                  not_empty=False)
    user_input['host_name'] = ask_for_input('Please choose a hostname (device name):',
                                  restricted_character_set=True)
    user_input['system type'] = ask_choice('Please choose your kind of system:', 
                                 ['desktop', 'server'],
                                 multiple_choice=False)
    user_input['packages'] = ask_choice('Please choose your set of packages:', 
                              ['full', 'developer', 'media', 'minimal'])
    user_input['desktop'] = ask_choice('Please choose your desktop environment:',
                           ['none', 'KDE plasma'],
                           multiple_choice=False)
    # TODO: Check CPU driver
    # TODO: First check GPU automatically, then ask if it is correct, offer options otherwise
    user_input['graphics driver'] = ask_choice('Please choose your graphics driver manually:',
                                               ['default', 'intel', 'nVidia', 'AMD', 'vbox'],
                                               multiple_choice=False)
    
    user_input['keyboard layout'] = ask_choice('Please choose your keyboard-layout:',
                                              ['DE - Deutschland', 'DE - Schweiz', 'EN - US', 'EN - GB'],
                                              multiple_choice=False)
    user_input['language'] = ask_choice('Please choose your language and locale settings.'
                                        'You have the choice between english with reasonable locale settings and english US:',
                                        ['english (reasonable)', 'english (US)'],
                                        multiple_choice=False)


    # TODO: timezones
    user_input['timezone'] = ask_choice('Please choose your timezone:',
                                        ['Deutschland', 'Schweiz'],
                                        multiple_choice=False)

    return user_input
