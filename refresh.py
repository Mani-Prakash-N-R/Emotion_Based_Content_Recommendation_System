import secret  # Assuming secret.py is in the same directory

class Refresh:
    def __init__(self):
        self.access_token = secret.access_token
        self.refresh_token = secret.refresh_token
        self.base_64 = secret.base_64

    def refresh(self):
        return self.access_token

# Example usage
if __name__ == "__main__":
    refresher = Refresh()
    access_token = refresher.refresh()
    print("Access token:", access_token)
