class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = []
        x = 0
        length = len(prices)
        for x in range(length-1):
            discount = 0
            new_price = prices[x]
            for y in range(x+1, len(prices)):
                if prices[y]<=new_price:
                    discount = prices[y]
                    break
            result.append(new_price-discount)
        result.append(prices[length-1])
        return result

# Runtime: 56 ms, faster than 50.27% of Python3 online submissions for Final Prices With a Special Discount in a Shop.
# Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Final Prices With a Special Discount in a Shop.
