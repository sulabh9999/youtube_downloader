import urllib2,urlparse

class DownloadVideo:
      def __init__(self):
          self.url = 'http://www.youtube.com/get_video_info?video_id='
          self.buffer_size = 1024 
          #self.responce = ''
          self.title = ''

      def download(self,video_id):
          responce = urllib2.urlopen(self.url+video_id)
          data = responce.read()
          info = urlparse.parse_qs(data) 
          self.title = info['title'][0]
          print self.title
          #stream_map = self.responce['url_encoded_fmt_stream_map'][0]         
          #video_info = stream_map.split(",")
          #print videeo_info

a=DownloadVideo()
a.download('pxofwuWTs7c')

'''
resp = urllib2.urlopen('http://www.youtube.com/get_video_info?video_id=gvVHSndpkEg')
data = resp.read()
info = urlparse.parse_qs(data)

title_ = info['title'][0]
fmane = title_+'.mp4'
stream_map = info['url_encoded_fmt_stream_map'][0]
v_info = stream_map.split(",")
for video in v_info:
    item = urlparse.parse_qs(video)
    #print item['quality'][0]
    #print item['type'][0]
    url = item['url'][0]
    resp = urllib2.urlopen(url)
    length = int(resp.headers['Content-length'])
    my_file = open(fmane,'w+r')
    done = 0
    buff = resp.read(1024)
    while buff:
         my_file.write(buff)
         done += 1024
         percent = done*100/length
         print '\r %d'%(percent),
         buff = resp.read(1024)
    break

'''
 
