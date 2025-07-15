from youtube_transcript_api import YouTubeTranscriptApi

video_id = "nOzW1zieR7w" # 字幕を出力する動画のID(v=以降)
transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

for transcript in transcript_list:
    for tr in transcript.fetch():
        print(tr) # {'text': '字幕のテキスト情報', 'start': 字幕の開始時間, 'duration': 字幕が表示されている時間}