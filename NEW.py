import datetime
import csv

class Main:


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


    def informPayments(self):
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

    def complimentaryDiscounts(self):
        discount_percentage = 10  # 10% discount
        required_streak = 3  # Required streak of months without missing a payment
        for member_id, details in self.members.items():
            if details['Streak'] >= required_streak:
                print(f"{details['Name']} has earned a {discount_percentage}% discount for maintaining a payment streak of {details['Streak']} months.")
     


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
        self.members = {} 
        self.advance_payments = {}
        self.load_members_from_csv(csv_file)

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
            
    def add_revenue(self, source, amount, month):
        self.income_statement['revenues'].append({'source': source, 'amount': amount, 'month': month})
    
    def add_expense(self, source, amount, month):
        self.income_statement['expenses'].append({'source': source, 'amount': amount, 'month': month})

    def calculate_total_revenue(self):
        return sum(revenue['amount'] for revenue in self.income_statement['revenues'])

    def calculate_total_expenses(self):
        return sum(expense['amount'] for expense in self.income_statement['expenses'])
    
    def calculate_total_revenue(self):
        return sum(revenue['amount'] for revenue in self.income_statement['revenues'])
    def calculate_total_expenses(self):
        return sum(expense['amount'] for expense in self.income_statement['expenses'])


    def calculate_monthly_profit(self):
        # Reset monthly profit
        self.monthly_profit = {month: 0 for month in range(1, 13)}
        
        # Calculate revenues per month
        for revenue in self.income_statement['revenues']:
            month = revenue['month']
            self.monthly_profit[month] += revenue['amount']
        
        # Subtract expenses per month
        for expense in self.income_statement['expenses']:
            month = expense['month']
            self.monthly_profit[month] -= expense['amount']
        
        return self.monthly_profit
    
    def analyze_profit_change(self):
        months_with_data = sorted(self.monthly_profit.keys())
        profit_changes = {
            'increased': [],
            'decreased': [],
            'no_change': []
        }

        for i in range(1, len(months_with_data)):
            current_month = months_with_data[i]
            previous_month = months_with_data[i-1]
            current_profit = self.monthly_profit[current_month]
            previous_profit = self.monthly_profit[previous_month]

            if current_profit > previous_profit:
                profit_changes['increased'].append((current_month, current_profit - previous_profit))
            elif current_profit < previous_profit:
                profit_changes['decreased'].append((current_month, previous_profit - current_profit))
            else:
                profit_changes['no_change'].append(current_month)
    
        return profit_changes

    def add_advance_payment(self, member_id, amount, for_month):
        if for_month not in self.advance_payments:
            self.advance_payments[for_month] = []
        self.advance_payments[for_month].append({'member_id': member_id, 'amount': amount})

    def get_current_month_payables(self):
        current_month = datetime.now().month
        return sum(payment['amount'] for payment in self.advance_payments.get(current_month, []))


        
  
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
