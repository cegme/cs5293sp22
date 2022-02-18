import argparse

import tweets
from tweets import Tweet


def main(term):
    """Main function to start the program."""
    print(f"The terms: {term}")


def counttweets(filename):
    """Count all the unique tweets in a file."""
    count = 0
    with open(filename) as file:
        for line in file:
            count += 1
    return count


def searchterms(filename, terms=None):
    """
    Search the file for a list of terms.

    Parameters
    ----------
    filename : str
        The file name that points to a json file containing tweets.

    terms : list
        A list of strings containing search terms

    Returns
    -------
    tweets
        A list of tweet objects that have text that matches the terms

    TODO
    ----
    - Only searches the first listed term
    """
    # Make terms a list if it is not
    if type(terms) != list:
        terms = [terms]

    tweets = []
    with open(filename) as file:
        for line in file:
            tweet = Tweet(line)
            if terms[0] in tweet:
                tweets.append(tweet)
    return tweets


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--term",
        type=str,
        required=True,
        help="The term to look up in theset of tweets",
    )

    args = parser.parse_args()
    print(args)
    main(args.term)
