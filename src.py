import pandas as pd
import random as rd
#email configuration
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = 'ruwicsbuddies@gmail.com'
EMAIL_PASSWORD = 'INSERT PASSWORD HERE'


col_list = ["Email address", "Full Name"]
df = pd.read_csv("names_modd.csv", usecols=col_list)
df_list=df.values.tolist() #converts dataframe to list

num_pairs=len(df.index)/2
pairs_list= list() #list of pairs

while df_list:
    if len(df_list) ==3: #odd number of participants
        x=rd.choice(df_list)
        df_list.remove(x)
        y=rd.choice(df_list)
        df_list.remove(y)
        z=rd.choice(df_list)
        pair= [x,y,z]
        break        
    else:
        x=rd.choice(df_list)
        df_list.remove(x)
        y=rd.choice(df_list)
        df_list.remove(y)
        pair= [x,y]

        if pair not in pairs_list: #avoid duplicates by checking if pair is created
            pairs_list.append(pair)
        else:
            df_list.append(x)
            df_list.append(y)

#TODO: 1) extract first names and last names 2) extract email 3) send to email

msg = EmailMessage()
msg['Subject'] = 'This is my test email for multiple people'
msg['From'] = EMAIL_ADDRESS 
msg['To'] = ['recipient1, 'recipient2']
msg.set_content('it works')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) 
    smtp.send_message(msg)
