mapa = [0,1,0,2,1,0,1,3,2,1,2,1]

count = 0

for key, value in enumerate(mapa):

    if key == 0 or key == 1:
        pass
    else:
        prev = mapa[key - 1]

        if value > prev:

            count += (value - prev)
    

print(count)