import re,requests

req = requests.request("GET","https://trackerslist.com/all_aria2.txt")
#print(req.text)

f = open("./aria2.conf","r")
#print(f.read())
#print(re.search("\nbt-tracker=.*",f.read()).span())
result = re.sub(r'\nbt-tracker=.*',"\nbt-tracker="+req.text,f.read())
print(result)
f.close()

print("Proceed to replace?")
i = input()
if i=="y" or i=="yes":
    pass
else:
    print("Abort.")
    exit()

f = open("./aria2.conf","w+")
f.write(result)
print("Successfully updated trackers.")
f.close()
