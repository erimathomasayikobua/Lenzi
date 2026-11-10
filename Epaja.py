from datetime import date
from typing import Optional, Any

class Loan:
    """Represents a borrowing transaction between a Member and an Item."""

    def __init__(self, loan_id: int, borrow_date: date, due_date: date, status: str = "Active"):
        self._loan_id = loan_id
        self._borrow_date = borrow_date
        self._due_date = due_date
        self._return_date: Optional[date] = None
        self._status = status
        
        self._item: Optional[Any] = None
        self._member: Optional[Any] = None

    # ==========================================
    # Properties (Getters & Setters)
    # ==========================================
    
    @property
    def loan_id(self) -> int:
        return self._loan_id

    @property
    def borrow_date(self) -> date:
        return self._borrow_date

    @property
    def due_date(self) -> date:
        return self._due_date

    @property
    def return_date(self) -> Optional[date]:
        return self._return_date

    @return_date.setter
    def return_date(self, value: date) -> None:
        self._return_date = value

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, value: str) -> None:
        self._status = value

    @property
    def item(self) -> Optional[Any]:
        return self._item

    @item.setter
    def item(self, item: Any) -> None:
        self._item = item

    @property
    def member(self) -> Optional[Any]:
        return self._member

    @member.setter
    def member(self, member: Any) -> None:
        self._member = member

    # ==========================================
    # Business Logic Methods
    # ==========================================

    def is_overdue(self) -> bool:
        if self._status == "Returned":
            return False
        return date.today() > self._due_date

    def record_return(self) -> None:
        if self._status == "Returned":
            print(f"Loan #{self._loan_id} has already been returned.")
            return

        self._return_date = date.today()
        self._status = "Returned"
        
        if self._item and hasattr(self._item, 'mark_available'):
            self._item.mark_available()
            
        print(f"Loan #{self._loan_id} successfully returned on {self._return_date}.")

    # ==========================================
    # Magic Methods
    # ==========================================

    def __repr__(self) -> str:
        return (
            f"Loan(id={self._loan_id}, status='{self._status}', "
            f"borrowed={self._borrow_date}, due={self._due_date}, "
            f"returned={self._return_date})"
        )

    def __str__(self) -> str:
        item_name = getattr(self._item, 'name', 'Unknown Item') if self._item else 'Unknown Item'
        return f"Loan #{self._loan_id} for {item_name}"
        