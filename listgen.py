jack = {
	'name': 'john',
	'car':'bmw'
}

john = {
	'name':'john',
	'car':'audi'
	}

users = [jack, john]

cars = [person['car'] for person in users] # сокращенная запись 
print(cars)

cars = []
for person in users:
	cars.append(person['car'])

print(cars)

new_cars = [person.get('car', '') for person in users]
print(new_cars) # исключение, если не будет ключа


# фильтрация

names = ['jack', 'john', 'oleg', 'ula']

new_names = [n for n in names if n.startswith('j')]
print(new_names)
