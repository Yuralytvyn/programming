class Hamster:

    def __init__(self, package_per_day, greed):
        self.package_per_day = package_per_day
        self.greed = greed

    def __del__(self):
        pass

    def __str__(self):
        return 'For {0} hamster number packages per day = {1} , greed = {2}.'.format(
            i + 1, self.package_per_day, self.greed)

    def total_one(self, n):
        total_per_day = self.package_per_day + self.greed * (n - 1)
        return total_per_day

    def worst_one(self, n):
        greedNum = n - 1
        if (n - 2 > 0):
            greedNum = n - 2
        total_per_day = self.package_per_day + self.greed * (greedNum)
        return total_per_day


def total_all(hamsters):
    n = len(hamsters)
    total_all_per_day = 0
    for i in range(n):
        total_per_day = hamsters[i].total_one(n)
        total_all_per_day += total_per_day
    return total_all_per_day


def the_worst_hamster_delete(hamsters):
    n = len(hamsters)
    total_all_per_day = total_all(hamsters)
    if s >= total_all_per_day:
        return(n)

    worst = 0
    for i in range(n):
        if hamsters[worst].worst_one(n) < hamsters[i].worst_one(n):
            worst = i
    if n != 0:
        hamsters.pop(worst)
        n -= 1
    return the_worst_hamster_delete(hamsters)


s = int(input('Enter total food per day : '))
c = int(input('Enter number of hamsters : '))
hamsters = []
for i in range(c):
    h, g = list(map(int, input('Enter number packages per day, greed for {0} hamster: '.format(i + 1)).split()))
    hamsters.append(Hamster(h, g))
print(the_worst_hamster_delete(hamsters))