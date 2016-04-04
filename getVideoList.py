import json,urllib2

PLAYLIST=[]
VIDEOLIST=[]
CHANNEL_ID='UCkefXKtInZ9PLsoGRtml2FQ'
API_KEY=''
URL='https://www.googleapis.com/youtube/v3/playlists?'
NEXTPAGE=''

def GetDataFromURL(url):
    data = json.load(urllib2.urlopen(url))
    for item in data['items']:
         PLAYLIST.append(item['snippet']['title']) 
    print len(PLAYLIST)
    try:
       if data['nextPageToken']:
          NEXTPAGE = data['nextPageToken'] 
          GetDataFromURL(URL+'pageToken='+NEXTPAGE+'&part=snippet&channelId='+CHANNEL_ID+'&key='+API_KEY)    
    except KeyError:
          print 'error hai...'
         
if __name__=='__main__':
   GetDataFromURL(URL+'part=snippet&channelId='+CHANNEL_ID+'&key='+API_KEY)
  
