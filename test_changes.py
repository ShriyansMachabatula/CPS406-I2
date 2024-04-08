# SHRIYANS MOHAMMAD AND VASHI

import csv

class ClubFinance:
    def __init__(self, csv_file):
        self.income_statement = {'revenues': [], 'expenses': []}
        self.members = {}  # Dictionary to hold member info
        self.load_members_from_csv(csv_file)

    def add_revenue(self, source, amount):
        self.income_statement['revenues'].append((source, amount))
    
    def calculate_total_revenue(self):
        return sum(amount for _, amount in self.income_statement['revenues'])

    def add_expense(self, source, amount):
        self.income_statement['expenses'].append((source, amount))
    
    def calculate_total_expenses(self):
        return sum(amount for _, amount in self.income_statement['expenses'])

    def load_members_from_csv(self, csv_file):
        try:
            with open(csv_file, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.members[row['MemberID']] = {
                        'Name': row['Name'],
                        'Attendance': int(row.get('Attendance', 0)),
                        'PaidSessions': int(row.get('PaidSessions', 0)),
                        'UnpaidSessions': int(row.get('UnpaidSessions', 0)),
                        'ConsecutiveMonthsPaid': int(row.get('ConsecutiveMonthsPaid', 0))
                    }
        except ValueError as e:
            print(f"Error loading CSV data: {e}")

    def update_member_attendance(self, member_id, attended=True, paid=False):
        member = self.members.get(member_id, {'Attendance': 0, 'PaidSessions': 0, 'UnpaidSessions': 0, 'ConsecutiveMonthsPaid': 0})
        if attended:
            member['Attendance'] += 1
        if paid:
            member['PaidSessions'] += 1
            member['ConsecutiveMonthsPaid'] += 1
            if member['ConsecutiveMonthsPaid'] >= 3:
                member['ConsecutiveMonthsPaid'] = 0
                self.apply_discount(member_id, discount_rate=0.1)
        else:
            member['UnpaidSessions'] += 1
            member['ConsecutiveMonthsPaid'] = 0
        self.members[member_id] = member

    def apply_discount(self, member_id, discount_rate):
        # Adjust member data to reflect the discount
        print(f"Applied {discount_rate*100}% discount to member {member_id}.")
        # Placeholder for discount application logic

    def apply_loyalty_discounts(self):
        sorted_members = self.organize_members_by_attendance()
        for member_id, _ in sorted_members[:10]:  # Top 10 attendees
            self.apply_discount(member_id, discount_rate=0.1)

    def organize_members_by_attendance(self):
        return sorted(self.members.items(), key=lambda x: x[1]['Attendance'], reverse=True)

    def check_and_apply_penalties(self):
        for member_id, stats in self.members.items():
            if stats['UnpaidSessions'] > 0:
                print(f"Reminder sent to member {member_id} for unpaid sessions.")

    def save_members_to_csv(self, csv_file):
        fieldnames = ['MemberID', 'Name', 'Attendance', 'PaidSessions', 'UnpaidSessions', 'ConsecutiveMonthsPaid']
        try:
            with open(csv_file, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for member_id, info in self.members.items():
                    row = {'MemberID': member_id, **info}
                    writer.writerow(row)
        except Exception as e:
            print(f"Error saving CSV data: {e}")

    # Adam's Code

    def create_member_list(self):
        # List of members
        member_list = []
        for member_id, details in self.members.items():
            if details['Attendance'] > 0: # Checking if they attended at least one class
                member_info = {
                    'MemberID': member_id,
                    'Phone': details['Phone'],
                    'Name': details['Name'],
                    'Address': details['Address']
                    'PaidSessions': details['PaidSessions'],
                    'UnpaidSessions': details['UnpaidSessions'],
                    'Streak': details['Streak'],
                }
                member_list.append(member_info)
        return member_list
    class PracticeSession:
        def __init__(self, member, date, coach, cost):
            self.member = member
            self.date = date
            self.coach = coach
            self.cost = cost
            self.payment_status = 'Pending'
    def make_payment(self, amount, practice_session):
            # Simulate payment
            print(f"{self.name} has made a payment of {amount} for {practice_session}")
            self.confirm_payment()

class Person():
    def __init__(self, member_id, name, phone, balance, address):
        self.member_id = member_id
        self.name = name
        self.phone = phone
        self.balance = balance
        self.address = address
        self.paid = False # Default paid status is False
        self.member_list = []
