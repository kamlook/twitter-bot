    # -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 11:08:00 2019

@author: Kam Look
"""
#import necessary libraries
import json
import tweepy as tw
import random as rd
import time as time
#use keys to get authourization from twitter
consumer_key= 'YMNxGy6kiMXDAQCmTNNDutj3R'
consumer_secret= '29sqvFEGzH4m5AnDTfYhtdXfaTSXZA3RgvIWaO49ysndqn2f8W'
access_token= '1172928849081815040-taCoW8NCF0d2r8AfOnYbBOoEs7jk8e'
access_token_secret= 'M7fn0i3Wmm8Ue1gt52WREUIOsRhgLdgHKIIyxg8MHZFiS'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth,wait_on_rate_limit=True)
FILE_NAME='last_seen_id.txt'
#defining functions to open last id and prevent redundant responses

pokemonTypeList=['Normal','Fire','Fighting','Water','Flying','Grass','Poison',
                 'Electric','Ground','Psychic','Rock','Ice','Bug','Dragon',
                 'Ghost','Dark','Steel','Fairy']
#for dev testing use id = 1173102244662636544
def pokedex_replys():
    f_read=open(FILE_NAME,'r')
    lastSeenID=int(f_read.read().strip())
    print(lastSeenID)
    f_read.close()
    mentions=api.mentions_timeline(lastSeenID)
    print('Retrieving and responding...')
    type1Int=18
    type2Int=18
    for mention in reversed(mentions):
        lastSeenID=mention.id
        f_write=open(FILE_NAME,'w')
        f_write.write(str(lastSeenID))
        f_write.close()
        user=mention.user
        user=json.dumps(user._json)
        user=json.loads(user)
        if '#reroll' in mention.text.lower():
            type1Int=rd.randint(0,17)
            type2Int=rd.randint(0,17)
            while type1Int == type2Int:
                type2Int=rd.randint(0,17)
            type1=pokemonTypeList[type1Int]
            type2=pokemonTypeList[type2Int]
            msgNum=rd.randint(0,2)
            if type1Int==type2Int:
                return api.update_status(status='@'+ user['screen_name'] + ' Wow! The data says you would be a pure' + type1 + ' type Pokemon!',
                                  in_reply_to_status_id= mention.id)
            elif msgNum==0:return api.update_status(status='@'+ user['screen_name'] + ' Hmmmm... Looks like you would be a ' + type1 + '/'+ type2 + ' type Pokemon!',
                              in_reply_to_status_id= mention.id)
            elif msgNum==1:return api.update_status(status='@'+ user['screen_name'] + ' Really? Well ok... The scan reports that you would definitely be a ' + type1 + '/'+ type2 + ' type Pokemon!',
                              in_reply_to_status_id= mention.id)
            else: return api.update_status(status='@'+ user['screen_name'] + ' Ha! Yeah, that makes sense. No doubt you are a ' + type1 + '/'+ type2 + ' type Pokemon!',
                              in_reply_to_status_id= mention.id)
        #36 fucking conditions because i am lazy on not creative
        if '#whatsmytype' in mention.text.lower():
            print('recieved a #whatsmytype')
            if 'x' in user['screen_name'].lower():type1Int=0
            if int(user['created_at'].split()[-1]) < 2012: type1Int=1
            if user['statuses_count'] > 6000: type1Int=2
            if 'a' in user['screen_name'][3:5].lower(): type1Int=3
            if len(user['description']) >110: type1Int=4
            if user['followers_count']%10==0: type1Int=5
            if user['id_str'][7] == '7': type1Int=6
            if 'r' in user['screen_name'].lower(): type1Int=9
            if user['id_str'][-1] == '0': type1Int=10
            if user['id_str'][-1] == '1': type1Int=11
            if user['id_str'][-1] == '2': type1Int=12
            if user['id_str'][-1] == '3': type1Int=13
            if user['id_str'][-1] == '4': type1Int=14
            if user['id_str'][-1] == '5': type1Int=15
            if user['id_str'][-1] == '6': type1Int=16
            if user['id_str'][-1] == '7': type1Int=17
            if user['id_str'][-1] == '8': type1Int=7
            if user['id_str'][-1] == '9': type1Int=8
            if 'e' in user['screen_name'][6:8]: type2Int=0
            if 'z' in user['screen_name']: type2Int=1
            if len(user['description'])<10: type2Int=2
            if user['followers_count']%7== 0: type2Int=3
            if 't' in user['name'].lower(): type2Int=4
            if int(user['created_at'].split()[-1]) > 2017:type2Int=5
            if 's' in user['screen_name'].lower(): type2Int=6
            if user['friends_count']%10==0: type2Int=9
            if user['id_str'][-2] == '0': type2Int=10
            if user['id_str'][-2] == '1': type2Int=11
            if user['id_str'][-2] == '2': type2Int=12
            if user['id_str'][-2] == '3': type2Int=13
            if user['id_str'][-2] == '4': type2Int=14
            if user['id_str'][-2] == '5': type2Int=15
            if user['id_str'][-2] == '6': type2Int=16
            if user['id_str'][-2] == '7': type2Int=17
            if user['id_str'][-2] == '8': type2Int=7
            if user['id_str'][-2] == '9': type2Int=8
            type1=pokemonTypeList[type1Int]
            type2=pokemonTypeList[type2Int]
            msgNum=rd.randint(0,2)
            if type1Int==type2Int:
                return api.update_status(status='@'+ user['screen_name'] + ' Wow! The data says you would be a pure' + type1 + ' type Pokemon!',
                                  in_reply_to_status_id= mention.id)
            elif msgNum==0: return api.update_status(status='@'+ user['screen_name'] + ' Hmmmm... Looks like you would be a ' + type1 + '/'+ type2 + ' type Pokemon!',
                              in_reply_to_status_id= mention.id)
            elif msgNum==1: return api.update_status(status='@'+ user['screen_name'] + ' Really? Well ok... The scan reports that you would definitely be a ' + type1 + '/'+ type2 + ' type Pokemon!',
                              in_reply_to_status_id= mention.id)
            else: return api.update_status(status='@'+ user['screen_name'] + ' Ha! Yeah, that makes sense. No doubt you are a ' + type1 + '/'+ type2 + ' type Pokemon!',
                              in_reply_to_status_id= mention.id)
while True:
    pokedex_replys()
    time.sleep(61)
