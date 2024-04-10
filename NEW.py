import datetime
import csv

class Main:



import csv 

class Members:
    def __init__(self, csv_file):
        self.members = {}  
        try:
            with open(csv_file, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.members[row['MemberID']] = {
                        'Name': row['Name'],
                        'Phone': row.get('Phone', ''),
                        'Address': row.get('Address', ''),
                        'Attendance': int(row.get('Attendance', 0)),
                        'PaidSessions': int(row.get('PaidSessions', 0)),
                        'UnpaidSessions': int(row.get('UnpaidSessions', 0)),
                        'Streak': int(row.get('Streak', 0)), 
                    }
        except ValueError as e:
            print(f"Error loading CSV data: {e}")


    def check_payments_and_notify(self):
        penalty_fee = 50  # This is an example amount for a penalty fee
        exclusion_threshold = 3  # Members with unpaid sessions equal to or greater than this are excluded
        
        for member_id, details in self.members.items():
            unpaid_sessions = details['UnpaidSessions']
            paid_sessions = details['PaidSessions']
            if unpaid_sessions > 0:
                print(f"Reminder sent to {details['Name']} for {unpaid_sessions} unpaid session(s).")
                if paid_sessions < 2 and unpaid_sessions < exclusion_threshold:
                    print(f"Penalty of ${penalty_fee} applied to {details['Name']} for unpaid sessions.")                
                if unpaid_sessions >= exclusion_threshold:
                    print(f"{details['Name']} is being considered for exclusion due to {unpaid_sessions} unpaid sessions.")

    def create_member_list(self):
        member_list = []
        for member_id, details in self.members.items():
            if details['Attendance'] > 0:  
                member_info = {
                    'MemberID': member_id,
                    'Phone': details['Phone'],
                    'Name': details['Name'],
                    'Address': details['Address'],
                    'PaidSessions': details['PaidSessions'],
                    'UnpaidSessions': details['UnpaidSessions'],
                    'Streak': details['Streak'],
                }
                member_list.append(member_info)
        return member_list

    def paid_sorted(self):
        sorted_members = sorted(self.members.values(), key=lambda x: x['PaidSessions'], reverse=True)
        return sorted_members

    def attendance_sorted(self):
            # This method returns a list of members sorted by Attendance in descending order
            sorted_members_by_attendance = sorted(self.members.values(), key=lambda x: x['Attendance'], reverse=True)
            return sorted_members_by_attendance 
      
class Session:


  

class Finances:
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

        
  
    # Assume monthly salary is paid at the start of a new month
    def end_of_month(dt):
        todays_month = dt.month
        tmrws_month = (dt + datetime.timedelta(days=1)).month
      
        # Checks if tomorrow is the start of a new month
        if (tmrws_month != todays_month):
            return True
        else:
            return False  
    def make_payment(self, amount, practice_session):
        # Simulate payment
        # Increases income/treasurer balance
        # Notifies treasurer (us) of payment
        print(f"{self.name} has made a payment of {amount} for {practice_session}")
        self.confirm_payment()
