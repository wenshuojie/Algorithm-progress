# 合并区间

def merge(intervals): # intervals: List[List[int]]
    intervals.sort(key=lambda x: x[0])
    results = []
    for interval in intervals:
        if len(results)==0 or results[-1][1] < interval[0]:
            results.append(interval)
        else:
            results[-1][1] = max(results[-1][1],interval[1])

    return results

print(merge([[0,4],[1,5]]))