
'''



def merge(intervals):
    def merge_eff(intervals):
        if not intervals or len(intervals) == 1:
            return intervals

        res = []
        intervals.sort(key=lambda x: x[0])

        def merge_intervals(a, b):
            return [min(a[0], b[0]), max(a[1], b[1])]

        skipelem = False
        for i in range(len(intervals)):
            if skipelem:
                skipelem = False
                continue

            if i==len(intervals)-1:
                break
            currelem = intervals[i]
            nextelem = intervals[i + 1]

            if currelem[1] >= nextelem[0]:
                res.append(merge_intervals(currelem, nextelem))
                skipelem = True
            else:
                res.append(currelem)

        #if intervals[-1][0] > intervals[-2][1]:
        if intervals[-1][1] >= res[-1][0]:#intervals[-1][0] > res[-1][1]:
            res.append(intervals[-1])
        else:
            res.append(merge_intervals(intervals[-1], res[-1]))

        return res

    result = merge_eff(intervals)
    while True:
        if result == merge_eff(result):
            return result
'''

'''

def merge_recur(intervals):
    res = []
    intervals.sort(key=lambda x:x[0])
    if len(intervals)<=0:
        return intervals

    for i in range(len(intervals)-1,0,-1):
        currelem = intervals[i]
        prevelem = intervals[i-1]
        
'''

def merge_two(a,b):
    return [min(a[0],b[0]),max(a[1],b[1])]

def list_diff(a,b):
    return [x for x in a if x not in b]

def merge_recur(intervals):


    def merge_simple(intervals):
        intervals.sort(key=lambda x:x[0])
        skipelem = False
        for i in range(len(intervals)-1):
            if skipelem:
                skipelem = False
                continue
            if i>len(intervals)-1:
                break
            currelem = intervals[i]
            nextelem = intervals[i+1]
            if currelem[1]>=nextelem[0]:
                intervals  = list_diff(intervals,[currelem,nextelem])
                intervals.append(merge_two(currelem,nextelem))
                intervals.sort(key=lambda x: x[0])
                skipelem = True

        return intervals

    res = merge_simple(intervals)

    while True:
        temp = merge_simple(res)
        if res == temp:
            return res
        else:
            res = temp




ex =   [[8,10],[1,3],[2,6],[15,18]]
#ex =   [[1,4],[0,2],[3,5]]
#merge_recur(ex)
print(merge_recur(ex))


