def maxProfit(prices:[int])-> int:
    profit = 0
    current_min = float('inf')
    for i,val in enumerate(prices):
        print(i,val)
        if val < current_min:
            current_min = val
        else:
            profit = max(val - current_min,profit)
        
    return profit

if __name__ == '__main__':
    prices = [7,1,5,4,6,4]
    out = maxProfit(prices)
    print(out)


'''
KEY CONCEPT: 
- track current_min and initialize it to float('inf')!!
'''