import pandas as pd
import random as rd

#email configuration
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = 'ruwicsbuddies@gmail.com'
EMAIL_PASSWORD = 'uclawgezoarwszbq'



col_list = ["Email address", "Full Name"]
df = pd.read_csv("t1.csv", usecols=col_list)
df_list=df.values.tolist() #converts dataframe to list
copy_df_list= df_list
num_pairs=len(df.index)/2
pairs_list= list() #list of pairs

while df_list:
    if len(df_list) ==3: #odd number of participants
        pair= rd.sample(df_list, 3)
        #print("item of 3 is:", pair)
        pairs_list.append(pair)
        break        
    else:
        pair= rd.sample(df_list, 2)
        if pair not in pairs_list: #avoid duplicates by checking if pair is created
            pairs_list.append(pair)
            for row in pair:
                    #print("item is:", item)
                    df_list.remove(row)

for pair in pairs_list: 
    #print("pair:", row)
    for individual in pair:
        print("individual:", individual)
        msg = EmailMessage() #instantiate email message class to send email
        msg['Subject'] = 'WiCS Buddy Bot Pair!'
        msg['From'] = EMAIL_ADDRESS 
        msg['To'] = [individual[0]]  #email will always be individual[0]
        
        #content of email
        html="""Hi, $(name)"""
        html = html.replace("$(name)", individual[1])
        msg.set_content(html)


        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) 
            smtp.send_message(msg)
