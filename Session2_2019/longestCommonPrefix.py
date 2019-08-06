class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        i = 0
        flag = True
        min_len_ind = 0
        min_len = 999
        for j, single_str in enumerate(strs):
            n = len(single_str)
            if min_len > n:
                min_len = n
                min_len_ind = j
        while i < len(strs[min_len_ind]):
            letter = strs[min_len_ind][i]
            for single_str in strs:
                if letter != single_str[i]:
                    flag = False
                    break
                else:
                    flag = True
                # print(single_str, letter, i, flag)
            if flag:
                i += 1
            else:
                break
        return strs[0][:i]
