import requests
import json
from newspaper import Article
from fpdf import FPDF

# Define the API endpoint and payload
url = "https://google.serper.dev/news"
payload = json.dumps({
  "q": "cricket",
  "gl": "in"
})
headers = {
  'X-API-KEY': '******************************************',##replace with your own api key
  'Content-Type': 'application/json'
}

# Send a POST request to the API
response = requests.request("POST", url, headers=headers, data=payload)
data = json.loads(response.text)

# Extract the top 10 URLs, titles, and sources from the response
articles = [(item['title'], item['link'], item['source']) for item in data['news'][:10]]

# Create a PDF document
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)

# Loop through the top articles and extract content
for index, (title, url, source) in enumerate(articles, start=1):
    article = Article(url)
    article.download()
    article.parse()

    # Add the article title, source, URL, and content to the PDF
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt=f"Article {index}", ln=True, align='C')
    pdf.set_font("Arial", size=12)
    
    pdf.multi_cell(0, 10, txt=f"Title: {title}", align='L')
    pdf.multi_cell(0, 10, txt=f"Source: {source}", align='L')
    pdf.multi_cell(0, 10, txt=f"URL: {url}", align='L')
    
    # Encode the content as UTF-8 to handle non-latin-1 characters
    pdf.multi_cell(0, 10, txt=article.text.encode('utf-8').decode('latin-1'), align='L')

# Save the PDF to a file
pdf.output("cricket_news.pdf")
