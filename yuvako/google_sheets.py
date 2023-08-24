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

    spreadsheet = client.open("Sabha BLR")  
    worksheet = spreadsheet.get_worksheet(0)  

    worksheet.append_row(yuvako_data)


import gspread
from oauth2client.service_account import ServiceAccountCredentials

def update_yuvako_in_sheet(MobileNumber, updated_data):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("P:\\Python\\Projects\\credentials.json", scope)
    client = gspread.authorize(creds)

    spreadsheet = client.open("Sabha BLR")  # Change to your spreadsheet title
    worksheet = spreadsheet.get_worksheet(0)  # Choose the correct worksheet index

    # Find the row index based on the MobileNumber
    all_records = worksheet.get_all_records()  # Fetch all records as dictionaries
    row_index = None
    for index, record in enumerate(all_records, start=2):  # Assuming header is in row 1
        if record["Mobile Number"] == MobileNumber: 
            row_index = index
            break

    if row_index is not None:
        # Update the cells in the row with the updated data
        cell_range = f"A{row_index}:F{row_index}"  # Assuming columns A to F need to be updated
        worksheet.update(cell_range, [list(updated_data.values())])