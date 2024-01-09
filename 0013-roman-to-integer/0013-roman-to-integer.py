from collections import OrderedDict

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        symbol_dict = OrderedDict()
        symbol_dict['IV'] = 4
        symbol_dict['IX'] = 9
        symbol_dict['XL'] = 40
        symbol_dict['XC'] = 90
        symbol_dict['CD'] = 400
        symbol_dict['CM'] = 900
        symbol_dict['I'] = 1
        symbol_dict['V'] = 5
        symbol_dict['X'] = 10
        symbol_dict['L'] = 50
        symbol_dict['C'] = 100
        symbol_dict['D'] = 500
        symbol_dict['M'] = 1000
        
        result = 0
        for symbol, value in symbol_dict.items():
            while s.find(symbol) != -1:
                s = s.replace(symbol, "", 1)
                result += value
                
        return result
        