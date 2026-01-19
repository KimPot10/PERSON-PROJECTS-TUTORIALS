# Nested dictionary with duplicate
teachers = {
    "id1": {
        "name": "Sara",
        "class": "V",
        "subject_integration": ["english", "math", "science"]
    },
    "id2": {
        "name": "David",
        "class": "V",
        "subject_integration": ["english", "math", "science"]
    },
    "id3": {
        "name": "Sara",  
        "class": "V",
        "subject_integration": ["english", "math", "science"]
    },
    "id4": {
        "name": "Surya",
        "class": "V",
        "subject_integration": ["english", "math", "science"]
    }
}

print("BEFORE removing duplicates:")
for key, value in d1.items():
    print(key, ":", value)

# Removing duplicates using loop
new_dict = {}
seen = []

# check if may seen duplicate
for key, value in d1.items():
    if value not in seen:
        seen.append(value)
        new_dict[key] = value

print("\nRemoved duplicates:")
for key, value in new_dict.items():
    print(key, ":", value)