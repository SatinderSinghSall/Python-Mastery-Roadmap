# Dictionary in Python: Key & Value Pair

info = {
    "name": "Satinder Singh Sall",
    "age": 22,
    "subjects": ["Math", "English"],
    "CGPA": 6.9
}

print(info)
print(type(info))
print(info["name"])

info["CGPA"] = 10
print(info)

# Dictionary Method:
print(info.keys())
print(info.values())
print(info.items())
print(info.get("CGPA"))
print(info.update({"CGPA": 5}))
