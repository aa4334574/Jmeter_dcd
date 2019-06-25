# n = 9
#
# for i in (range(1,n+1)):
#     for j in (range(1,n+1)):
#         if j<=i:
#             print('%d*%d=%d  '%(i,j,i*j),end='')
#     print('\n')

#
# l = [1,3,5,2,3,8]
#
#
# def maopao(l):
#     for i in range(len(l)):
#         for j in range(len(l)-i-1):
#             if l[j]>l[j+1]:
#                 l[j],l[j+1]=l[j+1],l[j]
#     return l
# print(maopao(l))

#
# l = 'hellw word'
#
# index = l.find('word',3,4)
# print(index)
import re
while 1:
    m = input('请输入字符串：')
    if m == 'end':
        break
    else:
        print(m.count(re.compile(m,'%d')))

#
#
# while 1:
#     num = 0
#     m = input('请输入字符串：')
#     if m == 'end':
#         print(num)
#         break
#     else:
#         for j in range(len(m)):
#             for i in range(10):
#                 if str(i) in m:
#                     num+=1
#         print(num)