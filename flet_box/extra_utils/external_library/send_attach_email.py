import smtplib
import os

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


class send_attach_email:
    """
    Send email with attachmend like [ pdf, imag, word ...]

    ```python
    from .send_attachment_emails import send_attach_email

    email_obj = send_attach_email(
        email_from = '...@gmail.com',
        email_to = '...@gmail.com',
        email_header = 'hi there!!!',
        email_body = 'hello world from dev!!!',
        email_password = '******',
        file_path = '/path/file_name.pdf',
    )
    print('email was sended')
    ```
    """
    def __init__(self,
        email_from: str="",
        email_to: str="",
        email_header: str="",
        email_body: str="",
        email_password: str="",
        file_path: str="",
        ):

        super().__init__()

        # init email sender
        self.email_from=email_from
        self.email_to= email_to
        self.email_header= email_header
        self.email_body= email_body
        self.email_password = email_password
        self.file_path = file_path
        self.filename = os.path.basename(self.file_path)

        self.runing_email_sender()

    def runing_email_sender(self):
        # make init class MIME
        self.msg = MIMEMultipart()
        self.msg['From'] = self.email_from
        self.msg['To'] = self.email_to
        self.msg['Subject'] = self.email_header

        # make a object in binar mode
        self.msg.attach(MIMEText(self.email_body, 'plain'))
        self.attach_file = open(self.file_path,'rb')

        # encode msg
        self.payload = MIMEBase('application', 'octate-stream')
        self.payload.set_payload((self.attach_file).read())
        encoders.encode_base64(self.payload)

        # make header
        self.payload.add_header('content-disposition','attachment',filename=self.filename)
        self.msg.attach(self.payload)

        self.send_email()

    def send_email(self):
        self.session  = smtplib.SMTP(host='smtp.gmail.com',port=587)
        self.session.starttls()
        self.session.login(user=self.email_from, password=self.email_password)
        self.message_to_send = self.msg.as_string()
        self.session.sendmail(from_addr=self.email_from, to_addrs=self.email_to, msg=self.message_to_send)
        self.session.quit()

if __name__ == '__main__':
    send_attach_email(
        email_from = 'justoneclick37@gmail.com',
        email_to = 'kuko53348@gmail.com',
        email_header = 'hi there!!!',
        email_body = 'hello world from dev!!!',
        email_password = 'gpae milb kxlm pdoq',
        file_path = '/media/mjay/Almacen/LINUX_BASIC/PYTHON_PROGRAMNG/FLETBOX_WEB/flet_box/extra_utils/external_library/flet_box_database.db',
    )
    print('email was sended')
