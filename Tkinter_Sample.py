import pandas as pd
import smtplib
from email.message import EmailMessage

df = pd.read_csv("sec_bhavdata_full_23112021.csv",skipinitialspace = True)
df.replace("-","",inplace=True)
df["CHANGE"] = df["CLOSE_PRICE"]-df["PREV_CLOSE"]
df["DELIV_PER"]=pd.to_numeric(df["DELIV_PER"])
data=df["SYMBOL"][(df.CHANGE > 0)]
#data = df["CHANGE"]
#print("The below Scrips are Positive Since Yesterday : "data)
print(data)
ndf = pd.DataFrame(data)
#ndf.sort_values(by='CHANGE')#, ascending=True
ndf.to_csv('Todays_Postive_Stocks.csv')
#print(Sorted_ndf)

#server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
#server.login("udeshjuseja88@gmail.com","Satnam@19su")
#server.sendmail("udeshjuseja88@gmail.com","udeshjuseja@gmail.com","Postive Stocks fot today -- Automated Email - Udesh ")
#server.sendmail("udeshjuseja88@gmail.com","nitinjuseja@gmail.com","Postive Stocks fot today -- Automated Email - Udesh ")
#server.sendmail("udeshjuseja88@gmail.com","animeshtiwari2323@gmail.com","Postive Stocks fot today -- Automated Email - Udesh ")
msg = EmailMessage()
msg['Subject'] = 'Automated_Mail_CSV_FILE_ATTACHED For Postive Stocks Today -- Udesh'
msg['From'] = 'udeshjuseja88@gmail.com'
msg['To'] = 'udeshjuseja@gmail.com'
msg.set_content('Following Stocks Enclosed in attached CSV File have closedhigher than yesrterday.Thus, being positive')
#msg['To'] = 'nitinjuseja@gmail.com'
#msg['To'] = 'animeshtiwari2323@gmail.com'
#msg['To'] = 'jainvikas013@gmail.com'

with open('Todays_Postive_Stocks.csv', 'rb') as file1 :
    file_data = file1.read()
    file_name = file1.name
msg.add_attachment(file_data, maintype = 'csv',subtype = 'csv',filename = file_name)

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("udeshjuseja88@gmail.com","Satnam@19su")
server.send_message(msg)


server.quit()

