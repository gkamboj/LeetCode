class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr = [str(i + 1) for i in range(n)]
        for ind in range(len(arr)):
            num = ind + 1
            if num % 15 == 0:
                arr[ind] = 'FizzBuzz'
            elif num % 3 == 0:
                arr[ind] = 'Fizz'
            elif num % 5 == 0:
                arr[ind] = 'Buzz'
        return arr
    
#Approach: Create an array of size n s.t. arr[i] = i + 1. Then check the given conitions for every element of array.