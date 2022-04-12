def isAnagram(s:str,t:str)->bool:
    hash_s = {}
    hash_t = {}
    for char in s:
        if char in hash_s:
            hash_s[char] += 1
        else: hash_s[char] = 1
    for char in t:
        if char in hash_t:
            hash_t[char] += 1
        else: hash_t[char] = 1
    print(hash_s.items(), hash_t.items())
    
    if hash_s == hash_t:
        return True
    return False

if __name__ == "__main__":
    s='anagram'
    t='nagaram'
    print(isAnagram(s,t))