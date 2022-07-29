#Noah Burnette
#Last Update 5/20/22

import subprocess
import socket
import pysftp
import mysql.connector
import yaml

#Global Variables
global log_file 
log_file = open("agent.log","a")

try:
    with open('agent_config.yml', 'r') as file:
            global config
            config = yaml.safe_load(file)
except:
    print("\tCould not open yaml file please ensure the path and name is correct",file = log_file)
    exit

global host_name
host_name = socket.gethostname()

global host_ip
host_ip = socket.gethostbyname(host_name)

global w_file
w_file = open(config['sftp']['localpath']+host_name+".txt",'w')



print(host_name + ": ", file=log_file)

def get_IP():
    try:
        print("IP:"+" "*23,host_ip,file=w_file)
        return host_ip
    except:
        print("\tUnable to get IP. Try cmd -> ipconfig",file=log_file)
        
def get_sysinfo(): #Iterates through windows systeminfo command.
    try:
        sysinfo = subprocess.check_output('systeminfo',shell=True).decode('utf-8').split('\n')
    except:
        print("\tCannot get system information.\nTry win+r -> msinfo32",file=log_file)
    try:
        new = []
        sep = [1,2,10,13,17]
        for item in sysinfo:
            new.append(str(item.split("\r")[:-1]))
        for i in sep:
            print(new[i][2:-2],file=w_file)
    except:
        print("\tCould not iterate through 'systeminfo', command could have failed.",file=log_file)
    try: #Finds UUID
        uuid = subprocess.check_output('wmic csproduct get "UUID"',shell=True).decode('utf-8').split("\n")
        print("UUID:"+" "*(26-len("UUID:")),uuid[1][:-4],file=w_file)#21
    except:
        print("\tCould not get UUID. Try cmd -> wmic csproduct get 'UUID'",file=log_file)
    try:#Finds User
        user = subprocess.check_output('whoami',shell=True).decode('utf-8').split("\n")
        print("User:"+" "*(26-len("User:")),user[0],file=w_file)
    except:
        print("\tCould not find user. Try cmd -> whoami",file=log_file)
    try:
        sn = subprocess.check_output("wmic bios get serialnumber",shell = True).decode('utf-8').replace(" ","").replace("\n","").split("\r")
        print("S/N:"+" "*(26-len("S/N:")),sn[2],file=w_file)
    except:
        print("Could not get serial number, try cmd -> wmic bios get serialnumber",file = log_file)

def check_ip(ip): #Checks ip and determines the location
    loc = ""
    for i in config['sftp']['location']:
        if str(i)[:-1] in ip:
            loc = config['sftp']['location'][i]
    if loc == "":
        loc = "Not Specified"
    print("Location:"+" "*(26-len("Location:")),loc,file=w_file)
        

def to_server(ip): #Sends the file to a sftp server
    if ip == "127.0.0.1":
        return
    try:
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None
        with pysftp.Connection(config['sftp']['host'] , username=config['sftp']['user'], password=config['sftp']['password'],cnopts=cnopts) as sftp:
            with sftp.cd(config['sftp']['abspath']):
                sftp.put(config['sftp']['localpath']+host_name+".txt")
    except:
        print("\tCould not connect to server. Only making a local copy",file=log_file)

def uptime():
    try:
        uptime = subprocess.check_output('powershell (get-date) - (gcim Win32_OperatingSystem).LastBootUpTime',shell=True).decode('utf-8').split('\r\n')
        try:
            total_days = uptime[8].replace(" ","").split(":")
            print(total_days[0]+":"+" "*(26-len(total_days[0]))+total_days[1],file=w_file)
        except:
            print("Could not open write file for uptime",file=log_file)
    except:
        print("Could not get uptime",file=log_file)

def get_signin():
    try:
        signin = subprocess.check_output('echo %date% %time%',shell=True).decode('utf-8').replace('\r\n'," ").split(" ")
        try:
            signin_fin =signin[1]+" "+ signin[2]
        except:
            print("Could not cat date and time strings",file=w_file)
        try:
            print("Sign In Date:"+" "*(26-len("Sign In Date:")),signin_fin,file=w_file)
        except:
            print("Could not write to file for time and date",file=log_file)
                          
    except:
        print("Could not get date and time",file=log_file)
    
    
        
        
        

get_sysinfo()
get_IP()
check_ip(host_ip)
uptime()
get_signin()
w_file.close()
to_server(host_ip)
log_file.close()




