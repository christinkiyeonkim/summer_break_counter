from datetime import datetime

# 📅 Last working day
last_day = datetime.strptime("2025-05-29", "%Y-%m-%d")
today = datetime.today()

# ⏳ Days left
days_left = (last_day - today).days

# 📣 Output
if days_left > 0:
    print(
        f"🏫 Still {days_left} day(s) left until your last day at the Latin School of Chicago!"
    )
    print("☀️ Hang in there — summer break is coming!")
elif days_left == 0:
    print(
        "🎉 TODAY is your LAST DAY at the Latin School of Chicago! Hello, summer break!! 🌴"
    )
else:
    print(f"🍹 You've been on summer break for {abs(days_left)} day(s) now! 😎")
