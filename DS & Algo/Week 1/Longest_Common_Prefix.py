class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def prefix(a,b):
            n=min(len(a),len(b))
            s=''
            for i in range(n):
                if(a[i]==b[i]):
                    s=s+a[i]
                else:
                    return(s)
            return(s)
        def f(array):
            if(len(array)==0):
                return('')
            elif(len(array)==1):
                return(array[0])
            else:
                n=len(array)
                P=prefix(array[0],array[n-1])
                for i in range(1,n-1):
                    p=prefix(P,array[i])
                    P=p
                return(P)
        return(f(strs))
