import re

if __name__ == "__main__":
    count = 0
    word = input("Enter word to search in PythonSummary.txt:\t").strip()
    try:
        file = open("PythonSummary.txt", "r")
    except:
        print("Error: Couldn't open file")
        raise
    file = file.read().lower()
    txt = re.findall(r"[\w']+", file)
    for words in txt:
        if(words == word):
            count += 1
    print("Found " + word + " " + str(count) + " times.")


