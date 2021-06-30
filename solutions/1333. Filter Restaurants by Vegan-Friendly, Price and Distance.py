class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        out = defaultdict(list)
        for i in restaurants:
            if i[2] >= veganFriendly and i[3] <= maxPrice and i[4] <= maxDistance:
                out[i[1]].append(i[0])
                
        ans = []
        for rate in sorted(list(out.keys())):
            ans += sorted(out[rate])
        return ans[::-1]
