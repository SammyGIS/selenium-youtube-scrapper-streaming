
import os
import gspread
import openpyxl
import df2gspread as d2g
from df2gspread import df2gspread as d2g
from oauth2client.service_account import ServiceAccountCredentials


def load_2_googlesheet(data:"dataframe",cell_number:"str"):
    """
    This functions load DataFrame into a google sheet used as database
    
    Args: 
        Dataframe: Data that will be uploaded to the db
        
        cell_number : The cell number where the data input will be pasted into the db
    
    """
    try:
        scope = ['https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive"]

        credentials = ServiceAccountCredentials.from_json_keyfile_name('key_credentials.json',scope)
        gs = gspread.authorize(credentials)

        spreadsheet_key = '1V7LQXgIZpQCaGkQlSFQBs4wNXDRDhL4-BadGx3TRpE8'
        wks_name = 'Abia'
        
        upload_file = d2g.upload(data, spreadsheet_key, wks_name,
                         credentials=credentials,row_names=False, clean = False,
                         col_names=False, start_cell= cell_number)
        print("file has been uploaded succesuflly to the database")
    
    
    except ConnectionError as e:
        print("An error occurred. Perphaps your network is down or Google server is down. Retry.....Later")