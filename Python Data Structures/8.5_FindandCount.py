# Open the file mbox-short.txt and read it line by line. 
# When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line 
# (i.e. the entire address of the person who sent the message). 
# Then print out a count at the end.

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    line = line.rstrip()
    
    if line == "":
        continue
        
    if line.startswith("From"):
        mylist=line.split()
        # to filter out those lines start with "From:" which have length of 2
        if len(mylist) > 2:            
            count += 1
            print(mylist[1])

print("There were", count, "lines in the file with From as the first word")
