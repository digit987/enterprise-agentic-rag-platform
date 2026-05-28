from tavily import TavilyClient

from app.core.config import settings


client = TavilyClient(
    api_key=settings.TAVILY_API_KEY
)


def web_search_tool(query: str):

    response = client.search(
        query=query,
        search_depth="basic",
        max_results=5
    )

    results = []

    for item in response["results"]:

        results.append({
            "title": item["title"],
            "content": item["content"],
            "url": item["url"]
        })

    return results