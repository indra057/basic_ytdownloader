from pytube import YouTube
from sys import argv

link = argv[1] #to run the program " python3 programfilename.py <youtube link> in cmd line and press enter "
yt = YouTube(link)

print("Title: ",yt.title)
print("View: ",yt.views)

yd = yt.streams.get_highest_resolution()

yd.download('/home/indra/Downloads')
# the directory in which you will save the youtube video
#sys.argv[0]: This is the name of the script itself. For example, if your script is named "youtubedownloader.py," sys.argv[0] will be "youtubedownloader.py."

#sys.argv[1], sys.argv[2], and so on: These elements represent the command-line arguments you pass to the script. If you run the script with additional arguments, they will be accessible through sys.argv[1], sys.argv[2], and so on, depending on the number of arguments you provide.
