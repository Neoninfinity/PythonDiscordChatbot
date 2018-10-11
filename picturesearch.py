def place(locVal,keyVal):
    from googleplaces import GooglePlaces, types, lang
    google_places = GooglePlaces('AIzaSyCGnrUPzm-6IehnzxsuxEGy8IgD5M1gGe8')
    
    ##Reference to the google library for place search
    
    result = google_places.nearby_search(location= locVal, keyword= keyVal,radius=20000, types=[types.TYPE_FOOD]) 

    # Written code
    if result.has_attributions:
        print (result.html_attributions)
        
    place= result.places[0]
    photo = place.photos[0]
    photo.get(maxheight=500, maxwidth=500)
    returnlist = [place.name,place.geo_location,place.place_id,photo.url]

    return returnlist
