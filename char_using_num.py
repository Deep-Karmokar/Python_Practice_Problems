dictionary = {2: ["a", "b", "c"], 3: ["d", "e", "f"], 4: ["g", "h", "i"], 5: ["j", "k", "l"], 6: 
["m", "n", "o"], 7: ["p", "q", "r", "s"], 8: ["t", "u", "v"], 9: ["w", "x", "y", "z"]}

string = input("Enter series of number: ")
# 9999335533 
output = ""
for i in range(len(string)):
  for key in string: 
    value = string.count(key) - 1
    output += dictionary[int(key)][value]
    break

print(output)