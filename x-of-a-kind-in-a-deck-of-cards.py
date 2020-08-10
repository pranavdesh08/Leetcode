class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        cnt = collections.Counter(deck)
        low = min(cnt.values())
        
        if low <=1:
            return False
        
        def gcd(x,y):
            while y:
                x,y = y,x%y
            print(x) 
            return x
        
        for i in set(deck):
            print('i',i)
            if gcd(low,cnt[i]) < 2 :
                return False
            else:
                low = cnt[i]
        return True
