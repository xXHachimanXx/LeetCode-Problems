# docs: https://docs.google.com/document/d/1C0LAhoju1eWwrNbzchcOIux454xtmohkNbiHUic6PMc/edit
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

def comparable( interval):
    return interval.start

def overlap_intervals( intervals):
    
    if len(intervals) < 2: return intervals

    intervals.sort(key=lambda x: x.start) # O(n*log(n))


    min = -float('inf')
    max = -float('inf')

    overlaped_intervals = []
    # [(0,2),(1,4),(3,5)]
    for index, interval in enumerate(intervals): # min = 1 | max = 3
        
        if interval.start > max:
            if index != 0:
                overlaped_intervals.append( Interval(min, max) )
            min = interval.start
            max = interval.end
        elif interval.end > max:
            max = interval.end
        
        
        
    if max != -float('inf') and [min, max] not in overlaped_intervals:
        overlaped_intervals.append(Interval(min, max))

    return overlaped_intervals

assert overlap_intervals([Interval(1,3)]) == [Interval(1,3)]
assert overlap_intervals([Interval(1,3),Interval(2,6),Interval(8,10),Interval(15,18)]) == [Interval(1,6),Interval(8,10),Interval(15,18)]