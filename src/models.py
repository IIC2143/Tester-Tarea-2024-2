from copy import deepcopy


class Game:

    def __init__(self, name, calification, description):
        self.id = None
        self.name = name
        self.calification = calification
        self.desciption = description
        self.reviews = []


    def data(self):
        return {
            'game': {
                'name': self.name,
                'calification': self.calification,
                'description': self.desciption,
            },
        }

    def is_valid(self, data, is_new=False):
        attr_1 = data['id'] == self.id or is_new
        attr_2 = data['name'] == self.name
        attr_3 = data['calification'] == self.calification
        attr_4 = data['description'] == self.desciption

        return all([attr_1, attr_2, attr_3, attr_4])
    
    def calculate_points(self):
        countOfReviews = 0
        sumCalification = 0
        newCalification = 0

        for review in self.reviews:

            if review.calification:
                countOfReviews += 1
                newCalification += review.calification
            
        if len(self.reviews) != 0:
            newCalification = sumCalification/countOfReviews
            return newCalification
        else: 
            return self.calification

    def destroy(self):
        for review in self.reviews:
            review.destroy()

        self.reviews.clear()


    def __str__(self):
        return self.__dict__.__str__()

    def __repr__(self):
        return self.__dict__.__repr__()


class Review:

    def __init__(self, title, description, calification):
        self.id = None
        self.title = title
        self.description = description
        self.calification = calification
        self.player_id = None
        self.game_id = None

    def data(self):
        return {
            'review': {
                'title': self.title,
                'description': self.description,
                'calification': self.calification,
            },
        }

    def is_valid(self, data, is_new=False):
        attr_1 = data['id'] == self.id or is_new
        attr_2 = data['title'] == self.title
        attr_3 = data['description'] == self.description
        attr_4 = data['calification'] == self.calification
        attr_5 = data['player_id'] == self.player_id
        attr_6 = data['game_id'] == self.game_id 

        return all([attr_1, attr_2, attr_3, attr_4, attr_5, attr_6])

    def update(self, data):

        if 'title' in data['review']:
            self.title = data['review']['title']
        
        if 'description' in data['review']:
            self.description = data['review']['description']

        if 'calification' in data['review']:
            self.calification = data['review']['calification']
        
        if 'player_id' in data['review']:
            self.player_id = data['review']['player_id']
        
        if 'game_id' in data['review']:
            self.game_id = data['review']['game_id']

    def destroy(self):
        pass

    def __str__(self):
        copy = deepcopy(self)
        return copy.__dict__.__str__()

    def __repr__(self):
        return self.__dict__.__repr__()


class Player:

    def __init__(self, name, preference , phone):
        self.id = None
        self.name = name
        self.preference = preference
        self.phone = phone
        self.favourite_game_id = None


    def data(self):
        return {
            'player': {
                'name': self.name,
                'preference': self.preference,
                'phone': self.phone,
            },
        }

    def is_valid(self, data, is_new=False):
        attr_1 = data['id'] == self.id or is_new
        attr_2 = data['name'] == self.name
        attr_3 = data['preference'] == self.preference
        attr_4 = data['phone'] == self.phone
        attr_5 = data['favourite_game_id'] == self.favourite_game_id or is_new


        return all([attr_1, attr_2, attr_3, attr_4, attr_5])

    def destroy(self):
        pass


    def __str__(self):
        copy = deepcopy(self)
        del copy.team
        return copy.__dict__.__str__()

    def __repr__(self):
        copy = deepcopy(self)
        del copy.team
        return copy.__dict__.__repr__()
