s = input()
s = s.lower().replace(" ", "")
letters = set(s)
if len(letters) == 26:
    print("pangram")
else:
    print("not pangram")
