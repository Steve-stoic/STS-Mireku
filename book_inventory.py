class Book_inventory:
    
    def __init__(self, book, quantity, inventory=None):
        self.book = book
        self.quantity = quantity
        if inventory is None:
            inventory = {}
        self.inventory = inventory
    
#Adding and updating a book in the system
    def add_book(self, book, quantity):
        try:
            if not isinstance(quantity, int):
                raise TypeError("The quantity must be an integer, please.")
            if book in self.inventory:
                self.inventory[book] += quantity
                print(f"{book} with quantity {quantity} has been added successfully")
                print(self.inventory)
            else:
                self.inventory[book] = quantity
                print(f"{book} with quantity {quantity} has been added successfully")
                print(self.inventory) 
        except TypeError as e:
            #print("The input type is invalid. Kindly enter a string for book and integer for quantity.")
            print(e)
        #except SyntaxError as e:
            #print("Check your syntax. An error occurred:", e)
        except Exception as e:
            print("An error occurred:", e)
        
       
    
#Delete a book
    def del_book(self, book):
        if book in self.inventory:
            self.inventory.pop(book)
            print(f"{book} has been deleted successfully")
            print(self.inventory)
        else:
            print(f"{book} is currently not in your inventory")
            print(self.inventory)
        

#Display just one book
    def display_book(self, book):
        if book in self.inventory:
            print(f"{book} has a quantity of {self.inventory.get(book)}")
        else: 
            print(f"{book} is currently not in your inventory")
            print(self.inventory)
            
#Lists out all the books available in the system
    def all_books(self):
        print(self.inventory)
        


        
mybooks = Book_inventory("book", 1)

mybooks.add_book(3, 3)

mybooks.add_book("48 laws", 4)
mybooks.add_book("the gods are not to blame", 2)
mybooks.add_book("the gods are not to blame", 2)
mybooks.display_book("the gods are not to")
mybooks.del_book("the gods are not to blame")
mybooks.all_books()


#testing exception
print("="*10, " test error ", '='*10)
mybooks.add_book(, "ghana")
mybooks.add_book()
