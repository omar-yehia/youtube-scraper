# https://pytube.io/en/latest/api.html
from pytube import YouTube, Search

all_video_ids=[1,2,3,4]

def videoExist(video_id):
	return video_id in all_video_ids



#
def getSearchObj(keywords):
	return Search(keywords)

def getSearchResults(searchObj):
	return searchObj.results

# def appendMoreSearchResults(searchObj):
# 	searchObj.get_next_results();
# 	return searchObj

def getStreams(youtubeObj):
	return youtubeObj.streams

def getStreamByResolution(streams,requiredResolution='720p'):
	return streams.get_by_resolution(requiredResolution)

def getStreamByHighestResolution(streams):
	return streams.get_highest_resolution()

def downloadStream(stream,videos_directory='videos'):
	stream.download(videos_directory)

def getVideoDetails(youtubeObj):
	return youtubeObj.vid_info['videoDetails']

def tryFetchingDetails(youtubeObj):
	attempts=0
	videoDetails=None
	while attempts < 3:
		try:
			attempts+=1
			videoDetails=getVideoDetails(youtubeObj)
			if(videoDetails):
				break
		except:
			pass
	    	

	return videoDetails
	

def downloadSearchResults(searchObj):
	# youtubeObj=searchObj[0]
	for youtubeObj in searchObj:
		attempts=0
		videoDetails=tryFetchingDetails(youtubeObj)
		if(not videoDetails): return
		streams=getStreams(youtubeObj)
		desiredStream=getStreamByResolution(streams)
		saveVideo(desiredStream,videoDetails)

def insertVideo(video_id,video_title):
	all_video_ids.append(video_id)
	print('saved',video_id,video_title)
	return

def saveVideo(desiredStream,videoDetails):
	if(not desiredStream): return
	videoId=videoDetails['videoId']
	title=videoDetails['title']
	# lengthSeconds=videoDetails['lengthSeconds']
	# channelId=videoDetails['channelId']
	# keywords=videoDetails['keywords']
	if(videoExist(videoId)): return
	print('downloading... ',videoId,title)
	downloaded=downloadStream(desiredStream)
	insertVideo(videoId,title)


# keywords="world cup"
print('Wakeb Youtube collector')
print('enter keywords')
keywords=input()

searchObj=getSearchObj(keywords);
searchRes=getSearchResults(searchObj)
searchObj.get_next_results()
# print(searchRes)
# exit()
# searchObj=appendMoreSearchResults(searchObj)  # can't pass by reference , so, won't make it in a separated function to save copied memory
downloadSearchResults(searchRes)