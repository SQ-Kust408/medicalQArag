from serpapi import GoogleSearch
from config import SERPAPI_API_KEY, SEARCH_RESULT_NUM

# 初始化搜索客户端
def serpapi_search(query):
    params = {
        "q": query,
        "api_key": SERPAPI_API_KEY,
        "engine": "google",
        "location": "Austin,Texas,United States",
        "hl": "en",
        "gl": "us",
        "num": SEARCH_RESULT_NUM
    }
    search = GoogleSearch(params)
    return search.get_dict()