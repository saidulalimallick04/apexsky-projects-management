import requests
from django.conf import settings

headers = {
    "Authorization": f"Client-ID {settings.UNSPLASH_ACCESS_KEY}"
}
def request_for_image(query,per_page):
    
    search_url = "https://api.unsplash.com/search/photos"
    
    parameters={
        "query": query,
        "per_page": per_page
    }
    response=requests.get(search_url,headers=headers,params=parameters)

    photo_urls=[]
    if (response.status_code)== 200:
        data=response.json()
        for i, photo in enumerate(data["results"], start=1):
            photo_urls.append(photo['urls']['regular'])
            
        return photo_urls
    else:
        print("Error:", response.status_code, response.json())
    
    