import sys,json,urllib2,download,os
import urlparse
PLAYLIST={}
VIDEOLIST={}
CHANNEL_ID=''
API_KEY='AIzaSyCCxkwVyeibZFnIRdpclyxr5FMTGlxHztg'
URL='https://www.googleapis.com/youtube/v3/playlists?'
URL_playlist='https://www.googleapis.com/youtube/v3/playlistItems?'
NEXTPAGE=''

def GetPlayListFromURL(url):
    data = json.load(urllib2.urlopen(url))
    for item in data['items']:
         PLAYLIST[item['id']] =  item['snippet']['title']
    
    #print (PLAYLIST)
    try:
       if data['nextPageToken']:
          NEXTPAGE = data['nextPageToken'] 
          GetPlayListFromURL(URL+'pageToken='+NEXTPAGE+'&part=snippet&channelId='+CHANNEL_ID+'&key='+API_KEY)    
    except KeyError:
          print 'error ...'

def GetVideoListFromPlayList(url,playlist_id):
    data = json.load(urllib2.urlopen(url))
    for item in data['items']:
         playlist_ = item['snippet']['resourceId']['videoId']
         VIDEOLIST[playlist_] = item['snippet']['title']
    try:
       if data['nextPageToken']:
          NEXTPAGE = data['nextPageToken']
          #print 'next page is %s'%NEXTPAGE
          GetVideoListFromPlayList(URL_playlist+'pageToken='+NEXTPAGE+ '&part=snippet&playlistId='+playlist_id+ '&key='+API_KEY,playlist_id)
    except KeyError:
          print 'error ...'     
      
def main(channel_url,video_list_path):
   if not  os.path.exists(video_list_path):
                  print 'path is not exist...!'
                  sys.exit()

   global CHANNEL_ID
   CHANNEL_ID =  urlparse.urlparse(channel_url).path.split('/')[-1]
   GetPlayListFromURL(URL+'part=snippet&channelId='+CHANNEL_ID+'&key='+API_KEY)
   count = 1
   for item in PLAYLIST.values():
      print '%d: %s'%(count,item)
      count += 1
   print 'Enter choise from playlist:',
   try:
         selectplaylist = input()
   except KeyboardInterrupt:
         print 'bye..'
         sys.exit()
   selected_playlist = str(list(PLAYLIST.keys())[selectplaylist-1])
   GetVideoListFromPlayList(URL_playlist+'part=snippet&playlistId='+selected_playlist+'&key='+API_KEY,selected_playlist)
   count = 1
   for item in VIDEOLIST.values():
      print '%d: %s'%(count,item)
      count += 1 
   print 'Enter choise form video list("0" for all videos):',
   try:
       selected_video = raw_input().split(' ')
   except KeyboardInterrupt:
       print 'ok bye..'
       sys.exit()
   for video_index in range( int(selected_video[0]),int(selected_video[1])+1):
          tmpobj = download.DownloadVideo()
          if video_index == 0:
                 for all_video in VIDEOLIST.keys():
                       tmpobj.download(str(all_video),video_list_path)          
          else:   

                 video_id = str(list(VIDEOLIST.keys())[video_index-1])
                 tmpobj.download(video_id,video_list_path)
  
       

if __name__=='__main__':
   main(sys.argv[1],sys.argv[2])

#https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId=PLG49S3nxzAnnXcPUJbwikr2xAcmKljbnQ&key=AIzaSyCCxkwVyeibZFnIRdpclyxr5FMTGlxHztg
#https://www.googleapis.com/youtube/v3/playlistItems?pageToken=CAUQAA&part=snippet&playlistId=PLG49S3nxzAnnXcPUJbwikr2xAcmKljbnQ&key=AIzaSyCCxkwVyeibZFnIRdpclyxr5FMTGlxHztg
