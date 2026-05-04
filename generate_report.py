from reportlab.platypus import Image
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
import json
from collections import Counter
doc = SimpleDocTemplate("SME_Security_Report.pdf")
styles = getSampleStyleSheet()
elements = []
elements.append(Paragraph("SME Cybersecurity Report", styles['Title']))
elements.append(Spacer(1, 10))
elements.append(Paragraph(f"Generated on: {datetime.now()}", styles['Normal']))
elements.append(Spacer(1, 10))
failed = 0
success = 0
usernames = []
passwords = []
sample_records = []
with open("/home/kali/cowrie/var/log/cowrie/cowrie.json") as f:
    for line in f:
        data = json.loads(line)

        if data.get("eventid") == "cowrie.login.failed":
            failed += 1
            usernames.append(data.get("username"))
            passwords.append(data.get("password"))

        elif data.get("eventid") == "cowrie.login.success":
            success += 1
        if data.get("eventid") == "cowrie.login.failed" or data.get("eventid") == "cowrie.login.success":
            if len(sample_records) < 5:
                sample_records.append({
                    "ip": data.get("src_ip"),
                    "time": data.get("timestamp"),
                    "session": data.get("session"),
                    "username": data.get("username"),
                    "password": data.get("password"),
                    "status": "SUCCESS" if data.get("eventid") == "cowrie.login.success" else "FAILED"
                })
elements.append(Paragraph("1. Authentication Summary", styles['Heading2']))
elements.append(Spacer(1, 10))
elements.append(Paragraph(f"Failed Attempts: {failed}", styles['Normal']))
elements.append(Paragraph(f"Successful Attempts: {success}", styles['Normal']))
elements.append(Spacer(1, 10))
elements.append(Paragraph(f"Top Usernames: {Counter(usernames)}", styles['Normal']))
elements.append(Paragraph(f"Top Passwords: {Counter(passwords)}", styles['Normal']))
elements.append(Spacer(1, 20))
total_attempts = failed + success

if total_attempts > 50:
    risk = "HIGH"
elif total_attempts > 20:
    risk = "MEDIUM"
else:
    risk = "LOW"

elements.append(Paragraph("2. Risk Assessment", styles['Heading2']))
elements.append(Spacer(1, 10))
elements.append(Paragraph(f"Risk Level: {risk}", styles['Normal']))
elements.append(Spacer(1, 20))
elements.append(Paragraph("2. Detailed Attack Records (Sample)", styles['Heading2']))
elements.append(Spacer(1, 10))
for r in sample_records:
    elements.append(Paragraph(f"IP Address: {r['ip']}", styles['Normal']))
    elements.append(Paragraph(f"Timestamp: {r['time']}", styles['Normal']))
    elements.append(Paragraph(f"Session ID: {r['session']}", styles['Normal']))
    elements.append(Paragraph(f"Username: {r['username']}", styles['Normal']))
    elements.append(Paragraph(f"Password: {r['password']}", styles['Normal']))
    elements.append(Paragraph(f"Status: {r['status']}", styles['Normal']))
    elements.append(Spacer(1, 10))

elements.append(Paragraph("3. Attack Visualization", styles['Heading2']))
elements.append(Spacer(1, 10))

elements.append(Image("username_chart.png", width=400, height=200))
elements.append(Spacer(1, 20))
elements.append(Paragraph("4. Recommendations", styles['Heading2']))
elements.append(Spacer(1, 10))

elements.append(Paragraph("• Avoid common usernames such as 'root' or 'admin'", styles['Normal']))
elements.append(Paragraph("• Use strong and unique passwords", styles['Normal']))
elements.append(Paragraph("• Regularly monitor login activity", styles['Normal']))
elements.append(Paragraph("• Enable additional security measures where possible", styles['Normal']))
elements.append(Spacer(1, 20))
doc.build(elements)
