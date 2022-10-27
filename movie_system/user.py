from unicodedata import name
from movie import Movie

class User:
    def __init__(self,name):
        self.name=name
        self.movies=[]

    def __repr__(self):
        return "<User {}>".format(self.name)

    def watched_movies(self):
        return list(filter(lambda new_watchedlist:new_watchedlist.watched, self.movies))

    def set_watched(self,name):
        for movie in self.movies:
            if movie.name==name:
                movie.watched=True

    def add_movies(self,name,language):
        movie_obj=Movie(name,language,False)
        self.movies.append(movie_obj)

    def delete_movie(self,name):
        self.movies=list(filter(lambda x: x.name!=name,self.movies))   

    def write_to_csv_file(self):
        with open("{}.txt".format(self.name), 'w') as f:
            f.write(self.name + "\n")
            for i in self.movies:
                f.write("{},{},{}\n".format(i.name,i.language,str(i.watched)))
   # @classmethod
   # def read_from_file(cls,priya):
    #    with open("priya","r") as f:
     #       file_content=f.readlines()
      #      user_name=file_content[0]
       #     movie=[]
        #    for i in file_content[1:]:
         #       file_data=i.split(",")
          #      movie.append(Movie(file_data[0],file_data[1],file_data[2]==True))
           # user=cls(user_name)
            #user.movies=movie
            #return user  


    def json(self):
        return {
            "name":self.name,
            "movies":
            [movie.json() for movie in self.movies]
        }

    
    @classmethod
    def from_json(cls,json_data):
        user=User(json_data['name'])
        movies=[]
        for i_data in json_data['movies']:
            movies.append(Movie.from_json(i_data))
        user.movies=movies

        return user    


        
        
