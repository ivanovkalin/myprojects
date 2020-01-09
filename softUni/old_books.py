book_name = input()
library_capacity = int(input())

books_counter = 1
is_book_found = False

while books_counter <= library_capacity:
    current_book = input()

    if book_name == current_book:
        books_counter -= 1
        print(f"You checked {books_counter} books and found it.")
        is_book_found = True
        break
    books_counter += 1

if not is_book_found:
    books_counter -= 1
    print("The book you search is not here!")
    print(f"You checked {books_counter} books.")

