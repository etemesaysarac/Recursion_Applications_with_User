

num = input('Enter your number here : ')
num = int(num)

def calculateFactorial(num):
    if num == 0:
        return 1
    else:
        return num * calculateFactorial(num-1)


print(calculateFactorial(num))


def calculateContigousSum(num):
    if num == 0:
        return 0
    else:
        return num + calculateContigousSum(num-1)


print(calculateContigousSum(num))