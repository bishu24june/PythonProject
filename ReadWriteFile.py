'''Created on Mar 14, 2020 @author: Bishwa '''

print("File Writing Started")
writeFile = open("C:/Personal/fileData.txt","a");
writeFile.write("\nThis is my first file data");
print ("Writing Completed")

print ("\n Reading file data")

readFile = open("C:/Personal/fileData.txt","r")
print (readFile.read())

