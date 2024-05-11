class Solution(object):
    def destCity(self, paths):
        for i in paths:
            x=i[1]
            for j in paths:
                y = j[0]
                if x==y:
                    break
            else: 
                return x