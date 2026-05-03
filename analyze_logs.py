import json
from collections import Counter
from datetime import datetime

failed = 0
success = 0
usernames = []
passwords = []

with open("/home/kali/cowrie/var/log/cowrie/cowrie.json") as f:
    for line in f:
        data = json.loads(line)

        if data.get("eventid") == "cowrie.login.failed":
            failed += 1
            usernames.append(data.get("username"))
            passwords.append(data.get("password"))

        elif data.get("eventid") == "cowrie.login.success":
            success += 1

report = f"""
==== SME SECURITY REPORT ====
Generated on: {datetime.now()}

Total Failed Attempts: {failed}
Total Successful Attempts: {success}

Most Targeted Usernames:
{Counter(usernames)}

Most Used Passwords:
{Counter(passwords)}
"""
print(report)
with open("report.txt", "w") as f:
    f.write(report)
