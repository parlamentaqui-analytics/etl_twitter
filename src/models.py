from mongoengine import *

class Deputy(Document):
    id = IntField(primary_key=True)
    name = StringField(required=True)
    photo_url = StringField()
    initial_legislature_id = IntField(required=True)
    final_legislature_id = IntField()
    initial_legislature_year = IntField(required=True)
    final_legislature_year = IntField()
    last_activity_date = DateTimeField()
    full_name = StringField()
    sex = StringField()
    email = StringField()
    birth_date = DateTimeField()
    death_date = DateTimeField()
    federative_unity = StringField()
    party = StringField()
    instagram_username = StringField()
    twitter_username = StringField()
    facebook_username = StringField()
    twitter_id = StringField()
    website = StringField()

    def to_json(self):
        return{
            'id':self.id,
            'name':self.name,
            'photo_url':self.photo_url,
            'initial_legislature_id':self.initial_legislature_id,
            'final_legislature_id':self.final_legislature_id,
            'initial_legislature_year':self.initial_legislature_year,
            'final_legislature_year':self.final_legislature_year,
            'last_activity_date':self.last_activity_date,
            'full_name':self.full_name,
            'sex':self.sex,
            'email':self.email,
            'birth_date':self.birth_date,
            'death_date':self.death_date,
            'federative_unity':self.federative_unity,
            'party':self.party,
            'instagram_username':self.instagram_username,
            'twitter_username':self.twitter_username,
            'facebook_username':self.facebook_username,
            'twitter_id':self.twitter_id,
            'website':self.website
        }


# class News(Document):
#     id = IntField(primary_key=True)
#     deputy_id = IntField()
#     link = StringField()
#     photo = StringField()
#     title = StringField()
#     abstract = StringField()
#     deputy_name = StringField()
#     update_date = DateTimeField()
#     source = StringField()

class DBTest(Document):
    message = StringField()

class Tweet(Document):
    tweet_id = IntField(primary_key=True)
    deputy_id = IntField()
    name = StringField()
    twitter_username = StringField()
    date = DateTimeField()

    def to_json(self):
        return {
            'tweet_id':self.tweet_id,
            'deputy_id':self.deputy_id,
            'name':self.name,
            'twitter_username':self.twitter_username,
            'date':self.date
        }
