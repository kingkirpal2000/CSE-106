if __name__ == "__main__":
    sentence = input("Enter punishment sentence:\t")
    sentence += "\n"
    try:
        reps = eval(input("Enter number of repetitions:\t"))
    except ValueError:
        print("Error: Please enter value")
        raise

    with open("CompletedPunishment.txt", "w") as writer:
        writer.write(sentence*reps)