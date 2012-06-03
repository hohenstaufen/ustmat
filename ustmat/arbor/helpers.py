import requests
import simplejson as json
from BeautifulSoup import BeautifulSoup
from arbor.models import Shape, Image
from django.core.files.base import ContentFile
from django.db.utils import DatabaseError

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

        data = json.loads(response.content)

        if data and data.get('query'):
            photos = data['query']['search']

            img = requests.get('http://toolserver.org/~magnus/commonsapi.php',
                params={'image':photos[0]['title'].split(':')[-1], 'thumbwidth':300},
                timeout=10.,)
            xml = BeautifulSoup(img.content)
            #import pdb;pdb.set_trace()
            thumb = xml.findAll('thumbnail')[0].text
            big = xml.findAll('file')[1].text
            return thumb, big, requests.get(thumb).content
        else:
            return 0, 0, 0
    except:
        return 0, 0, 0


def bananas():
    banana_trees = Shape.objects.values('botanical').distinct()
    try:
        f = open('asd.txt', 'a')
        for banana in banana_trees:
            #import pdb;pdb.set_trace()
            name = banana['botanical']
            if banana is not None and name is not None:
                cocco, anguria, alessandra = arbor_api_wikipedia_query(name)
                if cocco is not 0:
                    ext = '.'+ cocco.split('.')[-1]
                    img = Image()
                    img.file.save(name+ ext, ContentFile(alessandra))
                    img.small_url = cocco
                    img.big_url = anguria
                    for bongos in Shape.objects.filter(botanical=name):
                        img.botanical.add(bongos)
                    img.save()
                else:
                    f.write(name+'\n')
        f.close()
    except DatabaseError, e:
        print e
        pass

