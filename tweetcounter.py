
import argparse

def main(term):
	"""Main function to start the program"""
	print(f"The terms: {term}")


if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument("--term", type=str, required=True, help="The term to look up in theset of tweets")

	args = parser.parse_args()
	print(args)
	main(args.term)
