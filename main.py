
def main():
    book_content = get_book()
    count_words(book_content)
    number_of_characters = count_characters(book_content)
    report_data = number_of_characters
    print("--- Begin report of books/frankenstein.txt")
    report = make_report(report_data)
    print("--- End report ---")


def get_book():
    with open("books/frankenstein.txt") as book:
        book_content = book.read()
        return book_content


def count_words(book_content):
    individual_words = book_content.split()
    print(f"THE TOTAL NUMBER OF WORDS: {len(individual_words)}")


def count_characters(book_content):
    number_of_characters = {}
    for character in book_content.lower():
        if character.isalpha():
            if character in number_of_characters:
                number_of_characters[character] += 1
            else:
                number_of_characters[character] = 1
    return number_of_characters


def make_report(number_of_characters):
    report_list = []
    for key, value in number_of_characters.items():
        tmp = [key, value]
        report_list.append(tmp)
    report_list.sort()

    for character_count in report_list:
        print(f"The '{character_count[0]}' character was found {character_count[1]} times")


main()


# COUNTING CHARACTERS - THIS TAKES WAY TOO LONG
# for word in individual_words:
#     if word.isalpha():
#         for character in word:
#             number_of_characters.update({character: book_content.count(character) for character in word})
# return number_of_characters
