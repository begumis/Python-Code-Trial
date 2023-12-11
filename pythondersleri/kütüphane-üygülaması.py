book_list = list()
title = "---MENU---"
title1 = "{:^15}".format(title)
menu = """ 
 1)Add Book
 2)Delete Book
 3)Display Books
 Q)Exit
"""
def add_book(list,book):
    list += [book]
    print("Book added succesfully.")

def remove_book(list,book):
  list.remove(book)
  print("Book deleted succesfully.")
def dispilay(list):
    for a in list:
        print("Book Name >>>>>>>>>>>", a)
def Exit():
    print("Thank you for choosing us.... ")
    quit()

while True:
    print(title1)
    print(menu)
    choice = input("Please enter a choice: ")
    if choice == "1":
        book_name = input("Please enter the name of the book: ")
        add_book(book_list, book_name)
    elif choice == "2":
        book_name = input("Please enter the name of the book: ")
        remove_book(book_list, book_name)
    elif choice == "3":
       dispilay(book_list)
    elif choice == "Q" or choice == "q":
        Exit()
    else:
        print("Please enter a valid choice!!!")
    input("Please press ENTER to return to main menu!")