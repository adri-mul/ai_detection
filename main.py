# function returns a list of words split by spaces.
def read_file(filepath: str) -> list[str]:
    str_list = []
    with open(filepath) as fp:
        for line in fp:
            str_list.append(line.strip().split(" "))

    return str_list

# this is where you'll analyze the text samples
def main():
    print("Hello, world!")

if __name__ == "__main__":
    main()