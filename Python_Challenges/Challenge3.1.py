# Find the Access Codes
# =====================
#
# In order to destroy Commander Lambda's LAMBCHOP doomsday device, you'll need access to it. But the only door leading to the LAMBCHOP chamber is secured with a unique lock system whose number of passcodes changes daily. Commander Lambda gets a report every day that includes the locks' access codes, but only the Commander knows how to figure out which of several lists contains the access codes. You need to find a way to determine which list contains the access codes once you're ready to go in.
#
# Fortunately, now that you're Commander Lambda's personal assistant, Lambda has confided to you that all the access codes are "lucky triples" in order to make it easier to find them in the lists. A "lucky triple" is a tuple (x, y, z) where x divides y and y divides z, such as (1, 2, 4). With that information, you can figure out which list contains the number of access codes that matches the number of locks on the door when you're ready to go in (for example, if there's 5 passcodes, you'd need to find a list with 5 "lucky triple" access codes).
#
# Write a function solution(l) that takes a list of positive integers l and counts the number of "lucky triples" of (li, lj, lk) where the list indices meet the requirement i < j < k.  The length of l is between 2 and 2000 inclusive.  The elements of l are between 1 and 999999 inclusive.  The solution fits within a signed 32-bit integer. Some of the lists are purposely generated without any access codes to throw off spies, so if no triples are found, return 0.
#
# For example, [1, 2, 3, 4, 5, 6] has the triples: [1, 2, 4], [1, 2, 6], [1, 3, 6], making the solution 3 total.
#
# Languages
# =========
#
# To provide a Java solution, edit Solution.java
# To provide a Python solution, edit solution.py
#
# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.
#
# -- Java cases --
# Input:
# Solution.solution([1, 1, 1])
# Output:
#     1
#
# Input:
# Solution.solution([1, 2, 3, 4, 5, 6])
# Output:
#     3
#
# -- Python cases --
# Input:
# solution.solution([1, 2, 3, 4, 5, 6])
# Output:
#     3
#
# Input:
# solution.solution([1, 1, 1])
# Output:
#     1
# import time
# def find_divisors(n, n_f):
#     divisors = []
#     for i in range(1, n_f + 1):
#         if n % i == 0: divisors.append(i)
#     return divisors
#
# def solution(l):
#     start_time = time.time()
#     lucky_triple = 0; lst = list(l)
#     while len(lst) > 2:
#         z = lst.pop(-1)
#         divz = find_divisors(z, z)
#         if not divz : continue
#         for y in divz:
#             if y in lst :
#                 i = len(lst) - 1 - lst[::-1].index(y)
#                 lst_y = lst[:i]
#                 if not lst_y : continue
#                 max_ = max(lst_y)
#                 print(lst, lst_y, max_)
#                 divy = find_divisors(y, max_)
#                 for x in divy :
#                     if x in lst_y : lucky_triple +=1
#
#     end_time = time.time()
#     print("Total time :", end_time-start_time)
#     return lucky_triple


#print(solution([1,1,1]))
#print(solution([1,2,3,4,5,6]))




# def find_divisors(n):
#     divisors = []
#     for i in range(1, n + 1):
#         if n % i == 0: divisors.append(i)
#     return divisors
#
# def solution(l):
#     lucky_triple = 0; lst = list(l)
#     while len(lst) > 2:
#         z = lst.pop(-1)
#         divz = find_divisors(z)
#         if not divz : continue
#         for y in divz:
#             if y in lst :
#                 lst_y = lst[:y]
#                 divy = find_divisors(y)
#                 for x in divy :
#                     if x in lst_y :
#                         lucky_triple += 1
#     return lucky_triple
# Time for test 1 : 0.18311142921447754



# Second version time 0.12003350257873535


# def find_divisors(n, n_f):
#     divisors = []
#     for i in range(1, n_f + 1):
#         if n % i == 0: divisors.append(i)
#     return divisors
#
# def solution(l):
#   lucky_triple = 0; lst = list(l)
#   while len(lst) > 2:
#     z = lst.pop(-1)
#     divz = find_divisors(z, z)
#     if not divz : continue
#     for y in divz:
#         if y in lst :
#             lst.sort()
#             lst_y = lst[:y-1]
#             if len(lst_y) < 2 : continue
#             divy = find_divisors(y, lst_y[-1])
#             for x in divy :
#                 if x in lst_y : lucky_triple +=1
#     return lucky_triple


