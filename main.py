import os
import getpass
from rich.console import Console
from rich.panel import Panel
from rich import box
from rich.table import Table
from datetime import datetime
import matplotlib.pyplot as plt




# ======================= Colors =======================
RED, GREEN, YELLOW, BLUE, CYAN, RESET = (
    "\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[96m", "\033[0m")
os.system("")  # enables ANSI colors in Windows cmd

# ======================= Data =======================
credentials = {"username": "admin", "password": "Py@12345"}
logout = False

items= [
    {"item_id": 1,"type": "Book","title": "Clean Code","author": "Robert C. Martin","isbn": "9780132350884","copies": 2,"available": 1},
    {"item_id": 2,"type": "Magazine","title": "National Geographic","author": "Various","issue": "November 2026","copies": 1,"available": 1},
    {"item_id": 3,"type": "Book","title": "Practical English","author": "William","isbn": "9780178491284","copies": 3,"available": 3}
]

members= [
    {"member_id": 101,"name": "Sara","active_loans": [501, 503]},
    {"member_id": 102,"name": "Ali","active_loans": [502]}
]

loans= [
    {"loan_id": 501, "item_id": 1,"member_id": 101,"borrow_date": "2026-11-05","due_date": "2026-11-19","return_date": "", "status":"active"},
    {"loan_id": 502, "item_id": 2,"member_id": 102,"borrow_date": "2026-11-10","due_date": "2026-11-24","return_date": "", "status":"active"},
    {"loan_id": 503, "item_id": 3,"member_id": 101,"borrow_date": "2026-10-01","due_date": "2026-10-15","return_date": "2026-10-14", "status":"returned"},
    {"loan_id": 504, "item_id": 1, "member_id": 102, "borrow_date": "2026-09-01", "due_date": "2026-09-15", "return_date": "2026-09-14", "status": "returned"},
    {"loan_id": 505, "item_id": 1, "member_id": 101, "borrow_date": "2026-08-01", "due_date": "2026-08-15", "return_date": "2026-08-14", "status": "returned"},
    {"loan_id": 506, "item_id": 1, "member_id": 102, "borrow_date": "2026-07-01", "due_date": "2026-07-15", "return_date": "2026-07-14", "status": "returned"}
]



# ================================== Skeleton =======================

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_banner():    
    console = Console()
    banner_text = """[cyan] ______   _______  _______  _       _________ _______          
(  ___ \ (  ___  )(  ___  )| \    /\\__   __/(  ____ \|\     /|
| (   ) )| (   ) || (   ) ||  \  / /   ) (   | (    \/( \   / )
| (__/ / | |   | || |   | ||  (_/ /    | |   | (__     \ (_) / 
|  __ (  | |   | || |   | ||   _ (     | |   |  __)     \   /  
| (  \ \ | |   | || |   | ||  ( \ \    | |   | (         ) (   
| )___) )| (___) || (___) ||  /  \ \___) (___| )         | |   
|/ \___/ (_______)(_______)|_/    \/\_______/|/          \_/   
    [/cyan]"""
    banner_panel = Panel(
        banner_text,
        title="[bold blue]WELCOME TO [/bold blue]",
        border_style="blue",
        box=box.ROUNDED,
        #padding=(1, 2)
          )
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
        print_banner()
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

def search_items(items):
    try:
        s = int(input(
            CYAN + "\t\n1. " + RESET + "Search by title: "
            + CYAN + "\t\n2. " + RESET + "Search by author: "
            + BLUE + "\nchoose a number: " + RESET
        ))
    except ValueError:
        print(RED + "Error! you must enter a number" + RESET)
        return

    
    print(YELLOW + "=======================================" + RESET)
    if s not in (1, 2):
        print(RED + "invalid number" + RESET)
        return
    s_key = input("enter content to search:").lower()
    found= False
    if s == 1:
        #compare s_key with title (not exact mach)
        for item in items:
            if s_key in item["title"].lower() :
                found = True
                show_items([item])

    elif s == 2:
        for item in items:
            if s_key in item["author"].lower() :
                found =True
                show_items([item])


    if found == False:
        print(RED+"search content not found"+RESET)

