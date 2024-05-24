a = {1: 10, 2: 20, 3: 30, 4: 40}
given_key = int(input("Enter the key to be searched: "))

if given_key in a:
    print(f"The key {given_key} exists in the dictionary.")
else:
    print(f"The key {given_key} does not exist in the dictionary.")