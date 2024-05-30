def printOddNumber(numbers):
    for x in numbers:
        if x % 2 != 0:
            print(x)


def main():
    inputList = input("Enter seven integers separated by commas: ")
    numbers = list(map(int, inputList.split(',')))
    printOddNumber(numbers)


if __name__ == "__main__":
    main()
