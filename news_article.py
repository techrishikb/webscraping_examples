from newspaper import Article
import pdfkit

# Define the URL of the article or web page you want to scrape
url = "https://tech.hindustantimes.com/tech/news/sony-reveals-the-world-s-first-full-frame-mirrorless-4k-camera-story-mIePzcd2wKnTb3ZRXVRELI.html"

# Create an Article object and download/parse the article
article = Article(url)
article.download()
article.parse()

# Define the output PDF file name
output_pdf_file = "article.pdf"

# Create a string with HTML line breaks to format the content, title, URL, and description
pdf_content = f"<br><b>Title:</b><br>{article.title}<br><br><b>URL:</b><br>{url}<br><br><b>Content:</b><br>{article.text}"

# Convert the HTML content to a PDF file
pdfkit.from_string(pdf_content, output_pdf_file, options={'page-size': 'A4'})

print(f"Article content has been saved to {output_pdf_file}")
