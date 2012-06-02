import requests
import simplejson as json
from BeautifulSoup import BeautifulSoup


def arbor_api_wikipedia_query(name):
    params = dict(
        action="query",
        list="search",
        srsearch=name,
        srnamespace=6,
        srlimit=10,
        srprop="score|size",
        format="json",
    )
    try:
        response = requests.get("http://commons.wikimedia.org/w/api.php",
            params=params,
            timeout=15.,)
    except:
        return
    data = json.loads(response.content)
    photos = data['query']['search']
    img = requests.get('http://toolserver.org/~magnus/commonsapi.php',
        params={'image':photos[0]['title'].split(':')[-1], 'thumbwidth':300},
        timeout=10.,)
    xml = BeautifulSoup(img.content)
    #import pdb;pdb.set_trace()
    thumb = xml.findAll('thumbnail')[0].text
    big = xml.findAll('file')[1].text
    return img.content
