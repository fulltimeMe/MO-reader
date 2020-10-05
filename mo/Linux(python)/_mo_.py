

""" User input """

s = input("Data:")
INfile = input("File:")
print("")

""" File to string """

file = open(INfile, 'r')
read = file.readlines()
file.close()

data = "".join(read)

count = 0
ok = 0

""" Serch the Word """

while ok < 1:
    index = data[count]
    count  += 1
    
    if index == s:
        one = count + 4
        ok = 1

count  += 4
stop = "false"        
liste = []

while stop == "false":
    index = data[count]
    liste.append(index)
    count  += 1
    if index == "$":
        stop = "true"
        
""" Outputs the Word """

output = "".join(liste)
print(output)
input("")




        
    