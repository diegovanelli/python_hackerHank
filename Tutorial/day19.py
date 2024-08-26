class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError
 
class Calculator(AdvancedArithmetic):

    def divisorSum(self, n):
        divisors = []
        for i in range(n):
            index = i+1
            if ((n % index) == 0):
                divisors.append(index)
        return sum(divisors)

n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)