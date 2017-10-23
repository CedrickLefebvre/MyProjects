def instructions():
	print('Enter a new item:')
	print("""
Type 'HELP' if you want this to be displayed.
Type 'DONE' if you have finished.
Type 'SHOW' to see your list.
""")

def show_list(x):
	print("Here's your list: ")
	for item in x:
		print(item)

def add_to_list(one_list, one_item):
	one_list.append(one_item)
	print('Added {}. The list has now {} items.'.format(one_item, len(one_list)))


shopping_list=list()
instructions()

while True:
	item = input('> ')
	if item == 'DONE':
		break
	elif item =='HELP':
		instructions()
		continue
	elif item=='SHOW':
		show_list(shopping_list)
		continue

	add_to_list(shopping_list, item)


show_list(shopping_list)
