import urllib.request
import urllib.parse
import sys

def test_app():
    url = "http://127.0.0.1:5000"
    
    # Test GET request
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')
            if "Game Score Calculator" in html:
                print("GET request successful: 'Game Score Calculator' found in response.")
            else:
                print("GET request failed: 'Game Score Calculator' not found.")
                sys.exit(1)
    except Exception as e:
        print(f"GET request failed with error: {e}")
        sys.exit(1)

    # Test POST request
    data = urllib.parse.urlencode({
        "player_name": "Bob",
        "games_played": "5",
        "total_score": "250"
    }).encode('utf-8')
    
    try:
        req = urllib.request.Request(url, data=data, method="POST")
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            if "Average Score: 50.0" in html and "Player: Bob" in html:
                print("POST request successful: Correct average score found.")
            else:
                print("POST request failed: Output not found.")
                print(html) # Debug
                sys.exit(1)
    except Exception as e:
        print(f"POST request failed with error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    test_app()
