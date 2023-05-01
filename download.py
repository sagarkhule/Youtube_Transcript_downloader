from youtube_transcript_api import _api
fhand = open('subtitles.txt', 'w+', encoding='utf-8')

try:
    url = input("Enter Youtube Url: ")
    id = url.split('=') 
    sub = _api.YouTubeTranscriptApi.get_transcript(id[1])
except:
    print("Enter Valid Youtube URL")
    exit()
print('\n Downloading ........\n')
for obj in sub:
    word = obj['text']
    fhand.write(word)
fhand.close()
print('Download Complete !')