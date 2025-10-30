#!/usr/bin/python3

# INET4031
# Maatii Morke
# Data Created: 10-24-2025
# Date Last Modified: 10-30-2025

# importing os to execute system commands, re for regular expressions, and sys for reading input.
import os
import re
import sys

#YOUR CODE SHOULD HAVE NONE OF THE INSTRUCTORS COMMENTS REMAINING WHEN YOU ARE FINISHED
#PLEASE REPLACE INSTRUCTOR "PROMPTS" WITH COMMENTS OF YOUR OWN

def main():
    for line in sys.stdin:

        #This regular expression checks if the line begins with '#' to identify and skip comment lines in the input file.
        match = re.match("^#",line)
        
        print(match)
        # This splits each line into fields using ':' as a delimiter to seperate the user information values.
        fields = line.strip().split(':')

        print(fields)
        #This IF statement skips any line that starts with '#' or does not contain exactly 5 fields, preventing invalid input from being processed.
        if match or len(fields) != 5:
            continue

        #These three lines again variables from the input fields to match the user information stored in /etc/passwd.
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        #This splits the last field (groups) into a list in case multiple groups are listed, seperated by commas.
        groups = fields[4].split(',')

        #This print statement shows which user account is being created.
        print("==> Creating account for %s..." % (username))
        #This line builds the adduser command with the provided GECOS info and username.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)


        print(cmd)
        os.system(cmd)

        #This print statement indicates that the script is about to set the user's passowrd.
        print("==> Setting the password for %s..." % (username))
        #This line creates a command string to set the user's password by piping it twice into the passwd command.
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        print(cmd)
        os.system(cmd)

        for group in groups:
            #This checks if the group value is not '-' (a placeholder for no groups). If true, it adds the user to the listed group(s).
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()
