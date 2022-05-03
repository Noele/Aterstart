import json
import os.path


class Loader:
    def __init__(self):
        self.path = "data.json"
        self.data = None
        self.default_data = {
            "username": "",
            "password": "",
            "discord_bot_token": "",
            "hashed": False
        }
        self.load_data()


    def get_credentials(self):
        return self.data["username"], self.data["password"]

    def get_token(self):
        return self.data["discord_bot_token"]

    def load_data(self):
        if not os.path.exists(self.path):
            file = open(self.path, "x")
            file.write(json.dumps(self.default_data))
            file.close()
            print("data.json Created, Please update the file with your credentials.")
            exit()

        file = open(self.path)
        self.data = json.load(file)
        file.close()
        if self.data["username"] == "" or self.data["password"] == "":
            print("No username / password found in data.json")
            exit(404)

    def hash_data(self, aternos):
        self.data["password"] = aternos.md5encode(self.data["password"])
        self.data["hashed"] = True
        with open(self.path, "w") as jsonFile:
            json.dump(self.data, jsonFile)

    def get_hashed(self):
        return self.data["hashed"]