from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from news_api.models import Story
from dateutil import parser

#general imports
import os
# newsApi imports
from newsapi import NewsApiClient
my_api_key = os.environ.get("API_KEY")
newsapi = NewsApiClient(api_key=my_api_key)
#async imports
from multiprocessing.dummy import Pool as ThreadPool


"""Individual functions for handling API response data"""
def collect_results(articles):
    results = []
    for article in articles:
        headline = article['title']
        source = article["source"]["name"]
        if not article["content"]:  # sometimes Newsapi is unable to provide content for each story
            content = "No content preview found. Click the link above to access the full story."
        else:
            content = article['content']
        author = article['author']
        description = article['description']
        if not description:
            description = "No description."
        url = article['url']
        image = article['urlToImage']
        api_date = article['publishedAt']
        published_at = parser.parse(api_date)
        story = Story(headline=headline, source =source, content_preview=content, author=author, description=description, url=url, image=image, published_at=published_at)
        story.save()
        results.append(story)
    return results





"""Views for different pages of website"""

def index(request):
    return HttpResponse("Hello world. this is the main page of the website")

def test_story(request):
    latest_story = Story.objects.latest('date_added')
    # output = "".join(latest_story)

    return HttpResponse(latest_story)


"""Individual functions for separate types of API Calls"""
def cat_calls(query, slideshow = True):
    """API call to get generalized headlines for a specific catagory"""
    data = newsapi.get_top_headlines(language="en", category=f"{query}")
    articles = data['articles']
    results = collect_results(articles)
    return results

def headlines_call(request):
    """API call to get top headlines for all categories"""
    data = newsapi.get_top_headlines(language="en")
    articles = data['articles']
    print(articles, "0000000")

    results = collect_results(articles)
    serialized_stories = serializers.serialize('json', results)

    return JsonResponse(serialized_stories, safe=False)

def simple_search_call(query):
    """API call to get results from single search query"""
    data = newsapi.get_everything(q=f"{query}")
    articles = data['articles']
    spliced = articles[:10]
    results = collect_results(articles)
    return results

# def advanced_search_call(query):
#     from_ = str(query['date_from'])
#     to = str(query['date_to'])

#     if to == 'None' and from_ == 'None':
#         data = newsapi.get_everything(q=f"{query['keyword']}", sources=f"{query['source']}", language=f"{query['language']}", sort_by=f"{query['sort_by']}"
#                                       )
#     elif to == 'None' and from_ != 'None':
#         data = newsapi.get_everything(q=f"{query['keyword']}", sources=f"{query['source']}", language=f"{query['language']}", sort_by=f"{query['sort_by']}", from_param=f"{from_}"
#                                       )
#     elif to != 'None' and from_ == 'None':
#         data = newsapi.get_everything(q=f"{query['keyword']}", sources=f"{query['source']}", language=f"{query['language']}", sort_by=f"{query['sort_by']}", to=f"{to}"
#                                       )
#     else:
#         data = newsapi.get_everything(q=f"{query['keyword']}", sources=f"{query['source']}", language=f"{query['language']}", sort_by=f"{query['sort_by']}", from_param=f"{from_}", to=f"{to}"
#                                       )
#     # api seems to not want to allow dates to be optional if specified
#     # I ran into trouble with the pagesize parameter from news-api, however a
#     # temporary solution to this is to extract that number from the query dict,
#     # and then splice the resulting list of articles.
#     quantity = int(query['quantity'])
#     articles = data['articles']
#     spliced = articles[:quantity]
#     saved = save_to_session(spliced)
#     return saved


# """Executes Asyncronous API requests for cat_calls"""
# def async_reqs(query):
#     pool = ThreadPool(10)
#     results = pool.map(cat_calls, query)
#     pool.close()
#     pool.join()
#     return results