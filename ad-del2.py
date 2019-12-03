import csv, random, string, subprocess, platform
chars = "abcdefghijklmnopqrstuvwxyz"
chars1 = "1234567890"
chars2 = "!%&/()=#"
import random
import string
password = ""

for c in range (2):
    password += random.choice(chars)
    password += random.choice(chars.upper())
    password += random.choice(chars1)
    password += random.choice(chars2)

password = ''.join(random.sample(password,len(password)))
#f= open("losenordfil.txt","a") 
#f.write(password)
#f.write("\n")

print("Password: ", (password))

fields = ['user', "password"] 

rows = [ ['Nikhil', (password)], 
         ['Sanchit', (password)], 
         ['Aditya', (password)], 
         ['Sagar', (password)], 
         ['Prateek', (password)], 
         ['Sahil', (password)]] 

filename = "Auto_AD.csv"

 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 

    # writing the fields 
    csvwriter.writerow(fields) 

    # writing the data rows 
    csvwriter.writerows(rows)


# reading csv file 
with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 

 


 
    for row in csvreader: 
        rows.append(row) 

 
    print("Total no. of rows: %d"%(csvreader.line_num)) 

 
print('Field names are:' + ', '.join(field for field in fields)) 

 
print('\nFirst 5 rows are:\n') 
for row in rows[:5]: 

    for col in row: 
        print("%10s"%col), 
