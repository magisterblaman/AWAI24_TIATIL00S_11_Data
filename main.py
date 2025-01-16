import json

f = open("person.json", encoding="utf-8")
content = f.read()

my_dict = json.loads(content)

# date_dict = {
#     "year": 2012,
#     "month": 1,
#     "day": 9
# }

print("Name: " + my_dict["name"])
print("Age: " + str(my_dict["age"]))
print("Birth year: " + str(my_dict["birth_date"]["year"]))
print("Hair color: " + my_dict["hair_color"])
if my_dict["is_citizen"] == True:
    print("Is a Swedish citizen")
else:
    print("Is NOT a Swedish citizen")

print("Favorite foods:")
for i in range(len(my_dict["favorite_foods"])):
    print(" - " + my_dict["favorite_foods"][i])

print("Pets:")
for i in range(len(my_dict["pets"])):
    print(" - " + my_dict["pets"][i]["name"] + " (" +
          str(my_dict["pets"][i]["age"]) + ")")
# my_dict["pets"][2]["name"]


# print(" - " + my_dict["favorite_foods"][0])
# print(" - " + my_dict["favorite_foods"][1])
# print(" - " + my_dict["favorite_foods"][2])
