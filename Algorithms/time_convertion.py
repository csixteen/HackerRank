time = input()
pm = time[-2:]
time = time[:-2].split(":")
if pm == "PM" and int(time[0]) < 12:
    hour = str(int(time[0]) + 12)
elif pm == "AM" and time[0] == "12":
    hour = "00"
else:
    hour = time[0]
print(":".join([hour] + time[1:]))
