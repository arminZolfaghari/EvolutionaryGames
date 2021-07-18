import matplotlib.pylab as plt


def write_to_file(max, min, avg):
    with open("Generation_info.txt", "a") as file:
        file.write("{} {} {}\n".format(max, min, avg))


def read_from_file():
    max_arr, min_arr, avg_arr = [], [], []
    with open("Generation_info.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        line_arr = line.split(" ")
        max_arr.append(int(line_arr[0]))
        min_arr.append(int(line_arr[1]))
        avg_arr.append(float(line_arr[2][: -1]))

    return max_arr, min_arr, avg_arr


if __name__ == "__main__":
    max_arr, min_arr, avg_arr = read_from_file()
    plt.plot(max_arr, color='b', label="max fitness value")
    plt.plot(min_arr, color='r', label="max fitness value")
    plt.plot(avg_arr, color='g', label="max fitness value")

    plt.xlabel("Generation Number")
    plt.ylabel("Fitness Value")
    plt.legend()
    plt.show()
