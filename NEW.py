import datetime

class Main:



class Members:
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

