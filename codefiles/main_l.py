def read_file():
    f = open('availabilities.txt', 'r')
    lines = f.readlines()
    for line in lines:
        line = line.replace("\n", "")
        info = line.split(':')
        slot = int(info[0]) - 1
        available = int(info[1])
        AVAILABILITIES.insert(slot, available)
    f.close()


def save_file():
    f = open('availabilities.txt', 'w')
    for i in range(len(AVAILABILITIES)):
        print("%d:%d" % (i+1, AVAILABILITIES[i]), file=f)
    f.close()


def check_slot():
    slot = int(input("Enter the index of the slot you want to check : "))
    if AVAILABILITIES[slot-1] == 0:
        print("The slot", slot, "is available")
    else:
        print("The slot", slot, "is not available")
    return AVAILABILITIES[slot-1]


def display_available():
    slots = []
    for i in range(len(AVAILABILITIES)):
        if AVAILABILITIES[i] == 0:
            slots.append(i+1)
    return slots


def nbr_available():
    count = 0
    for i in AVAILABILITIES:
        if i == 0:
            count += 1
    return count


"""
def make_reservation(slot):
    select = False
    while not select:
        slot = int(input(
            "Enter the index of the slot you",
            "want to reserve (press 0 to quit) : "
        )) - 1
        if slot < 0 or slot > 99:
            select = True
        elif AVAILABILITIES[slot] == 1:
            print("Sorry, this slot is not available right now")
        else:
            AVAILABILITIES[slot] = 1
            print("Your slot is well reserved")
"""


def main():
    read_file()
    end = False
    while not end:
        choice = int(input("Enter the feature you want to use : "))
        if choice == 1:
            check_slot()
        elif choice == 2:
            print(display_available())
        elif choice == 3:
            print(nbr_available())
        elif choice == 4:
            make_reservation()
        else:
            save_file()
            end = True


if __name__ == '__main__':
    main()
