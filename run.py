#!/usr/bin/env python
# The Shebang tell the computer what to call the file with when it runs.
# For more info:https://bash.cyberciti.biz/guide/Shebang

import flywheel
import os

context = flywheel.GearContext()  # Get the gear context
config = context.config           # from the gear context, get the config settings

## Load in values from the gear configuration
my_name = config['my_name']
num_rep = config['num_rep']

## Load in paths to input files for the gear
message_file = context.get_input_path('message_file')

while (num_rep > 0):                      # While the num_rep variable is greater than zero:

    print("Hello, {}!".format(my_name))   # Print "Hello Name!" every loop
    num_rep -= 1                          # Decrease the num_rep variable by one

# Now read the custom message:
message_file = open(message_file,'r')   # Open the file with the intent to read
print('\n')                               # Print a blank line to separate the message from the "hello's"
print(message_file.read())
# Read and print the file
os.system("echo 'echo $MYENV'")
os.system('echo $MYENV')


