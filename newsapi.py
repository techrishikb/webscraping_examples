import json
import requests
from newspaper import Article
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def get_news_urls(topic, date, api_key):
    search_url = f"https://newsapi.org/v2/everything?q={topic}&from={date}&sortBy=publishedAt&apiKey={api_key}"
    response = requests.get(search_url)

    if response.status_code == 200:
        articles = response.json().get("articles", [])
        urls = [article.get("url") for article in articles]
        return urls
    else:
        raise Exception(f"Failed to get news articles: {response.status_code}")

def extract_news_content(url_list):
    content_dict = {}

    for url in url_list:
        try:
            article = Article(url)
            article.download()
            article.parse()
            content_dict[url] = {
                "title": article.title,
                "text": article.text
            }
        except Exception as e:
            print(f"Error processing URL {url}: {e}")

    return content_dict

def create_pdf(content_dict):
    pdf_file = "news_report_football.pdf"
    doc = SimpleDocTemplate(pdf_file, pagesize=letter)
    styles = getSampleStyleSheet()

    story = []
    for url, content in content_dict.items():
        story.append(Paragraph(f"<b>URL:</b> {url}", styles["Normal"]))
        story.append(Paragraph(f"<b>Title:</b> {content['title']}", styles["Normal"]))
        story.append(Paragraph(f"<b>Text:</b> {content['text']}", styles["Normal"]))
        story.append(Paragraph("=" * 50, styles["Normal"]))
    
    doc.build(story)

if __name__ == "__main__":
    topic = "football"
    date = "2023-11-02"
    api_key = "6927e73692f54d049c3761029cbf88a3"  # Replace with your actual API key

    urls = get_news_urls(topic, date, api_key)
    news_content = extract_news_content(urls)

    for url, content in news_content.items():
        print("URL:", url)
        print("Title:", content["title"])
        print("Text:", content["text"])
        print("=" * 50)
    
    create_pdf(news_content)
    print("PDF report generated.")
