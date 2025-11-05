marks={
    "Nami": 100,
    "Rahi":57,
    "Salman":85,
    "list":[4,5,7],
    0:"Sure"
}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Nami":99, "Sam":100})
print(marks)
print(marks.get("Nami"))
print(marks["Nami"])
# differences
# print(marks.get("Nami2"))# print none
# print(marks["Nami2"])# returns an error
