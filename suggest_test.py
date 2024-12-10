import requests

def test_suggest():
    suggest_url = "https://en.wikipedia.org/w/api.php?action=opensearch&search=Python"
    response = requests.get(suggest_url)
    if response.status_code == 200:
        print("Suggest Endpoint:")
        print("Response:", response.json())
        print("Status: Success\n")
    else:
        print("Suggest Endpoint:")
        print("Status: Error -", response.status_code, response.reason, "\n")

if __name__ == "__main__":
    test_suggest()