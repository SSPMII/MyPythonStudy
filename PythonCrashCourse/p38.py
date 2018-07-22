# p38 列表习题
guests = ['strike','aegis','Duel','Buster','Freedom','Justice','unicorn']
for name in guests:
    print('I will invite {0} to have dinner'.format(name.title()))
print("\nUnfortunately, {0} won't come".format(guests[0].title()))
guests.append('Phoenix')
newguest = guests[-1]
print('We will have a new guest: {0}'.format(newguest))
print('\nI found a bigger table!')
guests.insert(0, 'popco')
guests.insert(3, 'pipimi')
guests.append('lala')
for name in guests:
    print('I will invite {0} to have dinner'.format(name.title()))
print("\nGod, the new table won't arrive in time!\nSorry, I can only have dinner with two guys.")
while len(guests) > 2:
    name = guests.pop()
    print('Sorry dear {0}, I cannot have dinner with you'.format(name.title()))
print()
for name in guests:
    print("Dear {0}, let's have dinner tonight".format(name.title()))
del guests[:]
print(guests)   