def find_member(member_id):
    for member in members:
        if member["member_id"] == member_id :
            return member # Return the member dictionary if found

    return None

def find_item(item_id):
    for item in items:
        if item["item_id"] == item_id :
            return item  # Return the item dictionary if found

    return None


def borrow_item(member_id, item_id):
    member = find_member(member_id)
    item = find_item(item_id)

    # Check if member exists
    if member is None:
        print(RED + "Error! The member_id does not exist." + RESET)
        return

    # Check if item exists
    if item is None:
        print(RED + "Error! The item_id does not exist." + RESET)
        return

    # Count the member's active loans
    active_loans = 0
    for loan in loans:
        if loan["member_id"] == member_id and loan["status"] == "active":
            active_loans += 1
    # Check whether the member has reached the active loan limit
    if active_loans >= 3:
        print(RED+"Error! The member has reached the maximum limit of 3 active loans." +RESET)
        return
    # Check whether the member already has this item
    for loan in loans:
        if (loan["member_id"] == member["member_id"] 
            and loan["item_id"] == item["item_id"] 
                and loan["status"] == "active"):
            print(RED + "Error! This member already has this item on loan." + RESET)
            return

    # check if item is available(copies>0)
    if item["available"] <= 0 :
        print(RED+"Error! Item is not available"+RESET)
        return
    else :
        item["available"] -= 1  
        
    #create loan
    if len(loans) > 0:
        new_id = max(loan["loan_id"] for loan in loans) + 1
    else:
        new_id = 1
    new_loan ={
        "loan_id": new_id,"item_id": item_id,"member_id":member_id,
        "borrow_date":"Today","due_date": "due_date","return_date": "" ,"status":"active"}
        
    loans.append(new_loan)
    print(GREEN+"Item borrowed successfully!"+RESET)


def return_item(loan_id):
    found = False
    for loan in loans:
        if loan["loan_id"] == loan_id:
            found = True
            #cheack status
            if loan["status"] == "returned":
                print(RED+"This loan has already been returned"+RESET)
                return None
            elif loan["status"] == "active":
                loan["status"] = "returned"
                itemid = loan["item_id"]

                # Convert the borrow date string into a datetime to calculate the difference from today
                due_date = datetime.today()
                borrow_date = datetime.strptime(loan["borrow_date"], "%Y-%m-%d")
                diff = due_date - borrow_date
                # Convert difference to number of days
                delay = diff.days

    if found == True:
        for item in items:
            if item["item_id"] == itemid:
                item["available"] += 1
                item_type = item["type"].lower()

                # computing late penalty
                if item_type == "book":
                    max_delay = 14
                    penalty_per_day = 0.5
                elif item_type == "magazine":
                    max_delay = 7
                    penalty_per_day = 0.25

                if delay > max_delay:
                    late_penalty = (delay - max_delay) * penalty_per_day
                    return delay, late_penalty
                else:
                    late_penalty = 0
                    print(GREEN + "late_penalty is Zero" + RESET)
                    return delay, late_penalty

    if found == False:
        print(RED + "Error! Loan ID does not exist" + RESET)
        return None

def active_loans_report(loans, members, items):
    total_fine = 0
    active_count = 0
    console = Console()
    today=datetime.today().date()
    table = Table(title="Active Loans Report" , box=box.ROUNDED, show_lines=True,
              header_style='bold magenta', row_styles=['', 'dim'])
    table.add_column("Member" , style='cyan', no_wrap=True , justify='center')
    table.add_column("Title", style='cyan', no_wrap=True , justify='center')
    table.add_column("Borrow date", style='cyan', no_wrap=True , justify='center')
    table.add_column("Due date", style='cyan', no_wrap=True , justify='center')
    table.add_column("Status", style='cyan', no_wrap=True , justify='center')
    table.add_column("Days overdue", style='red', no_wrap=True , justify='center')
    table.add_column("Fine ", style='red', no_wrap=True , justify='center')
    for loan in loans:
        if loan["return_date"] == "": #active loans
            active_count += 1
            due= datetime.strptime(loan["due_date"] ,"%Y-%m-%d").date()

            for item in items:
                if item["item_id"] == loan["item_id"]:
                    item_title = item["title"]
                    item_type = item["type"]

                    if item_type == "book":
                        fine_per_day = 0.5
                    else:
                        fine_per_day = 0.25

            if due < today:
                days_overdue = (today - due).days
                fine = days_overdue * fine_per_day
                total_fine += fine
                print(item_title, days_overdue, fine)

                status = "[red]Overdue[/red]"              
            else:
                days_overdue = "-"
                fine = "-"
                status = "[green]Ontime[/green]"
            

            for member in members:
                if member["member_id"] == loan["member_id"]:
                    member_name = member["name"]


            table.add_row(member_name, item_title, loan["borrow_date"], loan["due_date"] , status,str(days_overdue),str(fine))
    table.add_section()
    table.add_row(
        "",
        "",
        "",
        "",
        "",
        "Total fine:",
        str(total_fine),
        style="bold"
    )

    if active_count == 0:
        table.add_row("-", "No active loans", "-", "-", "-", "-", "-")
    console.print(table)


