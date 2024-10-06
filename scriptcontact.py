from telethon.sync import TelegramClient
from telethon.tl.functions.contacts import GetContactsRequest
import csv

api_id = 'enterYourApiId'
api_hash = 'enterYourApiHAsh'
phone_number = '+2376#########'

client = TelegramClient('session_name', api_id, api_hash)
client.start(phone=phone_number)
contacts = client(GetContactsRequest(hash=0)).users

with open('skpContacts.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Phone'])  
    for contact in contacts:
        name = (contact.first_name or '') + (f" {contact.last_name}" if contact.last_name else '')
        phone = contact.phone if contact.phone else 'N/A'  
        writer.writerow([name, phone])

print("Contacts exported succesfully from telegram to skpContacts.csv")
client.disconnect()
