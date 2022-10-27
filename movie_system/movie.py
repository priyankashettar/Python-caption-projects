class Movie:
    def __init__(self, name, language,watched):
        self.name=name
        self.language=language
        self.watched=watched


    def __repr__(self):
        return "<movie {}>".format(self.name)


    def json(self):
        return{
            "name":self.name,
            "language":self.language,
            "watched":self.watched
        }       

    @classmethod
    def from_json(cls,json_data):
        #return Movie(json_data['name'],json_data['language'],json_data['watched'])
        return Movie(**json_data)