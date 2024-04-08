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
                        'Attendance': int(row.get('Attendance', 0)),
                        'PaidSessions': int(row.get('PaidSessions', 0)),
                        'UnpaidSessions': int(row.get('UnpaidSessions', 0)),
                        'Phone': row.get('Phone', ''),
                        'Address': row.get('Address', ''),
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

    def Paid_sorted(self):
        sorted_members = sorted(self.members.values(), key=lambda x: x['PaidSessions'], reverse=True)
        return sorted_members

  
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

