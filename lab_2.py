class Hamster:

    def __init__(self, package_per_day, greed):
        self.package_per_day = package_per_day
        self.greed = greed

    def __del__(self):
        pass

    def __str__(self):
        return 'For {0} hamster number packages per day = {1} , greed = {2}.'.format(
            i + 1, self.package_per_day, self.greed)

    def total_one(self, n, counter):
        total_per_day = self.package_per_day + self.greed * (n - counter)
        return total_per_day


def total_all(hamsters, counter_of_loop,counter):

    arr = []
    summ=0

    for i in range(len(hamsters)):
        total_per_day = hamsters[i].total_one(len(hamsters), counter)
        arr.append(total_per_day)
    arr.sort()
    for i in range(counter_of_loop):
        if counter_of_loop == 0:
            return arr
        else:
            arr.pop()
    for i in range(len(arr)):
        summ+=arr[i]
        arr[i]=summ

    return arr



def binary_search(arr, searched_value):
    low, high = 0, len(arr) - 1
    best_ind = low
    if searched_value > arr[len(arr) - 1]:
        best_ind = len(arr) - 1
    else:
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] < searched_value:
                low = mid + 1
                if arr[mid + 1] > searched_value:
                    best_ind = mid
                    break
            elif arr[mid] > searched_value:
                high = mid - 1
            else:
                best_ind = mid
                break
            if mid < arr[best_ind] < mid + 1:
                return best_ind - 1
    return best_ind + 1


def making_arr(c,counter_of_loop,counter):
    arr = []

    while counter_of_loop<c:
        totalall = total_all(hamsters, counter_of_loop,counter)
        arr.append(binary_search(totalall, s))
        counter_of_loop+=1
        counter += 1
        if counter_of_loop==c:
            break

    return arr


s = int(input('Enter total food per day : '))
c = int(input('Enter number of hamsters : '))

hamsters = []
counter = 1
counter_of_loop = 0

for i in range(c):
    h, g = list(map(int, input('Enter number packages per day, greed for {0} hamster: '.format(i + 1)).split()))
    hamsters.append(Hamster(h, g))

arr=making_arr(c,counter_of_loop,counter)
arr.sort()
last_number=arr[len(arr)-1]
print(last_number)
