# An example script to know the ip address of the Website of your Choice
# Author : Sayantan Pal
# Date : 16.03.2019
import socket  # for socket
import sys
print(
    """
Welcome to IP ADDRESS Finder !!

Note : The format for giving input which are accepted :

1) example.com
2) www.example.com

** NOTE --> https://example.com/ (IS NOT ACCEPTED)
"""
)
website = input("Enter the link of the website in above mentioned format : ")

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print ("ERROR : socket creation failed with error %s" % (err))

# default port for socket
port = 80

try:
    host_ip = socket.gethostbyname(website)
except socket.gaierror:

    # this means could not resolve the host
    print ("There was an error resolving the host (Please dont use https while giving input)")
    sys.exit()

# connecting to the server
s.connect((host_ip, port))

print ("\nIP address found : %s" % (host_ip))
