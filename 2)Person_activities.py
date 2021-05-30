
def activityselection(n, start, end):
    # checking if there's any need to sort with end time.
    test_sort = end[:]
    test_sort.sort()
    if test_sort != end:
    # sorting the end time of activities and saving the index of that sorting accordingly.
        li = []
        for i in range(len(end)):
            li.append([end[i], i])
        li.sort()
        sorted_index = []
        end.clear()
        for x in li:
            sorted_index.append(x[1])
            end.append(x[0])
        keydict = dict(zip(start, sorted_index))
        start.sort(key=keydict.get)
        total_activities = list(range(1,n+1))
        keydict = dict(zip(total_activities, sorted_index))
        total_activities.sort(key=keydict.get)

    activities = 1
    i = 0
    for j in range(1, n):
        if start[j] > end[i]:
            activities += 1
            i = j
    return activities
start = [1, 3, 2, 5]
end = [2, 4, 3, 6]
# start = [2, 1]
# end = [2, 2]

print(activityselection(4, start, end))

"""List sort method by default an implementation of Timesort that takes O(n * log n)
so time complexity will be  O(n * log n) and space complexity will be O(n)"""


