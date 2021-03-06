
import smtplib
from email.message import EmailMessage

#email configuration
EMAIL_ADDRESS = 'OMIT'
EMAIL_PASSWORD = 'OMIT' #app password, exclude from github

def no_buddy(buddy, msg):
    #content of email  
    msg['To'] = buddy[0]  #access email
    html="""<div style="text-align:center; font-family: 'Courier'; font-size: 15px;">
            <h2>Hi $(partner1) π  I'm the WiCS Buddy Bot π€ ! You've got mail π</h2>
            <p>If you're receiving this message, this means you've signed up to meet other members of WiCS βΊοΈ </p> 
            <p>Take a break this week and treat yourself to some me-time! You will receive a WiCS buddy the following week. </p> 
            <p>Have a great day β‘οΈ </p>

        </div>"""
    html = html.replace("$(partner1)", buddy[1])
    msg.set_content(html, subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) 
        smtp.send_message(msg)

    
def main(pairs):

    for pair in pairs: 
        msg = EmailMessage() #instantiate email message class to send email
        msg['Subject'] = 'WiCS Buddy Bot Pair!'
        msg['From'] = EMAIL_ADDRESS
        
        #content of email  
        #access email at pair[whatever person they are, 1 or 0][0]
        if pair[1][0] == '0':
            print(pair[0][1] + " does not have a buddy")
            no_buddy(pair[0], msg)
        elif pair[0][0] == '0':
            print(pair[1][1] + " does not have a buddy")
            no_buddy(pair[1], msg)            
        else:
            #content of email  
            msg['To'] = [pair[0][0], pair[1][0]]  #access email
            html="""<div style="text-align:center; font-family: 'Courier'; font-size: 15px;">
                    <h2>Hi π  I'm the WiCS Buddy Bot π€ ! You've got mail π</h2>
                    <p>If you're receiving this message, this means you've signed up to meet other members of WiCS βΊοΈ </p> 
                    <p>Here is your buddy pod for the week:</p> 
                    <ul style="list-style-type:none;">
                        <li>$(partner1)</li>
                        <li>$(partner2)</li>
                    </ul>
                    <p>Please contact them via email. Have a great day β‘οΈ </p>

                </div>"""
            html = html.replace("$(partner1)", pair[0][1])
            html = html.replace("$(partner2)", pair[1][1])

            msg.set_content(html, subtype='html')


            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) 
                smtp.send_message(msg)

    return



