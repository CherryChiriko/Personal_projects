# Fuel Injection Perfection
# =========================
#
# Commander Lambda has asked for your help to refine the automatic quantum antimatter fuel injection system for the LAMBCHOP doomsday device. It's a great chance for you to get a closer look at the LAMBCHOP -- and maybe sneak in a bit of sabotage while you're at it -- so you took the job gladly.
#
# Quantum antimatter fuel comes in small pellets, which is convenient since the many moving parts of the LAMBCHOP each need to be fed fuel one pellet at a time. However, minions dump pellets in bulk into the fuel intake. You need to figure out the most efficient way to sort and shift the pellets down to a single pellet at a time.
#
# The fuel control mechanisms have three operations:
#
# 1) Add one fuel pellet
# 2) Remove one fuel pellet
# 3) Divide the entire group of fuel pellets by 2 (due to the destructive energy released when a quantum antimatter pellet is cut in half, the safety controls will only allow this to happen if there is an even number of pellets)
#
# Write a function called solution(n) which takes a positive integer as a string and returns the minimum number of operations needed to transform the number of pellets to 1. The fuel intake control panel can only display a number up to 309 digits long, so there won't ever be more pellets than you can express in that many digits.
#
# For example:
# solution(4) returns 2: 4 -> 2 -> 1
# solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1
# Quantum antimatter fuel comes in small pellets, which is convenient since the many moving parts of the LAMBCHOP each need to be fed fuel one pellet at a time. However, minions dump pellets in bulk into the fuel intake. You need to figure out the most efficient way to sort and shift the pellets down to a single pellet at a time.
#
# The fuel control mechanisms have three operations:
#
# 1) Add one fuel pellet
# 2) Remove one fuel pellet
# 3) Divide the entire group of fuel pellets by 2 (due to the destructive energy released when a quantum antimatter pellet is cut in half, the safety controls will only allow this to happen if there is an even number of pellets)
#
# Write a function called solution(n) which takes a positive integer as a string and returns the minimum number of operations needed to transform the number of pellets to 1. The fuel intake control panel can only display a number up to 309 digits long, so there won't ever be more pellets than you can express in that many digits.
#
# For example:
# solution(4) returns 2: 4 -> 2 -> 1
# solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1
#
# Languages
# =========
#
# To provide a Python solution, edit solution.py
# To provide a Java solution, edit Solution.java
#
# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.
#
# -- Python cases --
# Input:
# solution.solution('15')
# Output:
#     5
#
# Input:
# solution.solution('4')
# Output:
#     2
#
# -- Java cases --
# Input:
# Solution.solution('4')
# Output:
#     2
#
# Input:
# Solution.solution('15')
# Output:
#     5

def solution(n):
    pow = {2**n : n for n in range(1027)}
    queue = [int(n)]; counter = [0] 
    visited_numbers = set()

    while queue:
        n = queue.pop(0)
        c = counter.pop(0)

        if n == 1: return c

        if visited_numbers & set([n]): continue     # if we have already seen this number before, it doesn't need to be considered again, since it's not on an optimal path
        visited_numbers.add(n)
        c += 1

        if n % 2:                                               # n is odd
            if n-1 in pow: return c + pow[n-1]            # if n-1 is a power of 2, we know the counter instantly. Important that n-1 is before n+1 for the case n=3
            if n+1 in pow: return c + pow[n+1]
            queue.append(n+1); queue.append(n-1)
            counter.append(c)
        else:
            if n in pow: return pow[n]
            queue.append(n//2)                      # if the number can be divided by 2, always divide.
        counter.append(c)

# def solution(n):
#     numb = bin(int(n))[2:]; count = 0
#     while len(numb) > 1:
#         numb = numb[:-1] if (numb[-1] == "0") else bin(int(numb,2) + (1 if (numb[-2] == "1" and len(numb) > 2) else -1))[2:]
#         count += 1
#     return count


def test(n): print(f"result for {n} : ", solution(n))

test("1")
test("2")
test("3")
test("4")
test("15")
test("16")
test("69")
test(str(10**309-1))
# def powers_of_two():
#     pow = []
#     for n in range(1,1027):
#         pow.append(2**n)        #if len(str(2**n))>309 : print("n :", n); break
#     return pow

# def solution(n):
#     n = int(n)
#     counter = 0; pow = powers_of_two()
#     while n!= 1 :
#         if n%2 :
#             if n-1 in pow:  return counter + pow.index(n-1) + 2
#             elif n+1 in pow : return counter + pow.index(n+1) + 2
#             else : n -= 1
#             counter += 1
#         n //= 2; counter += 1
#     return counter

# # print(solution("4"))
# #print(solution("15"))
# print(solution(str(10**309 - 1)))           #  1278

# def solution(n):
#     n = int(n)
#     counter = 0; pow = powers_of_two()
#     queue = [n]; temp = [counter]

#     while n!= 1 :
#         if not n % 2 : n//=2; counter += 1
#         else :
#             if n-1 in pow:  return counter + pow.index(n-1) + 2
#             elif n+1 in pow : return counter + pow.index(n+1) + 2
#             else :
#                 queue.append(n+1); queue.append(n-1); temp.append(counter+1); temp.append(counter+1)
#                 final_counter = []
#                 while queue :
#                     if final_counter : 
#                         minimum = min(final_counter)
#                         #print("min ", minimum)
#                     else : minimum = 10**309
#                     n = queue.pop(0)
#                     print("temp : ", temp)
#                     print("queue : ", queue, n)
#                     while n!= 1 :
#                         #print("n : ", n)
#                         if temp[0]> minimum : print("ah"); break
#                         if n%2 :
#                             if n-1 in pow:  
#                                 final_counter.append(temp.pop(0) + pow.index(n-1) + 2)                                
#                                 print(final_counter)
#                                 break
#                             elif n+1 in pow :                       
#                                 final_counter.append(temp.pop(0) + pow.index(n+1) + 2)
#                                 print(final_counter)
#                                 break
#                             else : 
#                                 queue.insert(0, n+1); queue.insert(1,n-1)
#                                 temp.insert(0,temp.pop(0)+1); temp.insert(1,temp[0])
#                                 print("q, t, ", queue, temp)
#                                 n = queue.pop(0)
#                         n //= 2 ; temp[0] += 1
#                 print(final_counter) 
#                 #return minimum
#                 return min(final_counter)
#     return counter
