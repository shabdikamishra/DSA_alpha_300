class Solution:    
    def findUnion(self, a, b):
        #set automatically drops duplicates
                seen = set()

                #add from first array
                for num in a:
                    seen.add(num)

                #for second array
                for num in b:
                    seen.add(num)
                    
                return list(seen)