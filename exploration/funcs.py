import urllib.request
import time
import feedparser

from pymongo import MongoClient

class dump_from_arXiv():
    """
    python_arXiv_paging_example.py

    This script dumps metadata from arxiv API and stores it
    in a mongodb database. There is a 3 seconds wait between api calls.

    Please see the documentation at 
    http://export.arxiv.org/api_help/docs/user-manual.html
    for more information, or email the arXiv api 
    mailing list at arxiv-api@googlegroups.com.
    """

    def __init__(self):
        # Base api query url
        self.base_url = 'http://export.arxiv.org/api/query?';

        # initiating mongo db
        client = MongoClient('localhost:27017')
        self.db = client.arXivDB

    def search_and_dump(self,
                        search_query='cat:quant-ph',
                        start=0,
                        results_per_iteration=2000,
                        wait_time=3):

        # fetching the total number of results
        query = 'search_query=%s&start=%i&max_results=%i' % (search_query, 0, 1)
        response = urllib.request.urlopen(self.base_url+query).read()
        feed = feedparser.parse(response)
        total_results = int(feed.feed.opensearch_totalresults)

        print('Searching arXiv for {}'.format(search_query))
        print('Found a total of {} entries'.format(total_results))

        for i in range(start,total_results,results_per_iteration):
            
            print("Results {} to {}".format(i, i+results_per_iteration))
            
            query = 'search_query=%s&start=%i&max_results=%i' % (search_query,
                                                                 i,
                                                                 results_per_iteration)

            # perform a GET request using the base_url and query
            response = urllib.request.urlopen(self.base_url+query).read()

            # parse the response using feedparser
            feed = feedparser.parse(response)
            print('This feed contains {} entries'.format(len(feed.entries)))

            # dumping the entries into mongo db
            self.db.arXivfeeds.insert_many(feed.entries)
            
            # playing nice and sleeping a bit before next call
            # to the api again!
            print('Sleeping for %i seconds' % wait_time) 
            time.sleep(wait_time)

        print('download and dump done!')
        