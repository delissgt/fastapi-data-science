# SCRIPT THAT READS A FILE ON DISK
with open(__file__) as f:
    data = f.read()

# the program will block here until the date has benn read
print(data)