from random import choice
from errbot import botcmd, BotPlugin


from imageBot import extract_rss_urls
from urllib2 import quote, urlopen

def ensure_image_url(url, types=['.png', 'gif', 'jpg', 'jpeg']):
    lower_url = url.lower()
    if any([img_type in lower_url for img_type in types]):
        return lower_url
    else:
        return "{0}?{1}".format(url, 't=.png')



class Cartoons(BotPlugin):
    @botcmd(template='showme')
    def dilbert(self, mess, args):
        """ by Scott Adams
        http://www.dilbert.com/ 
        """
        urls = extract_rss_urls('http://feed.dilbert.com/dilbert/most_popular?format=xml')
        urls.extend(extract_rss_urls('http://feed.dilbert.com/dilbert/daily_strip?format=xml'))
        return {'content':'Random Dilbert', 'url':ensure_image_url(choice(urls))}

    @botcmd(template='showme')
    def xkcd(self, mess, args):
        """
        Display random XKCD from RSS feed from http://xkcd.com
        """
        urls = extract_rss_urls('http://xkcd.com/rss.xml')
        return {'content':'Random XKCD', 'url':ensure_image_url(choice(urls))}

    @botcmd
    def shout(self, mess, args):
        """
        Display the queried ascii art
        """
        args=args.strip()
        if not args:
            return 'What can I shout for you ?'
        return urlopen('http://asciime.heroku.com/generate_ascii?s=%s'%quote(args)).read()
