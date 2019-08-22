amount = int(input("Enter Amount: "))
notes = [2000, 500, 100, 50, 20, 10]
change = []

while(amount>=0):
  if(amount-notes[0]>=0):
    amount = amount - notes[0]
    change.append(notes[0])

  elif(amount-notes[1]>=0):
    amount = amount - notes[1]
    change.append(notes[1])

  elif(amount-notes[2]>=0):
    amount = amount - notes[2]
    change.append(notes[2])

  elif(amount-notes[3]>=0):
    amount = amount - notes[3]
    change.append(notes[3])

  elif(amount-notes[4]>=0):
    amount = amount - notes[4]
    change.append(notes[4])

  elif(amount-notes[5]>=0):
    amount = amount - notes[5]
    change.append(notes[5])
  else:
    break

print(change)

for i in change:
  print(i, ":", change.count(i))
  change.remove(i)
