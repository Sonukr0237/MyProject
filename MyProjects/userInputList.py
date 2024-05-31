# Take 10 integer inputs from user and store them in a list and print them on screen.

var_list = []
for i in range(10):
    user_val = input(f"enter value for {i} index:" )
    var_list.append(user_val)

print("list : ",var_list)