
def add(*args):
	print(args) 
	print(sum(args))


l = [1, 2, 3]
add(*l)

def ad(**kwargs):
	print(kwargs)

ad(street='lenina', house=12)

# args со звездочкой нужен для упаковки n количества аргументов в кортеж, kwargs
# c двумя нужен для упаковки именованных аргументов в кортеж