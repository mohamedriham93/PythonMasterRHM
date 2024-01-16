username = input("enter your username: ")
password = input("enter your password: ")


print ("A = add books")
print ("B = delete books")
print ("C = View books")
print ("D = Return books")
print ("E = Logout")

A = "ADD BOOKS"
B = "DELETE BOOKS"
C = "VIEW BOOKS"
D = "RETURN BOOKS"
E = "LOGOUT"

select_option = input("Select any option [A / B / C / D / E]: ")
if (select_option == "A"):
    print (A)
    book_name = input("Enter book name: ")
    aurthor = input("Enter aurthor name: ")

    if (select_option == "B"):
        print (B)
        if (select_option == "C"):
            print(C)
            if (select_option == "D"):
                print(D)
                if (select_option == "E"):
                    print(E)
