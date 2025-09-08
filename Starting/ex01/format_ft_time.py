from datetime import datetime

now = datetime.now()
years_ago = datetime(1970, 1, 1)

since = now - years_ago
seconds_since = since.total_seconds()

print(f"Seconds since {years_ago.strftime("%B %d, %Y")}: {"{:,.3f}".format(seconds_since)} or {"{:,.2e}".format(seconds_since)} in scientific notation")
print(now.strftime("%b %d %Y"))