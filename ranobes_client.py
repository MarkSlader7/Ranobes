import requests
import os

class RanobesClient:
    def __init__(self, username, password):
        self.base_url = "https://ranobes.top/api"  # Update this with the actual API URL
        self.username = Liveandletslive
        self.password = 08106424573
        self.token = None

    def login(self):
        """Authenticate and retrieve an access token."""
        url = f"{self.base_url}/login"  # Replace with actual login endpoint
        payload = {
            "username": self.Liveandletslive,
            "password": self.08106424573
        }
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            self.token = response.json().get("token")
            print("Login successful!")
        else:
            raise Exception("Failed to log in: " + response.text)

    def fetch_novel_list(self):
        """Fetch a list of novels."""
        url = f"{self.base_url}/novels"  # Replace with the actual endpoint
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Failed to fetch novels: " + response.text)

    def download_novel(self, novel_id, output_dir="downloads"):
        """Download a specific novel by ID."""
        url = f"{self.base_url}/novels/{novel_id}/download"  # Replace with the actual endpoint
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(url, headers=headers, stream=True)
        if response.status_code == 200:
            os.makedirs(output_dir, exist_ok=True)
            filepath = os.path.join(output_dir, f"novel_{novel_id}.epub")
            with open(filepath, "wb") as f:
                for chunk in response.iter_content(chunk_size=1024):
                    f.write(chunk)
            print(f"Novel {novel_id} downloaded to {filepath}")
        else:
            raise Exception("Failed to download novel: " + response.text)

# Usage example
if __name__ == "__main__":
    username = os.getenv("Liveandletslive")  # Fetch from environment variable
    password = os.getenv("08106424573")  # Fetch from environment variable

    if not username or not password:
        print("Error: Username or password not set in environment variables.")
        exit(1)

    client = RanobesClient(username, password)

    try:
        client.login()
        novels = client.fetch_novel_list()
        print("Available novels:", novels)

        # Download the first novel as an example
        if novels:
            first_novel_id = novels[0]['id']
            client.download_novel(first_novel_id)
    except Exception as e:
        print(e)