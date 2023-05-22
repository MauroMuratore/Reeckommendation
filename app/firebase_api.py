from firebase import firebase

#connect to firebase
_fb_app = firebase.FirebaseApplication("https://beer-app-8729f-default-rtdb.europe-west1.firebasedatabase.app/", None)

def get_user_review_beer(user_id):
    user_id_reviews = _fb_app.get("users/" + user_id +"/review_beer", None)
    reviews = [_fb_app.get("reviews", id_rev) for id_rev in user_id_reviews]
    return [{"beer" : r["beer"], "rate": r["rate"]} for r in reviews ]

def get_location_beers(location_id):
    location_id_beer = _fb_app.get("locations/" + location_id + "/beers", None)
    return list(location_id_beer.keys())