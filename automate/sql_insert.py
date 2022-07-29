#Noah Burnette
#Last Update 5/20/22

import mysql.connector
import sys
import yaml

log_file = open("automate.log","a")

def prep_statement():#Reads from yaml file and helps prepare sql query
    prep_str = ""
    for k in sql_yaml['table_cols']:
        prep_str += k+", " 
    prep_str = prep_str[:-2]  
    return prep_str

def sql_insert(uncommitted_file):
    try:
        r_file = open(uncommitted_file,"r") #Opens file specified
        try:
            r_file_contents = r_file.read()
        except:
            print(uncommitted_file,"could not be read. Check permissions",file=log_file)
    except:
        print(uncommitted_file,"could not be opened",file = log_file)

    r_file_contents = r_file_contents.replace("\n\n","\n").split("\n") #newline is added from 'whoami' command

    content_list = []

    for i in r_file_contents:#Removes the spaces from each index
        content_list.append(str(i)[27:])
    try:
        with open('automate_config.yml', 'r') as file:#opens config.yml file
            global sql_yaml
            sql_yaml = yaml.safe_load(file)
        try:
            db = mysql.connector.connect( #Connection specified in config.yml
                host = sql_yaml['mysql']['host'],
                database = sql_yaml['mysql']['database'],
                user = sql_yaml['mysql']['user'],
                password = sql_yaml['mysql']['password'])
            
            table_name = sql_yaml['mysql']['table']
        except:
            print("Did not read yaml file correctly, please look to confirm format is correct.",file=log_file)
    except:
        print("Could not open yaml file. Ensure yaml file is titled 'automate_config.yml'",file=log_file)
        
    cursor = db.cursor()
    rem_duplicate = ("Delete from "+table_name+" where uuid = %s")#query that checks for duplicates
    rem_data = (content_list[5],)#UUID index

    try:
        cursor.execute(rem_duplicate,rem_data)
    finally:
        prep_str = prep_statement()
        
        ############################## SQL Query that inserts data into db
        add_computer = "INSERT INTO "+table_name+" ("+prep_str+") "+"VALUES ("+"%s, "*len(sql_yaml['table_cols'])
        add_computer = add_computer[:-2]#Removes Last two characters ', '
        add_computer += ")"
        ##################################################################                                  
        computer_data = tuple(content_list)
        cursor.execute(add_computer,computer_data[:-1])

        db.commit()#commits the insertion to the db
        cursor.close()
        db.close()

        r_file.close()#closes file that contains computer info
    


if len(sys.argv) == 1: #Checks for args
    print("Usage: <Files>")
    quit()

for i in range(1,len(sys.argv)):
    sql_insert(sys.argv[i])

log_file.close()
