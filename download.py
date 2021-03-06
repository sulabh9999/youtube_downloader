import urllib2,urlparse
import re

class DownloadVideo:
      def __init__(self):
          self.url = 'http://www.youtube.com/get_video_info?video_id='
          self.buffer_size = 1024 
          #self.responce = ''
          self.title = ''

      def download(self,counter,video_id,video_list_path):
          '''
          try:
              open(video_list_path, 'r')
          except IOError:
              print 'path is not valid..!'
              sys.exit()
          
          
          if not  os.path.exists(video_list_path):
                  print 'path is not exist...!'
                  sys.exit()
          '''
          
          responce = urllib2.urlopen(self.url+video_id)
          data = responce.read()
          info = urlparse.parse_qs(data) 
          self.title = info['title'][0]
          #print 'Title: '+self.title+'...',
          stream_map = info['url_encoded_fmt_stream_map'][0]         
          video_info = stream_map.split(",")
          for video in video_info:
                    item = urlparse.parse_qs(video)
                    #print item['quality'][0]
                    #print item['type'][0]
                    #print item['url'][0]
                    url = item['url'][0]
                    responce = urllib2.urlopen(url)
                    length = int(responce.headers['Content-length'])
                    self.title = re.sub('[^0-9a-zA-Z_ ]+', '', self.title)
                    my_file = open(video_list_path+'/'+self.title+'.mp4','w+r')
                    done = 0
                    buffer = responce.read(1024)
                    while buffer: 
                            my_file.write(buffer)
                            done += 1024
                            percent = done*100/length
                            print '\r%s: %s.... %d%%' %(counter,self.title,percent),
                            buffer = responce.read(1024)
                    break
          print ''

#a=DownloadVideo()
#a.download('YCcAE2SCQ6k')
