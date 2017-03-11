import time 
import requests
import operator

_url = 'https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize'
_key = 'passCode' 
_maxNumRetries = 10

def processRequest( json, data, headers, params ):
    retries = 0
    result = None

    while True:

        response = requests.request( 'post', _url, json = json, data = data, headers = headers, params = params )

        if response.status_code == 429: 

            print( "Message: %s" % ( response.json()['error']['message'] ) )

            if retries <= _maxNumRetries: 
                time.sleep(1) 
                retries += 1
                continue
            else: 
                print( 'Error: failed after retrying!' )
                break

        elif response.status_code == 200 or response.status_code == 201:

            if 'content-length' in response.headers and int(response.headers['content-length']) == 0: 
                result = None 
            elif 'content-type' in response.headers and isinstance(response.headers['content-type'], str): 
                if 'application/json' in response.headers['content-type'].lower(): 
                    result = response.json() if response.content else None 
                elif 'image' in response.headers['content-type'].lower(): 
                    result = response.content
        else:
            print( "Error code: %d" % ( response.status_code ) )
            print( "Message: %s" % ( response.json()['error']['message'] ) )

        break
        
    return result

t = int(raw_input())
for _ in range(t):
    urlImage = raw_input()

    headers = dict()
    headers['Ocp-Apim-Subscription-Key'] = _key
    headers['Content-Type'] = 'application/json' 

    json = { 'url': urlImage } 
    data = None
    params = None

    result = processRequest( json, data, headers, params )
    currEmotion = ""
    for currFace in result:
        currEmotion = max(currFace['scores'].items(), key=operator.itemgetter(1))[0]
        print(currEmotion)
        break