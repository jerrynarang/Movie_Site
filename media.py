import webbrowser
class Movie():
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):#init is a reserved function in python due to which it has 2 underscores at start and beginning.It takes a few arguments
        self.title=movie_title        #one of them is self.self means itself.
        self.storyline=movie_storyline #self is the instance being created in entertainment.py so self=toy_story or avatar
        self.poster_image_url=poster_image       #using init to initialise pieces of info like title,storyline etc These variables are unique to an object and are called instance variables
        self.trailer_youtube_url=trailer_youtube     

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
# All functions inside a class that haveself as argument are instance methods/functions
