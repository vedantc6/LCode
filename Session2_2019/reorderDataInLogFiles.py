class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        digits = []
        letters = []

        for val in logs:
            if val.split(' ')[1].isnumeric():
                digits.append(val)
            else:
                letters.append(val.split(" ", 1))
        letters = sorted(letters, key=lambda x: (x[1], x[0]))
        letters = [" ".join(letter) for letter in letters]
        return letters + digits
        
