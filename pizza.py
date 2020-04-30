#I bought 100 dominos accounts and the formatting of the 
#document sucked so I did this to import it all into excel
#Pavel
#it could be done way cleaner but if it works it works
#please don't make fun of my pizza parser
f = open("pizza.txt", "r")
usr = []
pwd = []
pnt = []
pnd = []
#username
#password
#currentpoints
#pending points
for x in f:
	currentLineString = x
	username = currentLineString.split(":")
	usr.append(username[0])
	passwordandpoints = username[1].split(" ")
	pwd.append(passwordandpoints[0])
	pnt.append(passwordandpoints[5])
	pnd.append(passwordandpoints[10])
newfile = open("pizzafile.txt", "x")
newfile.write("~~UserNames~~\n")
for i in usr:
	newfile.write(i)
	newfile.write("\n")
newfile.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
newfile.write("~~Passwords~~\n")
newfile.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
for i in pwd:
	newfile.write(i)
	newfile.write("\n")
newfile.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
newfile.write("~~Points~~\n")
newfile.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
for i in pnt:
	newfile.write(i)
	newfile.write("\n")
newfile.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
newfile.write("~~PendingPoints~~\n")
newfile.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
for i in pnd:
	newfile.write(i)
f.close()
newfile.close()