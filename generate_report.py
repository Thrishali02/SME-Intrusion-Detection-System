from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
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
ips = []

with open("/home/kali/cowrie/var/log/cowrie/cowrie.json") as f:
    for line in f:
        data = json.loads(line)

        if data.get("src_ip"):
            ips.append(data.get("src_ip"))

        if data.get("eventid") == "cowrie.login.failed":
            failed += 1
            usernames.append(data.get("username"))
            passwords.append(data.get("password"))

        elif data.get("eventid") == "cowrie.login.success":
            success += 1
elements.append(Paragraph("1. Connection & Identification Data", styles['Heading2']))
elements.append(Paragraph(f"Source IPs: {set(ips)}", styles['Normal']))
elements.append(Paragraph(f"Total Sessions Observed: {len(ips)}", styles['Normal']))
elements.append(Spacer(1, 10))
elements.append(Paragraph("2. Authentication Activity", styles['Heading2']))
elements.append(Paragraph(f"Failed Attempts: {failed}", styles['Normal']))
elements.append(Paragraph(f"Successful Attempts: {success}", styles['Normal']))
elements.append(Paragraph(f"Usernames Tried: {Counter(usernames)}", styles['Normal']))
elements.append(Paragraph(f"Passwords Tried: {Counter(passwords)}", styles['Normal']))
elements.append(Spacer(1, 10))
elements.append(Paragraph("3. Behavioral Indicators", styles['Heading2']))
elements.append(Paragraph("Attack Type: Brute-force / Dictionary Attack", styles['Normal']))
elements.append(Spacer(1, 10))
elements.append(Paragraph("4. Analytical Summary", styles['Heading2']))
elements.append(Paragraph("The system detected repeated login attempts using common credentials.", styles['Normal']))
elements.append(Spacer(1, 10))
try:
    elements.append(Image("username_chart.png", width=400, height=200))
except:
    elements.append(Paragraph("Graph not available", styles['Normal']))

elements.append(Spacer(1, 10))
elements.append(Paragraph("5. Recommendations", styles['Heading2']))

if failed + success > 30:
    risk = "HIGH"
elif failed + success > 10:
    risk = "MEDIUM"
else:
    risk = "LOW"

elements.append(Paragraph(f"Risk Level: {risk}", styles['Normal']))
elements.append(Paragraph("• Avoid using default usernames like 'root'", styles['Normal']))
elements.append(Paragraph("• Use strong passwords", styles['Normal']))
elements.append(Paragraph("• Monitor login activity regularly", styles['Normal']))

doc.build(elements)
