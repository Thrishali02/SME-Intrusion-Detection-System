import matplotlib.pyplot as plt
from collections import Counter
import json
usernames = []

with open("/home/kali/cowrie/var/log/cowrie/cowrie.json") as f:
    for line in f:
        data = json.loads(line)
        if data.get("eventid") == "cowrie.login.failed":
            usernames.append(data.get("username"))

counts = Counter(usernames)

plt.bar(counts.keys(), counts.values())
plt.xlabel("Usernames")
plt.ylabel("Attempts")
plt.title("Intrusion Attempts by Username")

plt.savefig("username_chart.png")
plt.show()
