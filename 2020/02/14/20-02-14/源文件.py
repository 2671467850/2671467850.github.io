# # 水仙花数
# for num in range(100, 1000):
#     # 3=153%10===>> % 取余
#     one = num % 10
#     # 5=153//10%10===>> // 整除
#     two = num // 10 % 10
#     # 1=153//100
#     high = num // 100
#     # 判断输出水仙数
#     if num == one ** 3 + two ** 3 + high ** 3:
#         print(num)


# # 百钱百鸡
# for x in range(0, 20):
#     for y in range(0, 33):
#         z = 100 - x - y
#         if x*5 + y*3 + z/3 == 100:
#             print("公鸡:[%d] 母鸡:[%d] 小鸡:[%d]" % (x, y, z))


# # CRAPS赌博游戏
# from random import randint
#
# # 设置赌注
# money = 1000
#
# while money > 0:
#     print("您的赌注为: %d" % money)
#
#     # 游戏进行下一局的设置
#     game_go = False
#     # 赌注>0时游戏循环进行
#     while True:
#         dz = int(input("请下注: "))
#         if 0 < dz <= money:
#             break
#     # 第一局的点数
#     first = randint(1, 6) + randint(1, 6)
#     print("第 1 局点数为:[%d]" % first)
#     if first == 7 or first == 11:
#         print("您赢了!")
#         money += dz
#     elif first == 2 or first == 3 or first == 12:
#         print("庄家赢!")
#         money -= dz
#     else:
#         game_go = True
#         times = 2
#
#     while game_go:
#         game_go = False
#         second = randint(1, 6) + randint(1, 6)
#         print("第 %s 局点数为:[%d]" % (times, second))
#         if second == 7:
#             print("庄家赢!")
#             money -= dz
#         elif second == first:
#             print("您赢了!")
#             money += dz
#         else:
#             game_go = True
#             times += 1
#
# print("您输光了所有赌注,游戏结束!")


# # 确定一个正整数的所有因子
# n = int(input("输入一个正整数: "))
# results = []
# for i in range(1, n+1):
#     if n % i == 0:
#         results.append(i)
# print(results)


# # 斐波那契数列
# a = 0
# b = 1
# results = []
# for i in range(1, 11):
#     results.append(a)
#     c = a + b
#     a = b
#     b = c
# print(results)













