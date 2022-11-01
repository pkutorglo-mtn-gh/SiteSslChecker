import socket  # to send messages across networks
import ssl     #
import datetime


class ssl_check():

    def __init__(self, hostname):
        print(hostname)
        # date format from ww3sch
        ssl_date_fmt = r'%b %d %H:%M:%S %Y %Z'
        context = ssl.create_default_context()
        # to wrap a socket., as SSLSocket objects
        # AF_INET for ipv4 representation
        conn = context.wrap_socket(socket.socket(socket.AF_INET),server_hostname=hostname,)
        conn.settimeout(3.0)
        conn.connect((hostname, 443))
        # to  retrieve the SSL certificate from the other endpoint of the communication
        ssl_info = conn.getpeercert()
        Exp_ON=datetime.datetime.strptime(ssl_info['notAfter'], ssl_date_fmt)
        Days_Remaining= Exp_ON - datetime.datetime.utcnow()
        #print ("Expires ON:- %s\nRemaining:- %s" %)
        print (Exp_ON,Days_Remaining)
        print ("----------------------------------")


domains = ['google.com', 'yahoo.com', 'facebook.com', "twitter.com"]

# I am using map function to iterate through the list.

map(ssl_check, domains)
