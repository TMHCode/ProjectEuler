import math
def Print_Answer(problem):
    print(problem)


def problem_1():
    sum = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

def problem_2():
    sequenz = [1, 2]
    max_number_size =4000000
    index = 0
    sum = 2
    while sequenz[len(sequenz)-1] <= max_number_size:
        sequenz.append((sequenz[index]+sequenz[index+1]))
        if sequenz[index+2] % 2 == 0:
            sum += sequenz[index+2]
        index += 1
    return sum

def Is_Prime(number):
    if number == 1:
        return False
    i = 2
    while i*i <= number:
        if number % i == 0:
            return False
        i += 1
    return True
    """
    for i in range(2, number-1):
        if number % i != 0:
            continue
        return False
    return True 
    """
def problem_3():
    number = 600851475143
    prime_factors = []
    # fill an array with all the primenumbers, the number contains
    for i in range(2, number):
        if Is_Prime(i):
            # find divisor
            if number % i == 0:
                prime_factors.append(i)
                #print(prime_factors)
                # check if primefactors result in input number
                result = 1
                for i in range(len(prime_factors)):
                    result *= prime_factors[i]
                if result == number:
                    return max(prime_factors)

    return False
    """
    k = 1
    x = 600851475143
    while k < x:
         k += 1
         while x % k == 0:
             x = x // k
    return k
    """

def problem_4():
    def Is_Palin(num):
        number = str(num)
        for i in range(math.floor(len(number)/2)):
            if number[i] != number[len(number)-i-1]:
                return False
        if len(number)<2:
            return False
        else:
            return True
    largest_pal = 0; li = 0; lj = 0
    for i in reversed(range(1000)):
        for j in reversed(range(1000)):
            res = i * j
            if Is_Palin(res) and res > largest_pal:
                largest_pal = res
                li = i
                lj = j
    return str(str(li) + ' * ' + str(lj) + ' = ' +str(largest_pal))

def problem_5():
    div_range = 20
    i = 11
    while True:
        count = 0
        for j in reversed(range(1,div_range+1)):
            if i % j == 0:
                count += 1
                continue
            else:
                break
        if count == div_range:
            return i
        i += j+1

def problem_6():
    sqsum = 0
    sumsq = 0
    for i in range(1, 101):
        sumsq += i
        sqsum += i**2
    sumsq **= 2
    div = sumsq - sqsum
    return div

def problem_7():
    primes = []
    i = 2
    while True:
        if Is_Prime(i):
            primes.append(i)
        if len(primes) == 10001:
            break
        i += 1
    return primes[-1]

def problem_8():
    number = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
    number = str(number)
    biggest = 0
    for i in range(0,len(str(number))-12):
        res = 1
        for j in range(13):
            res *= int(number[i+j]) 
        if res > biggest:
            biggest = res
        print(biggest)
    pass

def problem_9():
    for a in range(1, 1000):
        for b in range(1, 1000):
            c = 1000 - (a+b)
            if a**2 + b**2 == c**2:
                #print('a: ' + str(a) + ' b: ' + str(b) + ' c: ' + str(c))
                #print(a**2, b**2, c**2, a**2+b**2)
                return (a*b*c)
    pass

def problem_10():
    sum = 0
    for i in range(1, 2000000):
        if Is_Prime(i):
            sum += i
    return sum

def problem_11():

    pass

def problem_12():
    number = 0
    i = number
    while True:
        divs = []
        i += 1
        number += i
        #print(number)
        for j in range(1, number+1):
            if number % j == 0:
                divs.append(j)
        #print(divs)
        if len(divs)>500:
            break
    return number
        
Print_Answer(problem_12())