str = input("Please enter a word: ")
sub_str = input("Please enter your sub string: ")
count = 0
i = 0

while i <= len(str) - len(sub_str):
    if (str[i : i + len(sub_str)] == sub_str):
        count += 1   
    i += 1

print(f"The total number of times {sub_str} has occured: {count}")