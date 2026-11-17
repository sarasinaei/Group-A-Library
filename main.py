import os
import getpass
from rich.console import Console
from rich.panel import Panel
from rich import box
from rich.table import Table

# ======================= Colors =======================
RED, GREEN, YELLOW, BLUE, CYAN, RESET = (
    "\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[96m", "\033[0m")
os.system("")  # enables ANSI colors in Windows cmd

# ======================= Data =======================
credentials = {"username": "admin", "password": "Py@12345"}
logout = False

items= [
    {"item_id": 1,"type": "Book","title": "Clean Code","author": "Robert C. Martin","isbn": "9780132350884","copies": 2,"available": 1},
    {"item_id": 2,"type": "Magazine","title": "National Geographic","author": "Various","issue": "November 2026","copies": 1,"available": 1} , 
    {"item_id": 3,"type": "Book","title": "Practical English","author": "William","isbn": "9780178491284","copies": 3,"available": 3}  ,    
    ]
members= [
    {"member_id": 101,"name": "Sara","active_loans": [501]},
    {"member_id": 102,"name": "Ali","active_loans": []}
      ],
loans= [
    {"loan_id": 501,"item_id": 1,"member_id": 101,"borrow_date": "2026-11-10","due_date": "2026-11-24","return_date": ""},
    {"loan_id": 502,"item_id": 2,"member_id": 102,"borrow_date": "2026-10-01","due_date": "2026-10-08","return_date": "2026-10-06"}
  ]


# ================================== Skeleton =======================

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_banner():    
    console = Console()
    banner_text = """[cyan]
░████████     ░██████     ░██████   ░██     ░██ ░██████░██████████░██     ░██    
░██    ░██   ░██   ░██   ░██   ░██  ░██    ░██    ░██  ░██         ░██   ░██     
░██    ░██  ░██     ░██ ░██     ░██ ░██   ░██     ░██  ░██          ░██ ░██      
░████████   ░██     ░██ ░██     ░██ ░███████      ░██  ░█████████    ░████       
░██     ░██ ░██     ░██ ░██     ░██ ░██   ░██     ░██  ░██            ░██        
░██     ░██  ░██   ░██   ░██   ░██  ░██    ░██    ░██  ░██            ░██        
░█████████    ░██████     ░██████   ░██     ░██ ░██████░██            ░██                                                                                                                                                                                                                                                                            
    [/cyan]"""
    banner_panel = Panel(
        banner_text,
        title="[bold blue]WELCOME TO [/bold blue]",
        border_style="blue",
        box=box.ROUNDED,
        padding=(1, 2) )
    console.print(banner_panel)


def print_menu():
    print(YELLOW + "=============================== MENU ===============================" + RESET)
    items = ["add item","register member", "show items", "search", "borrow", "return",
              "overdue report", "chart", "exit"]
    for number, item in enumerate(items, 1):
        print(f"  {BLUE}{number}{RESET}. {item}")

def LoginSystem():
    attempt = 0
    while attempt <3:
        clear_screen()
        user_ = input("username: ")
        pass_ = getpass.getpass("password: ")
        if user_ == "admin" and pass_ =="Py@12345":
            input(GREEN+"Login successful"+RESET+"\nPress Enter to continue...")
            return True
        else:
            attempt +=1
            input(RED+"wrong pasword."+RESET + f"you try {attempt} of 3.\nPress Enter to continue...")   
    return False

def add_item(items):
    Type = input("type =")
    Item_id= input("item_id =")
    Title= input("title =")
    Author= input("author =")
    Isbn= int(input("isbn ="))
    Copies= int(input("copies ="))

    for item in items:
        if item["item_id"] == Item_id:
            return 

    new_item={
        "type":Type, "item_id": Item_id ,"title":Title,"author":Author ,"isbn":Isbn,
          "copies": int(Copies) ,"available":int(Copies)
    } 
    items.append(new_item)  
    print(GREEN +"Item added successfully."+RESET) 
    

def register_member(members):
    Member_id = int(input("member_id ="))
    Name = input("name =").strip()
    Active_loans = []
    for member in members:
        if member["member_id"] == Member_id:
            print(RED+"This member id already exists."+RESET)
            return
    new_member ={
    "member_id":Member_id  , "name":Name  ,"active_loans": Active_loans}
    members.append(new_member)
    print(GREEN +"Item added successfully."+RESET) 

#Create table using rich 
def show_items(items):
    table = Table(title='Items', box=box.ROUNDED, show_lines=True,
              header_style='bold magenta', row_styles=['', 'dim'])
    table.add_column('Type', style='cyan', no_wrap=True)
    table.add_column('Item_id', justify='center')
    table.add_column('title', justify='right', style='green')
    table.add_column('Author', style='cyan', no_wrap=True)
    table.add_column('Copies', justify='center')
    table.add_column('Available', justify='right', style='green')
    for item in items:
        table.add_row(item["type"], str(item["item_id"]),item["title"] ,item["author"] ,str(item["copies"]) ,str(item["available"]))   
    return table
        

def main():
    console = Console()
    if LoginSystem():
        while True:
            clear_screen()
            print_banner()
            print_menu()
            choice = int(input(YELLOW +"Enter Your Choice :" +RESET))
            match choice:
# add item  
                case 1:
                    while True:
                        clear_screen()
                        add_item(items)
                        ex = input("\npress b to back to menu (or any key to continue): ").strip().lower()
                        if ex == "b":
                            break
# register member                        
                case 2:
                    while True:
                        clear_screen()
                        register_member(members)
                        ex = input("\npress b to back to menu (or any key to continue): ").strip().lower()
                        if ex == "b":
                            break  
# show items                                 
                case 3:
                    while True:
                        clear_screen()
                        table=show_items(items)
                        Console().print(table)
                        ex = input("\npress b to back to menu (or any key to continue): ").strip().lower()
                        if ex == "b":
                            break 
# search                        
                case 4:
                    while True:
                        clear_screen()
                        print("implementing search ")
                        ex = input("\npress b to back to menu (or any key to continue): ").strip().lower()
                        if ex == "b":
                            break 
# borrow                        
                case 5:
                    while True:
                        clear_screen()
                        print("implementing borrow ")
                        ex = input("\npress b to back to menu (or any key to continue): ").strip().lower()
                        if ex == "b":
                            break 
# return                        
                case 6:
                    while True:
                        clear_screen()     
                        print("implementing return ")
                        ex = input("\npress b to back to menu (or any key to continue): ").strip().lower()
                        if ex == "b":
                            break 
# overdue report                       
                case 7:
                    while True:
                        clear_screen()
                        print("implementing overdue report ")
                        ex = input("\npress b to back to menu (or any key to continue): ").strip().lower()
                        if ex == "b":
                            break 
# chart                        
                case 8:
                    while True:
                        clear_screen()
                        print("implementing chart ")
                        ex = input("\npress b to back to menu (or any key to continue): ").strip().lower()
                        if ex == "b":
                            break 
# exit                        
                case 9:
                    logout = True
                    clear_screen()
                    input(GREEN +" Goodbye!" + RESET )
                    break 
# invalid choice
                case _:
                    input(RED+"You must choose a number between 1-9 !"+RESET)
    else:
        clear_screen()
        print(RED+"Access Denied!..."+RESET)

if __name__ == "__main__":
    main()

