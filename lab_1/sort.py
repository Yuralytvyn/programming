class Ticket:

    def __init__(self,country,duration,cost):
        self.country=country
        self.duration=duration
        self.cost=cost

ticket1=Ticket("Ukraine",10,101)
ticket2=Ticket("Ukraine",41,614)
ticket3=Ticket("Ukraine",11,965)
ticket4=Ticket("Ukraine",61,164)
ticket5=Ticket("Ukraine",26,568)
ticket6=Ticket("Ukraine",71,109)
ticket7=Ticket("Ukraine",19,501)
ticket8=Ticket("Ukraine",96,171)

tripDuration=[ticket1.duration,ticket2.duration,ticket3.duration,ticket4.duration,ticket5.duration,ticket6.duration,ticket7.duration,ticket8.duration]
tripCost=[ticket1.cost,ticket2.cost,ticket3.cost,ticket4.cost,ticket5.cost,ticket6.cost,ticket7.cost,ticket8.cost]


def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def heapify(arr, n, i):
    largest = i 
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        heapify(arr, n, largest)
def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

bubbleSort(tripDuration)
heapSort(tripCost)

print("Trip duration is")
print(tripDuration)
print()
print("Cost of the trip is")
print(tripCost)


