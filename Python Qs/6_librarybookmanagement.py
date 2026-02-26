book_dict={
    
    "python":5,
    "dsa":8,
    "c++":10
    
}
def add_book():
    print("--------adding the book----------")
    m=input("enter the book name:")
    n=int(input("enter number of copies:"))
    
    if m in book_dict:
        book_dict[m]+=n
        print("book added successfully")
         
    else:
        book_dict[m]=n
        print("book added successfully")
        
def remove_book():
    print("------removing the book----------")
    s=input("enter the book name to remove:")
    
    if s in book_dict:
        book_dict.pop(s) 
        print("book removed successfully")
        
    else:
        print("book not fount in library")
        
        
def borrow_book():
    print("-------borrowing the book---------")                        
    h=input("enter the book to borrow:")
    if h in book_dict:
        if book_dict[h]>0:
            book_dict[h]-=1
            print("successfully borrowed")
            return
        else:
            print(f"{h} is currently out of stock") 
    
    else:
        print(f"{h} book is not available")    
        
        
def return_book():
    print("-------returning the book----------")
    g=input("enter the book to return:")       
    if g in book_dict:
        book_dict[g]+=1
    else:
        print("this book is not belong to our library")
        
def show_book():
    print("--------------BOOK MENU-----------------------")
    for book,quantity in book_dict.items():
        print(book,':',quantity)      
        
def exit():
    print("successfully exited,THANK YOU Visit again")       
    
print("----------Welcome to JALAGARA'S library---------------")    
print("select the option")
print("1.To Adding the book")         
print("2.To Removing the book")         
print("3.To Borrowing the book")         
print("4.To Return the book")         
print("5.For Book menu")         
print("6.For Exit")        

k=int(input("enter a option:"))

match(k):
    case 1:
        add_book()
        print("After adding,book list was:")
        for book,quantity in book_dict.items():
            print(book,':',quantity) 
        
    case 2:
        remove_book()
        print("After removing book list was:")
        for book,quantity in book_dict.items():
            print(book,':',quantity)
        
    case 3:
        borrow_book()
        
    case 4:
        return_book()
        print("After returned book list was:")
        for book,quantity in book_dict.items():
            print(book,':',quantity)
        
    case 5:
        show_book()
        
    case 6:
        exit()                    
            
    case _:
        print("Invalid option")        
    
  