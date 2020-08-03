# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dict = {}

for line in handle:
    line = line.strip()
    if line == "": continue
    if line.startswith("From"):
        wordlist = line.split()
        if len(wordlist) > 2:
            key = wordlist[1]
            # .get() for create (if not exist) or update (if alrady exist) key and value            
            dict[key] = dict.get(key,0)+1

count = None
email = None

for e,c in dict.items():
    if count == None or c > count:
        count = c
        email = e
print(email,count)    