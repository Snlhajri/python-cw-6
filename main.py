# write your code here
person = {
    "name":"somaya",
    "age":18,
    "hoppies":["drawing","reading","swimming"]
}

print(person["name"])
print(person["age"])

person["age"]=17
person["country"]="kuwait"
print(len(person))
person["hoppies"].append("cooking")
def check_hobbies(person):
    if len(person["hoppies"])> 3:
       print("wow you are amaz")
    else:
       print("you are not amaz")
check_hobbies(person)


