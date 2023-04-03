# You got the bunny trainers to teach you a card game today, it's called Fizzbin. It's kind of pointless, but they seem to like it and it helps you pass the time while you work your way up to Commander Lambda's inner circle.
#
# At least all this time spent running errands all over Commander Lambda's space station have given you a really good understanding of the station's layout. You'll need that when you're finally ready to destroy the LAMBCHOP and rescue the bunny workers.
#
# Don't Get Volunteered!
# ======================
#
# As a henchman on Commander Lambda's space station, you're expected to be resourceful, smart, and a quick thinker. It's not easy building a doomsday device and ordering the bunnies around at the same time, after all! In order to make sure that everyone is sufficiently quick-witted, Commander Lambda has installed new flooring outside the henchman dormitories. It looks like a chessboard, and every morning and evening you have to solve a new movement puzzle in order to cross the floor. That would be fine if you got to be the rook or the queen, but instead, you have to be the knight. Worse, if you take too much time solving the puzzle, you get "volunteered" as a test subject for the LAMBCHOP doomsday device!
#
# To help yourself get to and from your bunk every day, write a function called solution(src, dest) which takes in two parameters: the source square, on which you start, and the destination square, which is where you need to land to solve the puzzle.  The function should return an integer representing the smallest number of moves it will take for you to travel from the source square to the destination square using a chess knight's moves (that is, two squares in any direction immediately followed by one square perpendicular to that direction, or vice versa, in an "L" shape).  Both the source and destination squares will be an integer between 0 and 63, inclusive, and are numbered like the example chessboard below:
#
# -------------------------
# | 0| 1| 2| 3| 4| 5| 6| 7|
# -------------------------
# | 8| 9|10|11|12|13|14|15|
# -------------------------
# |16|17|18|19|20|21|22|23|
# -------------------------
# |24|25|26|27|28|29|30|31|
# -------------------------
# |32|33|34|35|36|37|38|39|
# -------------------------
# |40|41|42|43|44|45|46|47|
# -------------------------
# |48|49|50|51|52|53|54|55|
# -------------------------
# |56|57|58|59|60|61|62|63|
# -------------------------
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
# solution.solution(0, 1)
# Output:
#     3
#
# Input:
# solution.solution(19, 36)
# Output:
#     1
#
# -- Java cases --
# Input:
# Solution.solution(19, 36)
# Output:
#     1
#
# Input:
# Solution.solution(0, 1)
# Output:
#     3

# def move_get (n):
#     x = n % 8 ; y = n // 8
#     #print("x, y : ", x, y)
#     move_set = []
#     dx = [2, 2, -2, -2, 1, 1, -1, -1]
#     dy = [1, -1, 1, -1, 2, -2, 2, -2]
#     for i in range(8):
#         #print("dx, dy : ", dx[i], dy[i])
#         x_n = x + dx[i]; y_n = y + dy[i]
#         if x_n < 8 and y_n < 8 and not x_n < 0 and not y_n < 0:
#             #print(x_n, y_n)
#             move_set.append(x_n + y_n*8)
#     move_set.sort()
#     return move_set
#
# def solution(src, dest) :
#     counter, level_counter = 0, 1
#     while src != dest :
#         visited, queue = [],[src]
#         while len(queue) > 0:
#             if queue[0] == str(queue[0]):
#                 counter = 0; level_counter += 1; queue.remove(queue[0])
#             src = queue.pop(0)
#             if src == dest : break
#             visited.append(src)
#             move_set = move_get(src)
#             for n in move_set :
#                 if n == dest :
#                     if "" in queue :
#                         while "" in queue:
#                             queue.remove(""); level_counter += 1
#                         break
#                     else : break
#                 elif n not in visited : queue.append(n)
#             if not counter :
#                 counter = 1; queue.append("")
#             print (counter)
#             print(queue)
#     return level_counter

def move_set(n):
    x = n % 8; y = n // 8                                   # conversion to 2D coords
    dx_ = [2, 2, -2, -2, 1, 1, -1, -1]
    dy_ = [1, -1, 1, -1, 2, -2, 2, -2]

    output = []
    for dx,dy in zip(dx_,dy_):
        x_n = x + dx; y_n = y + dy
        if (0 <= x_n < 8) and (0 <= y_n < 8):
            output.append(x_n + y_n * 8)                   # conversion back to 1D
    return output

def solution(src, dest) :
    if src == dest: return 0
    level = [None for _ in range(64)]; level[src] = 0      # initialization of branch level; source has level 0
    queue = [src]
    while queue:
        node = queue.pop(0)
        for n in move_set(node):                           # move_set returns the possible moves from the current position
            if level[n] is None:                           # means that this position has not been visited before
                queue.append(n)
                level[n] = level[node] + 1                 # level represents the branch level and also carries the information that the position has been visited
            if n == dest: return level[n]

print(solution(19,36))
