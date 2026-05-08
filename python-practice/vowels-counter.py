x=input("Enter the string: ").lower()
vowels = ["a","e","i","o","u"]
vow=[]

for char in x:
    if char in vowels:
        vow.append(char)
    else:
        continue

unique_vow = list(set(vow))

print(unique_vow)
j=len(unique_vow)
print("Number of vowels = ", j)
