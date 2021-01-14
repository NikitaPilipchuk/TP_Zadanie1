import random as r

def get_fraction(x):
    if x >= 0:
        result = x - int(x)
    else:
        result = (x - int(x))*-1

    return result

numb_list = []
for _ in range(10):
    numb_list.append(r.uniform(-100,100))

print(sorted(numb_list, key=lambda x: get_fraction(x)))


