# define a string
my_string = "Hello, world!"

# capitalize()
print(my_string.capitalize())  # "Hello, world!"

# casefold()
print(my_string.casefold())  # "hello, world!"

# center()
print(my_string.center(20, "*"))  # "***Hello, world!***"

# count()
print(my_string.count("o"))  # 2

# endswith()
print(my_string.endswith("!"))  # True

# find()
print(my_string.find("world"))  # 7

# index()
print(my_string.index("world"))  # 7

# isalnum()
print(my_string.isalnum())  # False

# isalpha()
print(my_string.isalpha())  # False

# isdecimal()
print(my_string.isdecimal())  # False

# isdigit()
print(my_string.isdigit())  # False

# isidentifier()
print(my_string.isidentifier())  # False

# islower()
print(my_string.islower())  # False

# isnumeric()
print(my_string.isnumeric())  # False

# isprintable()
print(my_string.isprintable())  # True

# isspace()
print(my_string.isspace())  # False

# istitle()
print(my_string.istitle())  # True

# isupper()
print(my_string.isupper())  # False

# join()
my_list = ["Hello", "world"]
print("-".join(my_list))  # "Hello-world"

# ljust()
print(my_string.ljust(20, "*"))  # "Hello, world!*******"

# lower()
print(my_string.lower())  # "hello, world!"

# lstrip()
print(my_string.lstrip("H"))  # "ello, world!"

# partition()
print(my_string.partition(","))  # ("Hello", ",", " world!")

# replace()
print(my_string.replace("world", "Python"))  # "Hello, Python!"

# rfind()
print(my_string.rfind("o"))  # 8

# rindex()
print(my_string.rindex("o"))  # 8

# rjust()
print(my_string.rjust(20, "*"))  # "*******Hello, world!"

# rpartition()
print(my_string.rpartition(","))  # ("Hello, world", ",", "")

# rsplit()
print(my_string.rsplit(","))  # ["Hello", " world!"]

# rstrip()
print(my_string.rstrip("!"))  # "Hello, world"

# split()
print(my_string.split(","))  # ["Hello", " world!"]

# splitlines()
multi_line_string = "Hello\nworld"
print(multi_line_string.splitlines())  # ["Hello", "world"]

# startswith()
print(my_string.startswith("Hello"))  # True

# strip()
print(my_string.strip("H!"))  # "ello, world"

# swapcase()
print(my_string.swapcase())  # "hELLO, WORLD!"

# title()
print(my_string.title())  # "Hello, World!"

# translate()
my_translation_table = my_string.maketrans("H", "J")
print(my_string.translate(my_translation_table))  # "Jello, world!"

# upper()
print(my_string.upper())  # "HELLO, WORLD!"

# zfill()
print(my_string.zfill(20))  # "0000Hello, world!"
