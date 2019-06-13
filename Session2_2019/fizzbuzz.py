class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        list_of_strings = []
        for i in range(1, n+1):
            if i % 15 == 0:
                list_of_strings.append("FizzBuzz")
            elif i % 3 == 0:
                list_of_strings.append("Fizz")
            elif i % 5 == 0:
                list_of_strings.append("Buzz")
            else:
                list_of_strings.append(str(i))

        return list_of_strings

#  FASTER
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        list_of_strings = []
        for i in range(1, n+1):
            ans = ""
            if i % 3 == 0:
                ans += "Fizz"
            if i % 5 == 0:
                ans += "Buzz"
            if not ans:
                ans = str(i)

            list_of_strings.append(ans)

        return list_of_strings

        