# def solution(l):
#     start_time = time.time()
#     lucky_triple = 0; lst = list(l)
#     while len(lst) > 2:
#         lst.sort(reverse = True)
#         z = lst.pop(0)
#         divz = find_divisors(z, z)
#         if not divz : continue
#         for y in divz:
#             if y in lst :
#                 lst.sort()
#                 lst_y = lst[y+1:]
#                 print(lst, lst_y)
#                 if not lst_y : continue
#                 divy = find_divisors(y, lst_y[0])
#                 for x in divy :
#                     if x in lst_y : lucky_triple +=1
#
#     end_time = time.time()
#     print("Total time :", end_time-start_time)
    # return lucky_triple

# def solution(l):
#     lucky_triples = set(); lst = l[::-1
#     # while len(lst) > 2:
#     for i,z in enumerate(lst[:-2]):
#
#         # z = lst.pop()
#         for j,y in enumerate(lst[i:-1]):
#             if z % y == 0 :
#                 for x in lst[j:]:
#                     if y % x == 0:
#                         lucky_triples.add((x,y,z))
#     return len(lucky_triples)
#[1,2,3,4,5,6]

def solution(l):
    lucky_triples =  0
    n_of_divisors = [0 for _ in l]                  # this stores the number of divisors found for each member of the list
    for i,z in enumerate(l):
        for j,y in enumerate(l[:i]):
            if not z % y:                           # y is a divisor of z
                lucky_triples += n_of_divisors[j]   # lucky triples can be build using the template (_,y,z),
                n_of_divisors[i] += 1               # where _ would be replaced by each divisor x of y
    return lucky_triples

# def solution(l):
#     lucky_triples = set(); counter = [[] for _ in range(l)]
#     for i, y in enumerate(l):
#         if not y % l[i] : counter[]
#         # z = lst.pop()
#     #     for j,y in enumerate(lst[i:-1]):
#     #         if z % y == 0 :
#     #             for x in lst[j:]:
#     #                 if y % x == 0:
#     #                     lucky_triples.add((x,y,z))
#     # return len(lucky_triples)
#
import time
print(solution([1,1,1]))
print("---------")
print(solution([1,2,3,4,5,6]))
print("---------")
start = time.time()
print(solution([2,3,4,6,7,8,9,10]*40 + list(range(99999 - 1500, 99999))))
print(solution([2,3]*40 + list(range(999999 - 2000, 999999))))
print("elapsed:", time.time()-start)


# def solution(l):
#     lucky_triples = 0
#
#     n_of_divisors = [0 for _ in l]
#
#
#     for i,x in enumerate(l):
#
#         for j in range(i):
#             if not x % l[j]:
#                 lucky_triples += n_of_divisors[j]
#                 n_of_divisors[i] += 1
#                 # print(n_of_divisors)
#     return lucky_triples


# respaldo 3
# def solution(l):
#     lucky_triples = set(); lst = l
#     while len(lst) > 2:
#         z = lst.pop(-1)
#         for i,y in enumerate(lst):
#             if z % y == 0 :
#                 lst_y = lst[:i]
#                 for x in lst_y:
#                     if y % x == 0:
#                         lucky_triples.add((x,y,z))
#     return len(lucky_triples)


# def solution(l):
#     lucky_triples = set(); lst = l
#     while len(lst) > 2:
#         z = lst.pop(-1)
#         for y in lst :
#             if z % y == 0 :
#                 i = len(lst) - 1 - lst[::-1].index(y)
#                 lst_y = lst[:i]
#                 for x in lst_y:
#                     if y % x == 0:
#                         lucky_triples.add((x,y,z))
#     return len(lucky_triples)

#
# respaldo 2
# def solution(l):
#     lucky_triples = set(); lst = l
#     while len(lst) > 2:
#         z = lst.pop(-1)
#         magia_de_gato = lst[::-1]
#         for y in magia_de_gato :
#             if z % y == 0 :
#                 # print(y)
#                 i = len(lst) - 1 - magia_de_gato.index(y)
#                 lst_y = lst[:i]
#                 for x in lst_y:
#                     if y % x == 0:
#                         # print((x,y,z), lst, lst_y)
#                         lucky_triples.add((x,y,z))
#     # print(*lucky_triples, sep = "\n")
#     return len(lucky_triples)
