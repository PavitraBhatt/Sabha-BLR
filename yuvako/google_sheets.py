# import gspread
# from oauth2client.service_account import ServiceAccountCredentials

# def add_to_google_sheet(data):
#     scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
#     creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
#     client = gspread.authorize(creds)

#     spreadsheet = client.open("Sabha Attendance BLR")
#     worksheet = spreadsheet.get_worksheet(0)  # Choose the correct worksheet index

#     worksheet.append_row(data)



# yuvako/google_sheets.py
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def add_yuvako_to_sheet(yuvako_data):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("P:\\Python\\Projects\\credentials.json", scope)
    client = gspread.authorize(creds)

    spreadsheet = client.open("Sabha BLR")  # Change to your spreadsheet title
    worksheet = spreadsheet.get_worksheet(0)  # Choose the correct worksheet index

    worksheet.append_row(yuvako_data)

# Call this function whenever a karyakarta adds a yuvako
# You can call this function from your karyakarta API view after successfully adding a yuvako
# Example:
# yuvako_data = ["Yuvako Name", "Yuvako Email", "Yuvako Phone"]
# add_yuvako_to_sheet(yuvako_data)



