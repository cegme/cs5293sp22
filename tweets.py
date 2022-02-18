import json
import logging


class Tweet(object):
    """
    A class work working with tweets.

    Parameters
    ----------
    tweetstring : str
        This is a twitter object that is a string.

    Attributes
    ----------
    text : str
        This is a string object with the tweet text
    """

    def __init__(self, tweetstring):
        self._tweetstring = tweetstring

    @property
    def text(self):
        """Returns the text of the tweet."""
        return json.loads(self._tweetstring)["text"]

    @text.setter
    def text(self, newvalue):
        pass

    def id(self):
        return json.loads(self._tweetstring)["_id"]

    def __contains__(self, term):
        logging.debug(f"{term} -> [[[{self.text}]]]")
        return term in self.text

    def __str__(self):
        return f"<{self.id()}: {self.text[:50]}>"

    def __repr__(self):
        return f"<{self.id()}>"


if __name__ == "__main__":
    with open("resources/tweets.json") as tweetfile:
        tweetstring = tweetfile.readline()
        tweet = Tweet(tweetstring)
        print(tweet)
        print(tweet.text)
        # tweet.text = "Why are you rapping?" # Doesn't work
