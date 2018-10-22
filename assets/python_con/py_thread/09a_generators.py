
def generator(target):
    current = 0
    while current < target:
        print('Generator Loop')
        yield current
        current += 1

for i in generator(5):
    print('Main loop with {0}.'.format(i))

# g = generator(1)
# next(g)
# next(g)
