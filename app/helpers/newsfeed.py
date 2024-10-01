import html2text
import feedparser

from datetime import datetime
from bs4 import BeautifulSoup


# Medium RSS feed URL
MEDIUM_RSS_URL = "https://medium.com/feed/@bogdan.sikorsky"


# Fetch RSS data
def fetch_medium_articles():
    h = html2text.HTML2Text()
    h.ignore_links = False  # This will retain the links
    h.bypass_tables = False

    feed = feedparser.parse(MEDIUM_RSS_URL)
    content = ''
    for i, entry in enumerate(feed.entries):
        markdown_text = h.handle(entry.summary)
        soup = BeautifulSoup(markdown_text, "html.parser")
        clean_markdown = soup.get_text()

        clean_date = datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S %Z")
        clean_date = clean_date.strftime("%A, %d %B %Y, %H:%M")

        # Combine title, published, link, and summary into one value
        full_article = (
            f"# {entry.title}\n\n "
            f"Published: _{clean_date}_\n\n "
            f"**[Source: Bogdan Sikorsky]({entry.link})**\n\n "
            f"{clean_markdown}"
        )
        full_article = full_article.split('## Contacts')[0].strip()
        content += full_article
        if i < len(feed.entries) - 1:  # Check if it's not the last article
            content += '\n --- \n'

    return content
