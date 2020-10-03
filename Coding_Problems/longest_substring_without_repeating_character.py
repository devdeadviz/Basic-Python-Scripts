def lengthOfLongestSubstring(self, s: str) -> int:
        word_set=set()
        n=len(s)
        ans=0
        i=0
        j=0
        while i<n and j<n:
            if(not s[j] in word_set ):
                word_set.add(s[j])
                j+=1
                ans=max(ans,j-i)
            else:
                word_set.remove(s[i])
                i+=1
        return ans

word=input()
print(lengthOfLongestSubstring(word))
