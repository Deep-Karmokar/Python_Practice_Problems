restaurants = [ [ "Acme", "Italian", 2, 4, 3, 5],[ "Flintstone", "Steak", 5, 2, 4, 3, 3, 4],[ "Bella", "Troy", "Italian", 1, 4, 5] ]

for x in range(len(restaurants)):
  for value in restaurants[x]:
    if(value == "Italian"):
      for value_one in restaurants[x]:
        if(type(value_one) == int):
          if(value_one != 1 and value_one >= 5):
            print(restaurants[x][0])
            break