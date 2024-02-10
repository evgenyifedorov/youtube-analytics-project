import os

from googleapiclient.discovery import build


class Video:
    """
    Класс для ютуб-канала
    """

    api_key: str = os.getenv('YOU_TUB_API')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id: str) -> None:
        """
        Инициализация реальными данными следующих атрибутов экземпляра класса.
        """

        self.video_id = video_id


        video = self.youtube.videos().list(part='snippet, statistics, contentDetails, topicDetails',
                                      id=video_id).execute()

        self.video_url: str = f"https://youtu.be/{self.video_id}"
        self.title = video['items'][0]['snippet']['title']
        self.view_count = video['items'][0]['statistics']['viewCount']
        self.like_count = video['items'][0]['statistics']['likeCount']


    def __str__(self):
        return f"{self.title}"


class PLVideo(Video):
    """
    второй класс для видео `PLVideo`, который инициализируется  'id видео' и 'id плейлиста'
    """
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id


