from main import *
c = dl("https://www.instagram.com/p/Cf08NZ-BGnH/?igshid=YmMyMTA2M2Y=")
x = len(c)
#print(c[2])
for i in range(x):
    print(f"link ke {i} : {c[i]}")
