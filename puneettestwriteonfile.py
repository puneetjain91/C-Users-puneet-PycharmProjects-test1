print("This the python program for writing data on exiting file" )
print("We are opening test file for writing")
f=open("test.txt","w")
print("File Name is :",f.name)
print("File Mode is :",f.mode)
print("Is file Readable:",f.readable())
print("Is the Fle Wriable:",f.writable())
list=["Puneet\n","sector 47 Noida\n","i m working in wipro technologies \n"]
f.writelines(list)
print("Writes lines in file successfully")
print("Is the file is closed:",f.closed)
f.close()
print("Is the file is closed:",f.closed)
f=open("test.txt","r")
data=f.read()
print(data)
f.close()