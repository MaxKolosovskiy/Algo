def max_experience(levels, experience):
    max_exp = 0
    array = [[0] * (i + 1) for i in range(levels)]

    for i in range(levels):
        for j in range(i + 1):
            if i == 0:
                array[i][j] = experience[i][j]
            elif j == 0:
                array[i][j] = array[i - 1][j] + experience[i][j]
            elif j == i:
                array[i][j] = array[i - 1][j - 1] + experience[i][j]
            else:
                array[i][j] = max(array[i - 1][j - 1], array[i - 1][j]) + experience[i][j]

            max_exp = max(max_exp, array[i][j])

    return max_exp

def main():
    with open("../resurses/career_in.txt", "r") as f:
        levels = int(f.readline().strip())
        experience = []
        for _ in range(levels):
            experience.append(list(map(int, f.readline().strip().split())))

    max_exp = max_experience(levels, experience)

    with open("../resurses/career_out.txt", "w") as f:
        f.write(str(max_exp))

if __name__ == "__main__":
    main()