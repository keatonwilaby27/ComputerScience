import random

r = random.randrange(0,10)
# 0 is inclusive and the 10 is exclusive< doesnt print 10
print(r)

p = random.random()
if p < 0.25:
    print("success")
else:
    print("Fail")
