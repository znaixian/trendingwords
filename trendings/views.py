from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import pandas as pd
# import matplotlib
from pytrends.request import TrendReq

pytrend = TrendReq()

# df.reset_index().plot(x='geoName', y='COVID', figsize=(120, 10), kind ='bar')

# print(df.head(100))
# df = pytrend.today_searches(pn='US')
# print(df.head())
# # # Get Google Top Charts
# # Related Queries, returns a dictionary of dataframes


def index(request):
    dt_html = {}
    error_dict = {}

    if request.method == 'POST':
        # pytrend.build_payload(kw_list=['COVID'])
        # Interest by Region
        # dfr = pytrend.interest_by_region()
        # print(dfr.head(10))
        # dt_html = dfr.to_html(index=False)
        country = request.POST['country']
        print(country)
        # Get Google Hot Trends data
        dfr = pytrend.trending_searches(pn='united_states')
        dfa = pytrend.trending_searches(pn=country)
        dfb = pd.concat([dfr, dfa], axis=1)
        dfb.columns = ['United States', country]
        dt_html = dfb.to_html(index=False)

        # # Related Topics, returns a dictionary of dataframes
        # pytrend.build_payload(kw_list=['Coronavirus'])
        # related_queries = pytrend.related_queries()
        # print(type(related_queries.values()))
        # related_topic = pytrend.related_topics()
        # print(related_topic.values())
        # df = pytrend.top_charts(2019, hl='en-US', tz=300, geo='GLOBAL')
        # print(df.head())

    else:
        dt_html = {}
        error_dict['error'] = "Please check!"

    return render(request, 'index.html', {'dt_html': dt_html, 'error_dict': error_dict})

# def index(request):
    # return HttpResponse("Hello, world. You're at the trending index.")
