tweets = [
    "Wow, what a great day today!! #sunshine",
    "I feel sad about the things going on around us. #covid19",
    "I'm really excited to learn Python with @JovianML #zerotopandas",
    "This is a really nice song. #linkinpark",
    "The python programming language is useful for data science",
    "Why do bad things happen to me?",
    "Apple announces the release of the new iPhone 12. Fans are excited.",
    "Spent my day with family!! #happy",
    "Check out my blog post on common string operations in Python. #zerotopandas",
    "Freecodecamp has great coding tutorials. #skillup"
]

happy_words = ['great', 'excited', 'happy', 'nice', 'wonderful', 'amazing', 'good', 'best']

sad_words = ['sad', 'bad', 'tragic', 'unhappy', 'worst']

# store the final answer in this variable
number_of_happy_tweets = 0

# perform the calculations here
for tweet in tweets:
    # Get a word from happy_words
    for word in happy_words:
        # Check if the tweet contains the word
        if word in tweet:
            # Word found! Mark the tweet as happy
            number_of_happy_tweets+=1

print(number_of_happy_tweets)
print("This is Not Completed Yet")