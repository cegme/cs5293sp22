import json


class Tweet:
    def __init__(self, tweetstring):
        self._tweetstring = tweetstring

    def text(self):
        """Returns the text of the tweet."""
        return json.loads(self._tweetstring)["text"]

    def id(self):
        return json.loads(self._tweetstring)["_id"]

    def __contains__(self, term):
        return term in self.text

    def __str__(self):
        return f"<{self.id()}: {self.text()}>"


if __name__ == "__main__":
    with open("resources/tweets.json") as tweetfile:
        tweetstring = tweetfile.readline()
        tweet = Tweet(tweetstring)
        print(tweet)
