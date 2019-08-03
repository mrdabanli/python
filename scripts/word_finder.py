programming_languages = {
    "C",
    "C#",
    "C++",
    "Python",
    "Java",
    "Swift",
    "Ruby",
    "Go",
    "Dart"
}

value = input("Aramak istediğiniz programlama dilini giriniz: ")

def find_word(value, list):
    for word in list:
        if value in list:
            return "Kelime listede var."
            break
        else:
            return "Kelime listede yok!"


def main():
    print(find_word(value, programming_languages))


if __name__ == "__main__":
    main()