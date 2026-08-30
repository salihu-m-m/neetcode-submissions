class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_char_s = sorted(s)
        sorted_char_t = sorted(t)
        sorted_t = "".join(sorted_char_t)
        sorted_s = "".join(sorted_char_s)
        if sorted_t == sorted_s:
            return True
        else:
            return False       
            
        

               
            
        