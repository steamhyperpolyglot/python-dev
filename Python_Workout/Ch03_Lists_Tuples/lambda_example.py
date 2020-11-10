def hello(name):
	return f'Hello, {name}'

def run_func_with_world(func):
	return func('world')

print(run_func_with_world(hello))