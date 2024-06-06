sampleDictionary = {
    'name': 'John',
    'age': 30,
    'city': 'New York',
    'country': 'USA'
}

print("Iterating over Keys: ")
for key in sampleDictionary:
    print(key)

print("Iterating over Values :")
for value in sampleDictionary.values():
    print(value)

print("\n Iterating over key-values pairs:")
for key, value in sampleDictionary.items():
    print(f"{key}:{value}")


print("\n Iterating over keys and accessing corresponding values:")
for key in sampleDictionary:
    print(f"{key}: {sampleDictionary[key]}")