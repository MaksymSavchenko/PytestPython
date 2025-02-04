it = 4

while it > 1:
    if it != 3:
        print(it)
    it = it - 1

print('while execution is done')

t = 4

while t > 1:
    print(t)
    if t == 3:
        break
    t = t - 1

print("{} {}".format("Breaking the loop. t =", t))


print('_______________')
print('Continue loop. Skip 9, break on 3')

r = 11
while r > 1:
    if r == 9:
        r = r-1
        continue
    if r == 3:
        break
    print(r)
    r = r - 1

print("{} {}".format("Breaking the loop. r =", r))