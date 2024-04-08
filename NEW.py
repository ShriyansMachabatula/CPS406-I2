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
  
    # Assume monthly salary is paid at the start of a new month
    def end_of_month(dt):
        todays_month = dt.month
        tmrws_month = (dt + datetime.timedelta(days=1)).month
      
        # Checks if tomorrow is the start of a new month
        if (tmrws_month != todays_month):
            return True
        else:
            return False  

