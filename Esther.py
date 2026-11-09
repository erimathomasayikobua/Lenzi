from datetime import date, timedelta

from models.member import Member
from models.admin import Admin
from models.category import Category
from models.item import Item
from models.loan import Loan


# Create a member
member1 = Member(
    101,
    "John Smith",
    "Room 12",
    "0701234567"
)

# Create an admin
admin1 = Admin(
    1,
    "Erima Thomas",
    "Room 01",
    "0700000000",
    "System Administrator"
)

# Create categories
category1 = Category(1, "Electronics")

# Create an item
item1 = Item(
    101,
    "HP Laptop",
    "Good",
    category1
)

# Create a loan
loan1 = Loan(
    1,
    item1,
    member1,
    date.today(),
    date.today() + timedelta(days=7)
)


# Display system information
print("===== HOSTEL BORROWING CLUB =====")

print("\nMEMBER DETAILS")
print("Name:", member1.full_name)
print("Room:", member1.room_number)

print("\nADMIN DETAILS")
print("Name:", admin1.full_name)
print("Role:", admin1.admin_role)

print("\nITEM DETAILS")
print("Item:", item1.name)
print("Category:", item1.category.name)
print("Condition:", item1.condition)
print("Status:", item1.status)

print("\nLOAN DETAILS")
print("Loan ID:", loan1.loan_id)
print("Borrower:", loan1.member.full_name)
print("Borrowed item:", loan1.item.name)
print("Due date:", loan1.due_date)
print("Loan status:", loan1.status)