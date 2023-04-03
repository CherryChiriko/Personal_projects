
def powers_of_two():
    pow = []
    for n in range(1,1027):
        pow.append(2**n)
    return pow  

def solution(n):
    n = int(n)
    counter = 0; pow = powers_of_two()
    queue = [n]; temp = [counter]

    while n!= 1 :
        if not n % 2 : n//=2; counter += 1
        else :
            if n-1 in pow:  return counter + pow.index(n-1) + 2
            elif n+1 in pow : return counter + pow.index(n+1) + 2
            else :
                queue.append(n+1); queue.append(n-1); temp.append(counter+1); temp.append(counter+1)
                final_counter = []
                while queue :
                    if final_counter : 
                        minimum = min(final_counter)
                        #print("min ", minimum)
                    else : minimum = 10**309
                    n = queue.pop(0)
                    print("temp : ", temp)
                    print("queue : ", queue, n)
                    while n!= 1 :
                        #print("n : ", n)
                        if temp[0]> minimum : print("ah"); break
                        if n%2 :
                            if n-1 in pow:  
                                final_counter.append(temp.pop(0) + pow.index(n-1) + 2)                                
                                print(final_counter)
                                break
                            elif n+1 in pow :                       
                                final_counter.append(temp.pop(0) + pow.index(n+1) + 2)
                                print(final_counter)
                                break
                            else : 
                                queue.insert(0, n+1); queue.insert(1,n-1)
                                temp.insert(0,temp.pop(0)+1); temp.insert(1,temp[0])
                                print("q, t, ", queue, temp)
                                n = queue.pop(0)
                        n //= 2 ; temp[0] += 1
                print(final_counter) 
                #return minimum
                return min(final_counter)
    return counter


print("result : ", solution("69"))