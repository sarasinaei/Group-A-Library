from datetime import date, timedelta


# ===============================================================================================================================
#                                                   Class LibraryItem
# ===============================================================================================================================
class LibraryItem:

    def __init__(self, item_id, title, author, copies, available):
        self.item_id = item_id
        self.title = title
        self.author = author
        self.copies = copies
        self.available = available

    def loan_days(self):
        pass

    def fine_per_day(self):
        pass

    def calculate_fine(self, days_late):
        return days_late * self.fine_per_day()

    @classmethod
    def from_dict(cls, data):  # rebuild an object from a dict
        return cls(
            data["item_id"],
            data["title"],
            data["author"],
            data["copies"],
            data["available"],
        )

    def to_dict(self):
        return {
            "item_id": self.item_id,
            "title": self.title,
            "author": self.author,
            "copies": self.copies,
            "available": self.available,
        }


# ===============================================================================================================================
#                                                   Class Book
# ===============================================================================================================================
class Book(LibraryItem):

    def __init__(self, item_id, title, author, copies, available, isbn):
        super().__init__(item_id, title, author, copies, available)
        self.isbn = isbn

    def loan_days(self):
        return 14

    def fine_per_day(self):
        return 0.50

    def to_dict(self):
        return {
            "item_id": self.item_id,
            "title": self.title,
            "author": self.author,
            "copies": self.copies,
            "available": self.available,
            "isbn": self.isbn,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            item_id=data["item_id"],
            title=data["title"],
            author=data["author"],
            copies=data["copies"],
            available=data.get("available"),
            isbn=data["isbn"],
        )


# ===============================================================================================================================
#                                                   Class Magazine
# ===============================================================================================================================
class Magazine(LibraryItem):

    def __init__(self, item_id, title, author, copies, available, issue):
        super().__init__(item_id, title, author, copies, available)
        self.issue = issue

    def loan_days(self):
        return 7

    def fine_per_day(self):
        return 0.25

    def to_dict(self):
        return {
            "item_id": self.item_id,
            "title": self.title,
            "author": self.author,
            "copies": self.copies,
            "available": self.available,
            "issue": self.issue,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            item_id=data["item_id"],
            title=data["title"],
            author=data["author"],
            copies=data["copies"],
            available=data.get("available"),
            issue=data["issue"],
        )


# ===============================================================================================================================
#                                                   Class Member
# ===============================================================================================================================
class Member:

    def __init__(self, member_id, name, active_loans):
        self.member_id = member_id
        self.name = name
        self.active_loans = active_loans

    def can_borrow(self):
        if len(self.active_loans) < 3:
            return True
        return False

    def to_dict(self):
        return {
            "member_id": self.member_id,
            "name": self.name,
            "active_loans": self.active_loans,
        }

    @classmethod
    def from_dict(cls, data_dic):
        return cls(
            data_dic["member_id"], data_dic["name"], data_dic["active_loans"]
        )


# ===============================================================================================================================
#                                                   Class Loan
# ===============================================================================================================================
class Loan:

    def __init__(
        self, item_id, member_id, borrow_date, due_date, return_date
    ):
        self.item_id = item_id
        self.member_id = member_id
        self.borrow_date = borrow_date
        self.due_date = due_date
        self.return_date = return_date

    def days_late(self):
        today = date.today()
        due = date.fromisoformat(self.due_date)
        if self.return_date is None:
            diff = (today - due).days
            if diff < 0:
                return 0
            else:
                return diff
        else:
            return_date = date.fromisoformat(self.return_date)
            diff = (return_date - due).days
            if diff < 0:
                return 0
            else:
                return diff

    def is_overdue(self):
        if self.days_late() > 0:
            return True
        return False

    def to_dict(self):
        return {
            "item_id": self.item_id,
            "member_id": self.member_id,
            "borrow_date": self.borrow_date,
            "due_date": self.due_date,
            "return_date": self.return_date,
        }

    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            data_dict["item_id"],
            data_dict["member_id"],
            data_dict["borrow_date"],
            data_dict["due_date"],
            data_dict["return_date"],
        )


# ===============================================================================================================================
#                                                   Class Library
# ===============================================================================================================================
class Library:

    def __init__(self, items, members, loans):
        self.items = items
        self.members = members
        self.loans = loans

    def add_item(self, item):
        self.items.append(item)

    def register_member(self, member):
        self.members.append(member)

    def search(self, keyword):
        keyword = keyword.lower()
        result = []
        for item in self.items:
            if (
                keyword in item.title.lower()
                or keyword in item.author.lower()
            ):
                result.append(item)
        return result

    # Count the number of currently active (unreturned) loans for a member
    def active_loans_count(self, member):
        cnt = 0
        for loan in self.loans:
            if (
                loan.member_id == member.member_id
                and loan.return_date is None
            ):
                cnt += 1
        return cnt

    # Check if the member already has an active loan for the item
    def has_active_loan_for_item(self, member, item):
        for loan in self.loans:
            if (
                loan.member_id == member.member_id
                and loan.item_id == item.item_id
                and loan.return_date is None
            ):
                return True
        return False

    def borrow(self, item, member):
        # Validate that both item and member belong to the library
        if item not in self.items:
            return None

        if member not in self.members:
            return None

        # Check maximum active loan limit (up to 3 items)
        if self.active_loans_count(member) >= 3:
            return None

        # Prevent borrowing the same item more than once concurrently
        if self.has_active_loan_for_item(member, item):
            return None

        # Ensure at least one copy is available
        if item.available <= 0:
            return None

        # Decrease available copies and calculate loan dates
        item.available -= 1
        borrow_date = date.today().isoformat()
        due_date = (date.today() + timedelta(days=item.loan_days())).isoformat()

        # Create new loan and update records
        new_loan = Loan(
            item.item_id, member.member_id, borrow_date, due_date, None
        )
        self.loans.append(new_loan)
        member.active_loans.append(new_loan)
        return new_loan

    def return_item(self, item, member):
        for loan in self.loans:
            if (
                loan.item_id == item.item_id
                and loan.member_id == member.member_id
                and loan.return_date is None
            ):
                item.available += 1
                loan.return_date = date.isoformat(date.today())
                if loan in member.active_loans:
                    member.active_loans.remove(loan)
                days_late = loan.days_late()
                fine_per_days = item.fine_per_day()
                if days_late > 0:
                    late_penalty = days_late * fine_per_days
                else:
                    late_penalty = 0
                return late_penalty
        return None

    def overdue_report(self):
        overdue_loans = []
        for loan in self.loans:
            if loan.return_date is None and loan.is_overdue():
                overdue_loans.append(loan)
        return overdue_loans

