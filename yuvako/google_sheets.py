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

    spreadsheet = client.open("Sabha BLR")  
    worksheet = spreadsheet.get_worksheet(0)  

    all_records = worksheet.get_all_records()
    row_index = None
    for index, record in enumerate(all_records, start=2): 
        if record["MobileNumber"] == MobileNumber: 
            row_index = index
            break

    if row_index is not None:
        cell_range = f"A{row_index}:F{row_index}" 
        worksheet.update(cell_range, [list(updated_data.values())])