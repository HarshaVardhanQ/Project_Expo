import random

class QuoteGenerator:
    def __init__(self, quotes):
        self.quotes = quotes

    def get_random_quote(self):
        return random.choice(self.quotes)

if __name__ == "__main__":
    # Sample quotes
    quotes = [
        "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "The way to get started is to quit talking and begin doing. - Walt Disney",
        "Your time is limited, don't waste it living someone else's life. - Steve Jobs"
    ]

    # Initialize the QuoteGenerator
    quote_generator = QuoteGenerator(quotes)

    # Get a random quote
    random_quote = quote_generator.get_random_quote()

    # Display the quote
    print("Random Quote:")
    print(random_quote)
