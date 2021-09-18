from pyrogram import Client

API_ID = int(input("Enter TG account API_ID:- "))
API_HASH = input("Enter TG account API HASH:- ")
MOBILE = input("Enter TG account mobile number in international format :- ")
with Client(':memory:', api_id=API_ID, api_hash=API_HASH, phone_number=MOBILE) as app:
    print(app.export_session_string())