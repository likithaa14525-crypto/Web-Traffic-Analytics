import pandas as pd

df = pd.read_csv("data.csv")

# Basic Metrics
page_views = df["page"].value_counts()
avg_session = df["session_time"].mean()
drop_off = (df["exit"] == "Yes").mean() * 100

print("=== WEB TRAFFIC ANALYTICS ===\n")

print("Page Views:")
print(page_views)

print("\nAverage Session Time:", avg_session)
print("Drop-off Rate:", drop_off, "%")

print("\nINSIGHTS:")
print("- Home page is most visited")
print("- Improve Checkout page UX")
print("- Reduce drop-off rate after About page")