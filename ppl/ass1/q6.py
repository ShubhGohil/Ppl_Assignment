import math

def get_factors_sum(n):  
    i = 1
    sum = 0
    while i <= math.sqrt(n): 
        if (n % i == 0) :  
            if (n / i == i) : 
                sum += i 
            else : 
                sum = sum + i + n/i 
        i = i + 1    
    return int(sum - n)

def get_amicable_pairs(n):
    map = {}
    pairs = []
    i = 2

    while(n > 0 ):
        map[i] = get_factors_sum(i)
        try:
            check = map[map[i]] == i
            if check and i != map[i]:
                pairs.append((i,map[i]))
                n += -1
        except KeyError:
            pass
        
        i += 1

    return pairs

print(get_amicable_pairs(10))
