#Erima Thomas Ayikobua M23B13/032

class Member:
    def __init__(self, member_id, full_name, room_number, phone):
        self.member_id = member_id
        self.full_name = full_name
        self.room_number = room_number
        self.phone = phone

    def register(self):
        print(f"Member {self.full_name} registered successfully.")

    def list_item(self):
        pass

    def request_item(self):
        pass

member1 = Member(
    101,
    "John Smith",
    "Room 12",
    "0701234567"
)

member1.register()


from models.member import Member


class Admin(Member):

    def __init__(self, member_id, full_name, room_number,
                 phone, admin_role):

        super().__init__(
            member_id,
            full_name,
            room_number,
            phone
        )

        self.admin_role = admin_role

    def approve_loan(self):
        pass

    def suspend_member(self):
        pass

