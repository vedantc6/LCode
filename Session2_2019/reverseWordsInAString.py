class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = re.findall(r"\S+", s)[::-1]
        return " ".join(s)
