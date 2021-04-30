"""
一百块钱买一百只鸡，公鸡5块，母鸡3块，小鸡1/3块
Author Fyb
"""
gj, mj, xj = 5, 3, 1/3
for x in range(1, 100//5):
    for y in range(1, 100//3):
        for z in range(1, 100):
            if gj * x + mj * y + xj * z == 100 and x + y + z == 100:
                print(x, y, x)
