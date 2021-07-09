def zip_cars(cars, names):
	length = min(len(cars), len(cars))
	for i in range(length):
		yield(cars[i], names[i])

cars = ["A6","RAV4","Logan",]
names = ('Denys', 'Elizabeth', "Andrew")

for res in zip_cars(names, cars):
	print(res)
