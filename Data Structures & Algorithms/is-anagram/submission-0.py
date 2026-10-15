class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def is_same_dict(q: str):
            temp_dict ={}
            for i in q:
                if i in temp_dict:
                    temp_dict[i]+=1
                else:
                    temp_dict[i]=1
            return temp_dict
        return is_same_dict(s) == is_same_dict(t)