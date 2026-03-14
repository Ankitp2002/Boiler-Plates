from langchain.tools import Tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import WikipediaQueryRun
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

search = DuckDuckGoSearchRun()
wiki = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

def read_webpage(url):
    """Read webpage content with BeautifulSoup."""
    try:
        resp = requests.get(url, timeout=10)
        soup = BeautifulSoup(resp.content, 'html.parser')
        # Remove script/style
        for script in soup(["script", "style", "nav", "footer"]):
            script.decompose()
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        return ' '.join(chunk for chunk in chunks if chunk)
    except:
        return "Failed to read page"

web_reader = Tool(
    name="web_reader",
    description="Reads full content from any URL. Use AFTER search tools find good links.",
    func=read_webpage
)

TOOLS = [search, wiki, web_reader]
