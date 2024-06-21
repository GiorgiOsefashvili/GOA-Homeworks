def main():
    names = []
    for i in range(5):
        name = input("Enter a name: ")
        names.append(name)

    print("First three names:")
    print(names[0:3])

if __name__ == "__main__":
    main()
