import re
from subprocess import CalledProcessError
from pyscripts.utilities import run


def ask_choice(question, options, multiple_choice=True):
    question += '\n' + \
            '  '.join([str(i + 1) + ') ' + opt for i,
                       opt in enumerate(options)]) + '\n --> '
    while True:
        user_input = [x.strip() for x in str(input(question)).split(',')]
        is_valid = True
        for input_ in user_input:
            if not input_.isdigit() or not int(input_) in range(1, len(options) + 1):
                is_valid = False
                break

        if is_valid:
            if multiple_choice:
                return [options[int(input_)-1] for input_ in user_input]

            if len(user_input) == 1:
                return options[int(user_input[0])-1]

            print('Please choose only one option between 1 and ' +
                  str(len(options) + '.'))
            continue
        else:
            if multiple_choice:
                print('Please choose one or more numbers between 1 and ' +
                      str(len(options)) + ' using a comma separated list.')
            else:
                print('Please choose one number between 1 and ' +
                      str(len(options)) + '.')


def ask_for_input(question, restricted_character_set=False, not_empty=True):
    while True:
        user_input = input(
            question + (' [a-z0-9_]' if restricted_character_set else '') + '\n --> ').strip()
        if(restricted_character_set and
           re.match('^[a-z0-9_]*$', user_input) is not None and
           (user_input if not_empty else True)):
            return user_input

        print('Please only use allowed characters.')


def get_user_input(detected_hardware):
    user_input = {}

    # First ask for keyboard layout
    user_input['keyboard layout'] = ask_choice('Please choose your keyboard-layout:',
                                               ['DE - Deutschland', 'DE - Schweiz',
                                                'EN - US', 'EN - GB'],
                                               multiple_choice=False)

    # And set it immediately for the current installation so that the
    # user can enter his user name etc correctly
    try:
        if user_input['keyboard layout'] == 'DE - Deutschland':
            run("loadkeys de-latin1")
            run("set -x LANG \'en_DK.UTF-8\'")
            run("set -x LC_ALL \'en_DK.UTF-8\'")

        elif user_input['keyboard layout'] == 'DE - Schweiz':
            run("loadkeys sg-latin1")
            run("set -x LANG \'en_DK.UTF-8\'")
            run("set -x LC_ALL \'en_DK.UTF-8\'")

        elif user_input['keyboard layout'] == 'EN - GB':
            run("loadkeys uk")
            run("set -x LANG \'en_US.UTF-8\'")
            run("set -x LC_ALL \'en_US.UTF-8\'")

    except CalledProcessError as error:
        print('Unable to set keyboard to requested model: ' + error.output)


    # User name
    user_input['username'] = ask_for_input('Please choose your username. '
                                            'If you do not specify a username, no user will be created for you:',
                                            restricted_character_set=True,
                                            not_empty=False)
    
    # Host name
    user_input['hostname'] = ask_for_input('Please choose a hostname (device name):',
                                            restricted_character_set=True)

    # Desktop or Server
    user_input['system type'] = ask_choice('Please choose your kind of system:',
                                           ['desktop', 'server'],
                                           multiple_choice=False)

    # Package bundle choices
    if user_input['system type'] == 'desktop':
        user_input['packages'] = ask_choice('Please choose your set of packages:',
                                            ['full', 'developer', 'office', 'media', 'minimal'])
    else:
        user_input['packages'] = ask_choice('Please choose your set of packages:',
                                            ['full', 'developer', 'media', 'minimal'])

    # Choice of desktops
    user_input['desktop'] = ask_choice('Please choose your desktop environment:',
                                       ['none', 'KDE plasma'],
                                       multiple_choice=False)

    # TODO: CPU drivers (including automatic detection)

    # GPU drivers:
    # First check GPU automatically, then ask if it is correct, offer options otherwise
    gpu_is_correct = ask_choice('The following GPU vendor was auto-detected: `'+detected_hardware['gpu']+'`. Is this correct?',
                                ['Yes', 'No'], multiple_choice=False)
    if gpu_is_correct == 'Yes':
        user_input['graphics driver'] = detected_hardware['gpu']
    else:
        user_input['graphics driver'] = ask_choice('Please choose your graphics driver manually:',
                                                   ['default', 'intel',
                                                    'nVidia', 'AMD', 'vbox'],
                                                   multiple_choice=False)

    # Languages
    user_input['language'] = ask_choice('Please choose your language and locale settings.'
                                        'You have the choice between english with reasonable locale settings and english US:',
                                        ['english (reasonable)',
                                         'english (US)'],
                                        multiple_choice=False)

    # Timezones
    user_input['timezone'] = ask_choice('Please choose your timezone:',
                                        ['Deutschland', 'Schweiz'],
                                        multiple_choice=False)

    return user_input