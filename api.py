import json,urllib2
####################################################initial url ########################################




url = 'https://www.googleapis.com/youtube/v3/playlists?part=snippet&channelId=UCkefXKtInZ9PLsoGRtml2FQ&key=AIzaSyCCxkwVyeibZFnIRdpclyxr5FMTGlxHztg'
d= urllib2.urlopen(url)
data = json.load(d)

for item in data['items']:
   print item['snippet']['title']
#print data


