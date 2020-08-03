# Write code using find() and string slicing to extract the number at the end of the line below. 
# Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475";

# find the index position of "0"
pos=text.find("0")
# slice from "0" to all the way the end of the string
num = float(text[pos:])

print(num)