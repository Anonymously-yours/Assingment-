
# library to manupulate csv files.
import csv

# To get the name of the input file and open it.
print("Enter the input file name")
file =input()
#file="input1.csv"

fields=[]
rows=[]

with open(file,'r') as csvfile:
    csvr=csv.reader(csvfile)
    fields=next(csvr)

    for row in csvr:
        rows.append(row)


# l is used to later calculate number of tests.
l=len(fields)-3


# These are the fields in output file.
fields2=["Name","Username","Chapter Tag","Test_Name","answered","correct","score","skipped","time-taken","wrong"]
rows2=[]

# creating data to be later inserted in csv file.
for row in rows:
    #print(row)
    name=row[0]
    id=row[1]
    ch=row[2]
    li=[name,id,ch]
    for i in range((l//6)):
        
        tn=row[i*6+3].strip("-score")
        ans=row[i*6+5]
        # if the parameter is empty the row will not be inserted in the output file.
        if ans=="-":
            continue
        cor=row[i*6+6]
        sco=row[i*6+3]
        skip=row[i*6+8]
        time=row[i*6+4]
        wro=row[i*6+7]
        rows2.append(list(li+[tn,ans,cor,sco,skip,time,wro]))
    


# Finally creating the output file and writing data into it.
with open("output.csv",'w') as csvfile:
    csvw=csv.writer(csvfile)
    csvw.writerow(fields2)
    csvw.writerows(rows2)
    
