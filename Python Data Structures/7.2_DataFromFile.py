# Write a program that prompts for a file name, 
# then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values 
# and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# when you are testing below enter mbox-short.txt as the file name.


fname = input("Enter file name: ")
fh = open(fname)

count = 0
rs = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        count += 1
        target_line = line.rstrip()
        pos = target_line.find("0")
        target_num = float(target_line[pos:])
        rs += target_num

Avg = rs/count        
 
print("Average spam confidence:",Avg)

