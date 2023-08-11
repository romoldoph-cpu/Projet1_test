n = int(input("combien de note?"))
s = 0
for a in range (1,n +1):
    note = float(input("Note?"))
    s = s + note
print(s/n)
