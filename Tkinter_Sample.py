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


msg = EmailMessage()
msg['Subject'] = 'Automated_Mail_CSV_FILE_ATTACHED For Postive Stocks Today -- Udesh'
msg['From'] = 'xxx@gmail.com'
msg['To'] = 'xxx@gmail.com'
msg.set_content('Following Stocks Enclosed in attached CSV File have closedhigher than yesrterday.Thus, being positive')


with open('Todays_Postive_Stocks.csv', 'rb') as file1 :
    file_data = file1.read()
    file_name = file1.name
msg.add_attachment(file_data, maintype = 'csv',subtype = 'csv',filename = file_name)

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("xxx@gmail.com","pass")
server.send_message(msg)


server.quit()

