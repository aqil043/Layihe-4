import requests

def test_geo_search():
    geo_search_url = "https://en.wikipedia.org/w/api.php?action=query&list=geosearch&gscoord=37.786971|-122.399677&gsradius=10000&format=json"
    response = requests.get(geo_search_url)
    if response.status_code == 200:
        data = response.json()
        geo_search_results = data['query']['geosearch']
        print("Geo Search Endpoint:")
        print("Geo Search Results:", geo_search_results)
        print("Status: Success\n")
    else:
        print("Geo Search Endpoint:")
        print("Status: Error -", response.status_code, response.reason, "\n")

if __name__ == "__main__":
    test_geo_search()

