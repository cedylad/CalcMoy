def main():
    # gather the first grade
    note1 = int(input("Enter the first grade: "))

    # gather the second grade
    note2 = int(input("Enter the second grade: "))

    # gather the third grade
    note3 = int(input("Enter the last grade: "))

    # calculate the average
    result = (note1 + note2 + note3) / 3

    # display the result
    print("The average is " + str(result))


if __name__ == '__main__':
    main()