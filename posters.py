from random import choice
from feedparser import parse
from bs4 import BeautifulSoup
import re
from errbot import botcmd, BotPlugin

def get_random_url_from_feed(feed_url):
    feeds = parse(feed_url)['entries']
    html = choice([feed.content[0].value for feed in feeds if len(feed.content) > 0])
    soup = BeautifulSoup(html)
    img = soup.find("img")
    return img['src']

class Posters(BotPlugin):

    @botcmd(template='showme')
    def fixor(self, mess, args):
        """
            There ! I fixed it !
            from http://thereifixedit.files.wordpress.com/
        """
        return {'content':'There I fixed it !', 'url':get_random_url_from_feed('http://feeds.feedburner.com/ThereIFixedIt') + '?t=.jpg'}

    @botcmd(template='showme')
    def wtf(self, mess, args):
        """
        (De)motivates you
        from VeryDemotivational
        """
        return {'content':'Very demotivational !', 'url':get_random_url_from_feed('http://feeds.feedburner.com/VeryDemotivational') + '?t=.jpg'}
