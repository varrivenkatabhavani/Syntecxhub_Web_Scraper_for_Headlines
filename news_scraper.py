import requests
from bs4 import BeautifulSoup
import csv

# Website URL
url = "https://news.ycombinator.com/"

try:
    # Get webpage content
    response = requests.get(url)

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Find headlines
    headlines = soup.find_all("span", class_="titleline")

    # Create CSV file
    with open("headlines.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Column heading
        writer.writerow(["Headlines"])

        print("Top Headlines:\n")

        # Write headlines
        for h in headlines:
            title = h.get_text()
            print(title)
            writer.writerow([title])

    print("\nHeadlines saved to headlines.csv")

except Exception as e:
    print("Error:", e)