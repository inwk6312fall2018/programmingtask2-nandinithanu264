
import string
#open the file
myfile = open("Crime.csv")
#initializations
mylist_intname=[]
count_list=[0,0,0,0,0]
id_list=[1430,1610,2142,2135,2120]
crime_type=['ASSAULT','ROBBERY','FROM','OF','BREAK']
#read the file
for line in myfile:
 line=line.strip()
 line=line.split()
 a=str(line)
 #put it in a list for easier manipulation
 b=a[79:]
 mylist_intname.append(b)
#print(ord('1'))
 #read the list and check for necessary values
for i in range(len(mylist_intname)):
    #print (mylist_intname[i])
    if (crime_type[0] in mylist_intname[i]):
        count_list[0]=count_list[0]+1
    if (crime_type[1] in mylist_intname[i]):
        count_list[1]=count_list[1]+1
    if (crime_type[2] in mylist_intname[i]):
        count_list[2]=count_list[2]+1
    if (crime_type[3] in mylist_intname[i]):
        count_list[3]=count_list[3]+1
    if (crime_type[4] in mylist_intname[i]):
        count_list[4]=count_list[4]+1
#print output
print ("CRIME TYPE   ID   COUNT ")
for i in range(5):
    print(str(crime_type[i])+ "    "  +str(id_list[i])+ "    " +str(count_list[i]))
