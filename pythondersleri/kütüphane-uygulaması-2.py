menü ="""
      -Python Kütüphanesine Hoş Geldiniz-
  
  1)Lend Book
  2)Barrow Book
  3)Display All
  Q)Exit
"""
list= list()

def lend_book(book:tuple, list:list):
   list.append(book)
   print("Thank you for the book you lent..." )
def check(book:tuple, list:list):
   if book in list:
      return True
   else:
      return False
def borrow_book(book:tuple, list:list):
   if check(book,list):
      list.remove(book)
      print("You have borrowed the book successfully. Good reading...")
   else:
      print("The book you requested is not available.")
def display_all(list:list):
   for a in list:
      print("Kitap adı: {}               Yazar Adı: {}".format(a[1], a[0]))

while True:
   print(menü)
   choice = input("Please enter your choice : ")
   if choice == "1":
      author = input("Author name: ")
      book_name = input("Book name: ")
      book = (author, book_name)
      lend_book(book,list)
   elif choice == "2":
      author = input("Author name: ")
      book_name = input("Book name: ")
      book = (author, book_name)
      borrow_book(book,list)
   elif choice == "3":
      display_all(list)
   elif choice == "Q" or choice =="q":
      print("Program is terminating...")
      quit()
   else:
      print("Please enter a valid choice!!!")

   input("Please press ENTER to return to main menu...")