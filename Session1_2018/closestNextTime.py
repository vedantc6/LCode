# Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.
# You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

# Input: "19:34"
# Output: "19:39"
# Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.

# Input: "23:59"
# Output: "22:22"
# Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.

def nextClosestTime(time):
    hours = time[:2]
    minutes = time[3:]
    current = 60*int(hours) + int(minutes)
    unique_digits = {int(t) for t in time if t.isdigit()}
    while True:
        current = (current+1)%(24*60)
        if all(digit in unique_digits for hm in divmod(current, 60) for digit in divmod(hm, 10)):
            return "{:2d}:{:2d}".format(*divmod(current, 60))

if __name__ == '__main__':
    print(nextClosestTime("19:34"))
    print(nextClosestTime("23:59"))
