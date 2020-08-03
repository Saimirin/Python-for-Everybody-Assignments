# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, 
# sorted by hour as shown below:
# 04 3
# 06 1
# 07 1
# 09 2
# ....


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

dict = {}

for line in handle:
    line = line.strip()
    if line == "": continue
    if line.startswith("From"):
        wordlist = line.split()
        # filter out the lines starts with "From:" which has length of 2
        if len(wordlist) > 2:
            # locate the index of time
            time = wordlist[5]
            # slice the hour from the time
            hour = time[:2]
            # .get() for create (if not exist) or update (if alrady exist) key and value    
            dict[hour] = dict.get(hour,0)+1

hour_list = sorted((h,c) for h,c in dict.items())
            
# The hour_list would be a list of tuples, use for loop iterate each item and print the values.
for i in hour_list:
    x,y=i
    print (x,y)