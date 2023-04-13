import requests


class MessagePusherSDK:
    def __init__(self, host, token='') -> None:
        self.host = host
        self.token = token
        # self.sess = requests.session()

    def __enter__(self):
        self.sess = requests.Session()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.sess.close()

    def push(self, username: str, title: str, description: str, content: str) -> None | str:
        res = requests.post(f"{self.host}/push/{username}", json={
            "title": title,
            "description": description,
            "content": content,
            "token": self.token
        }).json()

        if res["success"]:
            return None
        else:
            return res["message"]
