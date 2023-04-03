def solution(n):
    numb = bin(int(n))[2:]; count = 0
    while len(numb) > 1:
        numb = numb[:-1] if (numb[-1] == "0") else bin(int(numb,2) + (1 if (numb[-2] == "1" and len(numb) > 2) else -1))[2:]
        count += 1
    return count



def test(n): print(f"result for {n} : ", solution(n))

test("1")
test("2")
test("3")
test("4")
test("15")
test("16")
test("69")
test(str(10**309-1))