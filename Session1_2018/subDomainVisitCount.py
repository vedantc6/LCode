import re

class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        res = dict()
        listofdomains = []
        for cp in cpdomains:
            visits, domain = cp.split(" ")
            dots = [x.start() for x in re.finditer('\.', domain)]
            alldom = [domain[d+1:] for d in dots]
            alldom.append(domain)
            for dom in alldom:
                if dom in res:
                    res[dom] += int(visits)
                else:
                    res[dom] = int(visits)
        return ["{} {}".format(j, i) for i,j in res.items()]

# Faster implementation by someone else
class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """

        domain_count = {}
        for cpdomain in cpdomains:
            count, domain = cpdomain.split(' ')

            split_idx = 0
            curr_domain = domain[split_idx:]
            while split_idx >= 0:
                if curr_domain not in domain_count:
                    domain_count[curr_domain] = 0
                domain_count[curr_domain] += int(count)
                split_idx = domain.find('.', split_idx + 1)
                curr_domain = domain[split_idx + 1:]

        result = []
        for key, val in domain_count.items():
            result.append("{val} {key}".format(val=val, key=key))

        return result
