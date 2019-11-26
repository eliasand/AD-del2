import csv, random, string, subprocess, platform


fields = ['user'] 

rows = [ ['Nikhil'], 
         ['Sanchit'], 
         ['Aditya'], 
         ['Sagar'], 
         ['Prateek'], 
         ['Sahil']] 

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