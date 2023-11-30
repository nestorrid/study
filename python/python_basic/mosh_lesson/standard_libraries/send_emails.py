# -*- coding=utf-8 -*-
#
# @Project      : python_basic
# @Author       : nestor
# @File         : send_emails.py
# @Date         : 2023/11/5 19:21
#
# @Description  :
#
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from pathlib import Path
from string import Template

template = Template(Path("mail_template.html").read_text())

mail = MIMEMultipart()

mail["from"] = "***"
mail["to"] = "***"
mail["subject"] = "Test python email"
mail.attach(MIMEText(template.substitute({"name": "handsome"}), "html"))

with smtplib.SMTP(host="smtp.exmail.qq.com", port=25) as smtp:
    # with smtplib.SMTP(host="smtp.163.com", port=25) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("***", "***")
    smtp.send_message(mail)
    print("sent")
