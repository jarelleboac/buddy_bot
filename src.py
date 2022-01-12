import pandas as pd
import random as rd
import csv

def write_to_existing_pairs1(fields, pairs_list):
    #writing the new pairs to the list of existing pairs, where each row in the csv is a pair
    with open('new_pairs.csv', 'a', newline='') as csvfile: #should be gfg fix later
        write = csv.writer(csvfile)
        write.writerow(fields)


def write_to_existing_pairs(fields, pairs_list):
    #writing the new pairs to the list of existing pairs, where each row in the csv is a pair
    with open('new_pairs.csv', 'a', newline='') as csvfile: #should be gfg fix later
        writer = csv.writer(csvfile)
        writer.writerows(pairs_list)


def buddy_bot():
    #email configuration
    import smtplib
    from email.message import EmailMessage
    EMAIL_ADDRESS = 'OMIT'
    EMAIL_PASSWORD = 'OMIT' #app password, exclude from github


    #initialize data structures for pairs
    col_list = ["Email address", "Full Name"] #extracting only the important values (for now): email, full name
    df = pd.read_csv("form_responses.csv", usecols=col_list) #reading in the form responses exported to csv into a dataframe
    df_list=df.values.tolist() #converts dataframe of form responses to list
    pairs_list= list() #list to store pairs in

    #SECTION 1:
    #---make current pairs while also checking that these pairs have not already been made---
    with open('GFG.csv') as file1:
        existing_lines = csv.reader(file1)
    
        while df_list:
            if len(df_list) == 3: #odd number of participants and we have gotten to the last 3 pairs
                pair= rd.sample(df_list, 3)
                #print("item of 3 is:", pair)
                pairs_list.append(pair)
                break        
            else: 
                pair= rd.sample(df_list, 2)
                if pair not in pairs_list and pair not in existing_lines: #avoid duplicates by checking if pair is created
                    pairs_list.append(pair)
                    for row in pair:
                            #print("item is:", item)
                            df_list.remove(row)

    print("pairs list:")
    print(pairs_list)


    #SECTION 2:
    #---BEGIN TO WRITE PAIRS TO CSV---
    # field names 
    fields = ['Person1', 'Person2', 'Person3'] 
    


    #readiing to check if headers already exist in csv file
    with open('new_pairs.csv', 'r', newline='') as csvfile:
        existingLines = [line for line in csv.reader(csvfile, delimiter=',')]

        #reader = csv.reader(csvfile)
        if fields not in existingLines:
            print("fields not in existing lines")
            write_to_existing_pairs1(fields, pairs_list)
            write_to_existing_pairs(fields, pairs_list)
        else:
            print("fields existing in lines")
            write_to_existing_pairs(fields, pairs_list)


    #SECTION 3:
    #---CREATE EMAIL TEMPLATE AND SEND PAIR BY PAIR---
    for pair in pairs_list: 
            msg = EmailMessage() #instantiate email message class to send email
            msg['Subject'] = 'WiCS Buddy Bot Pair!'
            msg['From'] = EMAIL_ADDRESS 

            #content of email
            if len(pair) == 3: #if this is a pair of 3
                msg['To'] = [pair[0][0], pair[1][0], pair[2][0]]  #access email
                html="""
                    <div style="text-align:center; font-family: 'Courier'; font-size: 15px;">
                        <h2>Hi 👋  I'm the WiCS Buddy Bot 🤖 ! You've got mail 💌</h2>
                        <p>If you're receiving this message, this means you've signed up to meet a new member of WiCS every week : )</p> 
                        <p>Here are your buddies for the week:</p>
                        <ul style="list-style-type:none;">
                            <li>$(partner1)</li>
                            <li>$(partner2)</li>
                            <li>$(partner3)</li>
                        </ul>
                        <p>Please email us if you wish to opt out. Have a great day ⚡️ </p>

                    </div>"""
                html = html.replace("$(partner1)", pair[0][1])
                html = html.replace("$(partner2)", pair[1][1])
                html = html.replace("$(partner3)", pair[2][1])
            else:   
                msg['To'] = [pair[0][0], pair[1][0]]  #access email
                html="""<div style="text-align:center; font-family: 'Courier'; font-size: 15px;">
                        <h2>Hi 👋  I'm the WiCS Buddy Bot 🤖 ! You've got mail 💌</h2>
                        <p>If you're receiving this message, this means you've signed up to meet a new member of WiCS every week : )</p> 
                        <p>Here are your buddies for the week:</p> 
                        <ul style="list-style-type:none;">
                            <li>$(partner1)</li>
                            <li>$(partner2)</li>
                        </ul>
                        <p>Please email us if you wish to opt out. Have a great day ⚡️ </p>

                    </div>"""
                html = html.replace("$(partner1)", pair[0][1])
                html = html.replace("$(partner2)", pair[1][1])

            msg.set_content(html, subtype='html')


            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) 
                smtp.send_message(msg)



    return



buddy_bot()

