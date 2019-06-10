class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        res = []
        for email in emails:
            at_index = email.find("@")
            temp = email[:at_index].replace(".","") + email[at_index:]
            at_index = temp.find("@")
            plus_index = temp.find("+")
            if plus_index != -1:
                temp = temp[:plus_index], temp[at_index:]
            res.append(temp)
        return len(set(res))
        
