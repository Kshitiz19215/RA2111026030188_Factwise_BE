def cardScore (points , k):
    n = len (points)
    size_window = n - k
    total_sum = sum(points)
    sum_window = sum(points[:size_window])
    min_sum = sum_window

    for i in range(size_window,n):
        sum_window += points[i] - points[i-size_window]
        min_sum = min(min_sum,sum_window)
    
    return total_sum - min_sum

#sample input
print(cardScore([1,2,3,4,5,6,7,8,9], 3))