
st = {100, 200, 300, 400}
l2 = list(st)
tmp = l2[0]
l2[0] = l2[1]
l2[1] = tmp
st2 = set(l2)
print("Q5 Set:", st2)
