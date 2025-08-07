input = str(input())
input = input.upper()
alphabet = dict()
for l in input:
    if l in alphabet:
        alphabet[l] += 1
    else:
        alphabet[l] = 1
max_count = max(alphabet.values())
max_keys = [k for k, v in alphabet.items() if v == max_count]
if len(max_keys) > 1:
    print("?")  
else:
    print(max_keys[0]) 