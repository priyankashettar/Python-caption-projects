import os
import json
from user import User

def main():
    name=input("please enter the file name")
    file_name='{}.txt'.format(name)
    if file_exists(file_name):
        with open(file_name,'r') as f:
            json_data=json.load(f)
        user=User.from_json(json_data)
    else:
        user=User(name)        

    user_input=input("Enter '1' to add movie, '2' to see the list of movies,"
        "'3' to set the movie as watched, '4' to delete movie,'5' to see list of watched movie"
        "'6' to save or 'q' to exit")

    while user_input !='q':
        if user_input=='1':
            movie_name=input("enter the movie name here")
            movie_language=input("enter the language")
            user.add_movies(movie_name,movie_language)  
        elif user_input=='2':
            for movie in user.movies:
                print("name:{} language:{} watched:{}".format(movie.name,movie.language,movie.watched)) 
        elif user_input=='3':
            movie_watched=input("enter the name of the watched movie")
            user.set_watched(movie_watched)   
        elif user_input=='4':
            movie_delete=input("enter the name of the movie to delete")
            user.delete_movie(movie_delete)
        elif user_input=='5':
            for movie in user.watched_movies():
                print("name:{} language:{} watched:{}".format(movie.name,movie.language,movie.watched))    
        elif user_input=='6':
            with open(file_name,'w') as f:
                json.dump(user.json(),f)    

        user_input=input("Enter '1' to add movie, '2' to see the list of movies,"
            "'3' to set the movie as watched, '4' to delete movie,'5' to see list of watched movie"
            "'6' to save or 'q' to exit")

    


def file_exists(file_name):
    return os.path.isfile(file_name)
main()    