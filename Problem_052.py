candidate = 1
done = False

while not done:
    for i in range(6, 1, -1):
        if sorted(str(i * candidate)) != sorted(str(candidate)):
            break
    else:
        print (candidate)
        done = True

    candidate += 1
