import random

#result = dir(random)
#result = help(random)

#result = random.random()
#result = random.random() * 5 

#result = random.uniform()
#result = random.uniform(5,100)
#result = random.uniform(5,10)
#result = int(random.uniform(5,10))
#result = float(random.uniform(5,10))

names = ["ali","yağmur","deniz","cenk"]
result = names[random.randint(0,len(names)-1)]





print(result)