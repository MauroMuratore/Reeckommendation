import random
import firebase_api as firebase_api

def calculate_reccomend(id_user, id_location, randomness):
    user_reviews_beer = firebase_api.get_user_review_beer(id_user)
    print("retrive all reviews")
    good_beers = [ rev["beer"] for rev in user_reviews_beer if rev["rate"] > 2]
    bad_beers = [ rev["beer"] for rev in user_reviews_beer if rev["rate"] <= 2]

    bar_beers = firebase_api.get_location_beers(id_location)
    print("retrive all beers from location")
    if randomness==0 :
        best_beers_bar = [ beer for beer in bar_beers if beer in good_beers]
        if len(best_beers_bar) == 0 :
            return -1
        else :
            print(best_beers_bar)
            return random.choice(best_beers_bar)
    
    elif randomness==1:
        possible_beers_bar = [ beer for beer in bar_beers if beer not in bad_beers]
        if len(possible_beers_bar) == 0 :
            return -1
        else :
            print(possible_beers_bar)
            return random.choice(possible_beers_bar)
    
    elif randomness==2 :
        new_beer_bar = [beer for beer in bar_beers if not(beer in bad_beers or beer in good_beers)]
        if len(new_beer_bar) == 0 :
            return calculate_reccomend(id_user, id_location, 1)
        else :
            print(new_beer_bar)
            return random.choice(new_beer_bar)

    return -1        
