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

    def worst_one(self, n):class Hamster:

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

    def get_package_per_day(self):
        return self.package_per_day


def total_all(hamsters, nubmerOfHamsters):
    n = len(hamsters)
    total_all_per_day = 0
    for i in range(n):
        total_per_day = hamsters[i].total_one(nubmerOfHamsters)
        total_all_per_day += total_per_day
    return total_all_per_day

def max_hamsters_amount(hamsters, nubmerOfHamsters):
    if nubmerOfHamsters == 0:
        best_without_greed = hamsters[0].get_package_per_day()
        for i in range(len(hamsters)):
            if best_without_greed < hamsters[i].get_package_per_day():
                best_without_greed = hamsters[i].get_package_per_day()

        if(best_without_greed <=s):
            return 1
        else:
            return 0

    temp=hamsters.copy()
    while len(temp) - nubmerOfHamsters > 0:
        worst = 0
        for i in range(len(temp)):
            if temp[worst].total_one(nubmerOfHamsters) < temp[i].total_one(nubmerOfHamsters):
                worst = i
        if len(temp) != 0:
            temp.pop(worst)

    total_all_per_day = total_all(temp, len(temp))
    if s >= total_all_per_day:
        return (len(temp))

    nubmerOfHamsters -= 1
    return max_hamsters_amount(hamsters, nubmerOfHamsters)


s = int(input('Enter total food per day : '))
c = int(input('Enter number of hamsters : '))
hamsters = []
for i in range(c):
    h, g = list(map(int, input('Enter number packages per day, greed for {0} hamster: '.format(i + 1)).split()))
    hamsters.append(Hamster(h, g))

print(max_hamsters_amount(hamsters, len(hamsters)))



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
