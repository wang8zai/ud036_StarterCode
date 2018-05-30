import webbrowser
class Movie():
    def __init__(self, movie_title, movie_storyline, movie_poster, movie_trailer):
        self.title = movie_title                    
        self.storyline = movie_storyline                    #movie description
        self.poster_image_url = movie_poster                #movie poster
        self.trailer_youtube_url = movie_trailer            #trailer url

    def showTrailer(self):
        webbrowser.open(self.trailer_youtube_url)           #a method to show trailer in browser