class BookLibrary:
    directory = "./booksLibrary/"
    lib_dir = directory + "books.txt"

    def __init__(self, shelf_name):
        # Init with empty book self
        self.books_arr = []
        self.shelf_name = shelf_name
        self.create_shelf(self.shelf_name)

    # Creating shelf if it does not exists
    @staticmethod
    def create_shelf(shelf_name):
        name = BookLibrary.directory + shelf_name + ".txt"
        with open(name, "a") as f:
            pass

    def action(self):
        print("Action to be performed")
        print("1: Rent Book, 2: Add Book, 3: Books in main library, 4: Books in own library, 5: exit")
        action = int(input())

        if action == 1:
            self.rent_books()
        elif action == 2:
            self.add_books()
        elif action == 3:
            self.books_in_lib(self.lib_dir)
        elif action == 4:
            self.books_in_lib(self.directory + self.shelf_name + ".txt")
        elif action == 5:
            exit()

    @staticmethod
    def books_in_lib(shelf):
        with open(shelf, "r") as f:
            while True:
                line = f.readline()
                if line == "":
                    break

                split = line.split("@")

                if len(split) > 1:
                    if split[1] != "\n":
                        print(split[0], "---- Not Available")
                    else:
                        print(split[0])
                else:
                    print(split[0])

    def rent_books(self):
        print("Enter book name you want")
        books_name = input()

        if self.is_books_avail(books_name):
            BookLibrary.rent(books_name, self.shelf_name)
        else:
            print("Sorry book is not available. Try after sometime")

    @staticmethod
    def rent(books_name, reader_name):
        # Add book to user shelf
        with open(BookLibrary.directory + reader_name + ".txt", "a") as f:
            book = books_name + "\n"
            f.write(book)

        # Updating the main library
        books = []
        with open(BookLibrary.lib_dir) as f:
            while True:
                line = f.readline()
                if line == "":
                    break

                books.append(line)

        for i in range(len(books)):
            split = books.__getitem__(i).split("@")
            if split[0].lower() == books_name.lower():
                string = split[0].capitalize() + "@" + reader_name + "\n"
                books[i] = string

        with open(BookLibrary.lib_dir, "w") as f:
            f.writelines(books)

    @staticmethod
    def is_books_avail(book_name):
        with open(BookLibrary.lib_dir, "r") as f:
            while True:
                book = f.readline()
                if book == "" or book == "\n":
                    return False

                splits = book.split("@")
                lib_book_name = splits[0]
                book_rented_to = splits[1]

                if lib_book_name.lower() == book_name.lower():
                    if book_rented_to == "\n":
                        return True

    def add_books(self):
        print("Add Books To\n1: To Main Library, 2: Own Library")
        action = int(input())

        if action == 1:
            BookLibrary.add_to_main_lib()
        elif action == 2:
            BookLibrary.add_to_own_lib(self.shelf_name)

    @staticmethod
    def add_to_main_lib():
        print("Book Name?")
        book_name = input() + "@" + "\n"

        with open(BookLibrary.lib_dir, "a") as f:
            f.write(book_name)

    @staticmethod
    def add_to_own_lib(shelf_name):
        print("Book Name?")
        book_name = input() + "\n"

        with open(BookLibrary.directory + shelf_name + ".txt", "a") as f:
            f.write(book_name)
