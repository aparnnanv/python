#create new file
'''f=open("D://STUDENTS//aparnna//FILE1.txt",'x')
f.write()
f.close()'''

f=open("D://STUDENTS//aparnna//FILE1.txt",'w')
f.write("good morning")
f.close()
 
#append mode in file
f=open("D://STUDENTS//aparnna//FILE1.txt",'a')
f.write("\nhave a nice day!")
f.close()

#read from a file
f=open("D://STUDENTS//aparnna//FILE1.txt",'r')
print(f.read())
f.close()
