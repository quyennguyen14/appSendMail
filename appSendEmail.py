from model.dbModel import getData
from Ultils import Log, smtpSendMail
import pandas as pd
from Ultils.smtpSendMail import smtpSendEmail
from config import config
from pretty_html_table import build_table

def appSendEmail():
    #Get data from DATABASE
    dataClass = getData(filename='config/config.ini', section='mssql')
    dfResult = dataClass.SP_Articles_getInfo_byArticleId_Pandas(articleId='7002D1C3-A813-46D7-8CA2-12CDD8A54EB8')

    # get email information in config file
    emailConfig = config.config()
    emailInfo = emailConfig.emailConfig(filename='config/config.ini', section='emailconfig')
    smtpHost = emailInfo['smtp']
    senderEmail = emailInfo['senderEmail']
    senderPass = emailInfo['senderPass']
    receivers = emailInfo['recieveEmail'].split(',')

    # send email
    html_body = f"""
                <html>
                <body>
                <p><h1> Hi, This is content in email </h1> <br>
                <h1 style="color: #5e9ca0;">Báo cáo bán hàng thương mại </h1> <br>
                {build_table(dfResult, 'blue_light')}
                </p>
                </body>
                </html>
                """

    smtpSendEmail(host=smtpHost,
            sender_email=senderEmail,
            sender_password=senderPass,
            receiver_email=receivers,
            subject='Test Email',
            html_body=html_body)

appSendEmail()
