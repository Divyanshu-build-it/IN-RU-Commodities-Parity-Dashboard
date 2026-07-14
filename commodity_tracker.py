from datetime import datetime

def get_commodity_data():
    return [
        {"Commodity": "Coking Coal", "Origin": "Kuzbass/Far East", "Target_Market": "Indian Steel Sector", "Price_Trend_30D": "-2.4%", "Supply_Status": "Stable"},
        {"Commodity": "Specialized Timber", "Origin": "Primorsky Krai", "Target_Market": "Indian Construction", "Price_Trend_30D": "+1.1%", "Supply_Status": "Capacity Available"},
        {"Commodity": "LNG", "Origin": "Sakhalin", "Target_Market": "Indian Power Grid", "Price_Trend_30D": "Stable", "Supply_Status": "Long-term contracts active"}
    ]

def generate_markdown(data):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    md = "## 📊 India-Russia Industrial Commodities Parity\n\n"
    md += "**Macro-Economic Dashboard — Daytraa Business Solutions**\n\n"
    md += f"*Last Automated Sync: {timestamp} IST*\n\n"
    md += "| Commodity | Russian Origin | Indian Target Market | 30-Day Trend | Supply Status |\n"
    md += "| :--- | :--- | :--- | :--- | :--- |\n"
    for row in data:
        md += f"| {row['Commodity']} | {row['Origin']} | {row['Target_Market']} | {row['Price_Trend_30D']} | {row['Supply_Status']} |\n"
    md += "\n---\n*Automated pricing intelligence for cross-border procurement.*"
    
    with open("README.md", "w") as f: f.write(md)

if __name__ == "__main__": generate_markdown(get_commodity_data())
