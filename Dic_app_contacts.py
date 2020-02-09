#contact app

contacts=[]

while(True):
    print("1 Add contact :")
    print("2 Search contact :")
    print("3 Del contact :")
    print("4 Update contact :")
    print("5 Display contact :")
    print("6 Sort by name: ")
    print("7 Sort by email: ")
    print("8 sort by phone: ")

    print()
    choice= int(input("enter choice: "))

    if(choice==1):
        contact={}
        contact['name']=input("enter name: ")
        contact['email']=input("enter email: ")
        contact['phone']=input("enter phone: ")
        contacts.append(contact)
    elif(choice==2):
        search=input("enter seach keyword: ")
        isfound=False
        for contact in contacts:
            if(contact['name']== search or contact['email']== search or contact['phone']==search):
                print("name: ", contact['name'])
                print("email: ", contact['email'])
                print("phone: ", contact['phone'])
                isfound=True
        if(isfound==False):
            print("contact not found")
    elif(choice==3):
        search=input("enter seach keyword: ")
        isfound=False
        for contact in contacts:
            if(contact['name']== search or contact['email']== search or contact['phone']==seach):
                contacts.remove(contact)
                isfound=True
        if(isfound==False):
            print("contact not found")
    elif(choice==4):
        search=input("enter seach keyword: ")
        isfound=False
        for contact in contacts:
            if(contact['name']== search or contact['email']== search or contact['phone']==seach):
                contact['name']=input("enter name")
                contact['email']=input("enter email")
                contact['phone']=input("enter phone")
                isfound=True
        if(isfound==False):
            print("contact not found")
        elif(choice==5):
            for contact in contacts:
                print("Name: ", contact['name'])
                print("email: ", contact['email'])
                print("phone: ", contact['phone'])
        elif(choice==6):
            contacts.sort(key=lambda x:x['name'])
        elif(choice==7):
            contacts.sort(key=lambda x:x['email'])
        elif(choice==8):
            contacts.sort(key=lambda x:x['phone'])
        elif(choice==0):
            break













        
