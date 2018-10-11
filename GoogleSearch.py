


def gsearch(string,num):
    from googleapiclient.discovery import build

    apikey = "AIzaSyAdg6K5gxSaLaXLVT3nbqDNqLnp0587FaI"
    cseid = "017578349630011676667:i5oi_ecmspk"

    def google_search(search_term, api_key, cse_id, **kwargs): #Function from https://github.com/frrmack/googlesearch
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute() # seperate key value pairs using the ** syntax
        return res['items']

    results = google_search(
        string, apikey, cseid, num=10)
    
    # Added code
    resultlist = []
    # iterate through the results num amount and then 
    print(len(results))
    for x in range(0,num):
        if x == 10:
            break
        resultlist.append(results[x]['link'])
    
    
    return (resultlist)