def show_chart():
    borrow_counts = {}
    
    most_borrowed_item = None  
    #for each item id in loan ,put item id and its count in borrow_count{}  
    for loan in loans:
        item_id = loan["item_id"]
        if item_id in borrow_counts:
            borrow_counts[item_id] += 1
        else:
            borrow_counts[item_id] =1
    print(borrow_counts)
    #find the item id that its count is the most
    max_count =0
    most_borrowed_item = None  
    #move on borrow_cont's item id and compare each value with max_count and update max_count
    for itemid in borrow_counts:
        if max_count <= borrow_counts[itemid]:
            max_count = borrow_counts[itemid]
            most_borrowed_item = itemid
    print (most_borrowed_item ,max_count)

    #
    item_ids = []
    borrow_cnts = []
    for itemid in borrow_counts:
        borrow_cnts.append(borrow_counts[itemid])
        item_ids.append(itemid)

    # Create a list of tuples containing the borrow count and item ID
    items_list = []
    for itemid in borrow_counts:
        count = borrow_counts[itemid]
        items_list.append((count, itemid))
        
    # Sort the items list in descending order based on borrow counts
    items_list = sorted(items_list, reverse=True)
    top_items = items_list[:5]
    # Separate top items into counts and IDs for the chart
    top_ids = []
    top_counts = []
    for item in top_items:
        top_counts.append(item[0])
        top_ids.append(item[1])
    # Create the bar chart
    plt.bar(top_ids, top_counts)
    # Display the chart
    plt.show()








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
                        search_items(items)
                        ex = input("\npress b to back to menu (or any key to continue): ").strip().lower()
                        if ex == "b":
                            break 
# borrow   ????????????????????????????????????????????????????????????????????????????????how to init today and due date ??????????                    
                case 5:
                    while True:
                        clear_screen()
                        while True:
                            try:
                                member_id= int(input("please enter member ID: "))
                                break
                            except ValueError :
                                print(RED+"Error! member ID is a number"+RESET)
                        while True:        
                            try:
                                item_id = int(input("please enter item ID:"))
                                break
                            except ValueError :
                                print(RED+"Error! item ID is a number"+RESET)
                        borrow_item(member_id ,item_id)
                        ex = input("\npress b to back to menu (or any key to continue): ").strip().lower()
                        if ex == "b":
                            break 
# return                        
                case 6:
                    while True:
                        clear_screen()     
                        try:
                            loan_id = int(input("please enter loan ID: "))
                        except ValueError:
                            print(RED + "Error! loan ID is a number" + RESET)
                            continue

                        delay ,penalty = return_item(loan_id)
                        print(f"delay: {delay}  \nLate penalty: {penalty} ")

                        ex = input("\nPress b to go back to menu (or any key to continue): ").strip().lower()
                        if ex == "b":
                            break
# overdue report                       
                case 7:
                    while True:
                        clear_screen()
                        active_loans_report(loans, members, items)
                        ex = input("\npress b to back to menu (or any key to continue): ").strip().lower()
                        if ex == "b":
                            break 
# chart                        
                case 8:
                    while True:
                        clear_screen()
                        show_chart()
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

