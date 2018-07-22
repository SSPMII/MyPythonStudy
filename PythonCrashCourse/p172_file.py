# 讲用户的名字写入guest.txt中
file_name = 'guest_book.txt'
guest_active = True

while guest_active:
	with open(file_name, 'a') as guests:
		name = input('Please enter your name, q to quit')
		if name != 'q':
			guests.write(name + '\n')
		else:
			guest_active = False
