class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        a = []
        order = 0
        count = 0
        

        for i in range(n):

            if chars[i] not in a or chars[i] != chars[i-1]  :
                if count>1:
                    val = str(count)
                    a.extend(val)
                a.append(chars[i])
                count=0
            count += 1
            order += 1

            if order == n and count >1:
                val = str(count)
                a.extend(val)

        chars[:] = a
        return len(a)
        
    

