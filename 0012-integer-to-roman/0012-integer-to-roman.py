class Solution(object):
        
    def convert(self, n, answer=""):
        if n == 0:
            return answer
        
        elif n >= 1000:
            return self.convert(n - 1000, answer + "M")
            
        elif n >= 500:
            if n / 900 == 1:
                return self.convert(n - 900, answer + "CM")
            else:
                return self.convert(n - 500, answer + "D")
        
        elif n >= 100:
            if n / 400 == 1:
                return self.convert(n - 400, answer + "CD")
            else:
                return self.convert(n - 100, answer + "C")
        
        elif n >= 50:
            if n / 90 == 1:
                return self.convert(n - 90, answer + "XC")
            else:
                return self.convert(n - 50, answer + "L")
        
        elif n >= 10:
            if n / 40 == 1:
                return self.convert(n - 40, answer + "XL")
            else:
                return self.convert(n - 10, answer + "X")
        
        elif n >= 5:
            if n / 9 == 1:
                return self.convert(n - 9, answer + "IX")
            else:
                return self.convert(n - 5, answer + "V")
        
        elif n >= 1:
            if n / 4 == 1:
                return self.convert(n - 4, answer + "IV")
            else:
                return self.convert(n - 1, answer + "I")
    
    
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        return self.convert(num)