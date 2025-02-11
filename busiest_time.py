# Busiest Time in The Mall
# The Westfield Mall management is trying to figure out what the busiest moment at the mall was last year. You’re given data extracted from the mall’s door detectors. Each data point is represented as an integer array whose size is 3. The values at indices 0, 1 and 2 are the timestamp, the count of visitors, and whether the visitors entered or exited the mall (0 for exit and 1 for entrance), respectively. Here’s an example of a data point: [ 1440084737, 4, 0 ].

# Note that time is given in a Unix format called Epoch, which is a nonnegative integer holding the number of seconds that have elapsed since 00:00:00 UTC, Thursday, 1 January 1970.

# Given an array, data, of data points, write a function findBusiestPeriod that returns the time at which the mall reached its busiest moment last year. The return value is the timestamp, e.g. 1480640292. Note that if there is more than one period with the same visitor peak, return the earliest one.

# Assume that the array data is sorted in an ascending order by the timestamp. Explain your solution and analyze its time and space complexities.

def find_busiest_period(data: List[List[int]]) -> int:
    n = len(data)
    if n == 0:
        return 0

    count = 0
    maxcount = 0
    max_time = 0
    
    for i in range(n):
        if data[i][2] == 1:
            count += data[i][1]
        else:
            count -= data[i][1]


        if i < n-1 and data[i][0] == data[i+1][0]:
            continue
        
        if count > maxcount:
            maxcount = count
            max_time = data[i][0]
    return max_time
