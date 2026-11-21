
LibraryItem   features >> item_id, title, author, copies, available
|             methods  >> loan_days(), fine_per_day(), calculate_fine(days_late), to_dict(), from_dict()
|
├── Book      features >> isbn
|             methods  >> loan_days() = 14, fine_per_day() = 0.5
|
└── Magazine  features >> issue
              methods  >> loan_days() = 7, fine_per_day() = 0.25
Member  features >> member_id,name,active_loans
        methods  >> can_borrow()  max=3
Loan    features >> item_id, member_id, borrow_date, due_date, return_date
        methods  >> days_late(), is_overdue()
Library features >> items,members,loans
        methods  >> add_item(), register_member(), search(), borrow(), return_item(),verdue_report()
 




