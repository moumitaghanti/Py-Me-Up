import os
import re

filename = os.path.join( "paragraph_2.txt")
# opening the text file and reading it 
with open(filename, 'r') as file:
    file_contents = file.read()
    # finding the special character in the paragraph
    p = re.compile('["?","!","(",")","=",">","+","."]')
    # finding the letter/ character{A-Z, a-z, 0-9,-} in the paragraph
    ty = re.compile('\w') 
    # counting  the letter/ character{A-Z, a-z, 0-9,-} in the paragraph and special characters which results total number of letters
    tot1 = (float(len(ty.findall(file_contents))))
    tot= (float(tot1+(len(p.findall(file_contents)))))
    print(file_contents)
    # counting  the ending punctiation marks
    st= float((file_contents.count("?"))+ (file_contents.count("!")))
    #Printing the analysis
    print("Paragraph Analysis")
    print("-----------------")
    print("Approximate Word Count:   "+ str(len(file_contents.split())+1))
    print("Approximate Sentence Count:   "+ str((file_contents.count(".")) + st))
    print("Average Letter Count:  "+ str(float(tot/len(file_contents.split()))))
    print("Average Sentence Length:  "+ str(float(len(file_contents.split())+1)/file_contents.count(".")))