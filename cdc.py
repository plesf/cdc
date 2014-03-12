import requests
import json


def search(query='', language='', media_type='', _max = ''):
    payload = {'q' : query,
               'language' : language,
               'mediatype' : media_type,
               'max' : _max,
               }
    results = []
    endpoint = 'http://tools.cdc.gov/api/v1/resources/media'
    response = requests.get(endpoint, params=payload)
    if response.status_code == 200:
        raw_json = json.loads(response.text)
        search_results = raw_json['results']
        for result in search_results:
            results.append({'title' : result['title'],
                            'language' : result['language'],
                            'mediatype' : result['mediaType'],
                            'target_url' : result['targetUrl'],
                            })
    import pdb; pdb.set_trace()
    return results


if __name__ == '__main__':
    print search(query='cancer', language='English', media_type='Video', _max = 40)
