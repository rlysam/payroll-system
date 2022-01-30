import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ! WARNING: Call the generate payslip FIRST before calling this functions
def sendPaySlipToEmployeeEmail(recipientEmail, employeeName):

	password = '6&vFK3JxgNzK2H*N'
	sender_email = 'infosec123dummy@gmail.com'
	receiver_email = recipientEmail # Enter receiver address
	# receiver_email = "bellosamuelb@gmail.com"  # Enter receiver address
	# receiver_email = "aprilkatepascual23@gmail.com"  # Enter receiver address
	company_name = 'SGV Co./EY Philippines'

	subject = "An email with attachment from " + company_name
	body = "This is an email with attachment sent from Python of your receipt"

	# Create a multipart message and set headers
	message = MIMEMultipart()
	message["From"] = sender_email
	message["To"] = receiver_email
	message["Subject"] = subject
	message["Bcc"] = receiver_email  # Recommended for mass emails

	# Add body to email
	message.attach(MIMEText(body, "plain"))

	# filename = "functions/email/"+employeeName+".pdf"  # In same directory as script
	filename = employeeName+"_PAYSLIP"+".pdf"  # In same directory as script
	# filename = 'PAYSLIP.pdf'
	# Open PDF file in binary mode
	with open(filename, "rb") as attachment:
		# Add file as application/octet-stream
		# Email client can usually download this automatically as attachment
		part = MIMEBase("application", "octet-stream")
		part.set_payload(attachment.read())

	# Encode file in ASCII characters to send by email    
	encoders.encode_base64(part)

	# Add header as key/value pair to attachment part
	part.add_header(
		"Content-Disposition",
		f"attachment; filename= {filename}",
	)

	# Add attachment to message and convert message to string
	message.attach(part)
	text = message.as_string()

# Log in to server using secure context and send email
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, text)

# sendPaySlipToEmployeeEmail('sam17.bello@ymail.com')