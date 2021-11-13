def main():
    # write your code below this line
    A = "impossible!"
    B = "failed"
    C = 1
    D = 2
    E = 3
    F = 4
    G = 5
    H = "incredible"
    point = int(input("Give Points [0-100]\n"))
    if point < 0:
        print("Grade: ", A)
    elif point >= 0 and point <= 49:
        print("Grade:", B)
    elif point >= 50 and point <= 59:
        print("Grade:", C)
    elif point >= 60 and point <= 69:
        print("Grade: ", D)
    elif point >= 70 and point <= 79:
        print("Grade:", E)
    elif point >= 80 and point <= 89:
        print("Grade:", F)
    elif point >= 90 and point <= 100:
        print("Grade:", G)
    elif point > 100:
        print("Grade:", H)
    else:
        print()


if __name__ == '__main__':
    main()
