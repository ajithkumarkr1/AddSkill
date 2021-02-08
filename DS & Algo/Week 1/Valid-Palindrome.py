class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower() # to convert everything to lowercase
        f=filter(str.isalnum,s)  # isalnum is used to check  whether characters in the string are alphanumeric
        s="".join(f) # to join them all into a string 
        if(s==s[::-1]):  # if reverse of the string is true
            return True
        else:
            return False
