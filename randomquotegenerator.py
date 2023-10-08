import random

# List of quotes
quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Innovation distinguishes between a leader and a follower. - Steve Jobs",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "The best way to predict the future is to invent it. - Alan Kay",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "All our dreams can come true; if we have the courage to pursue them. - Walt Disney",
    "However difficult life may seem, there is always something you can do and succeed at. - Stephen Hawking",
    "People begin to become successful the minute they decide to be. - Harvey MacKay",
    "It always seems impossible until it’s done. - Nelson Mandela",
    "Nothing is impossible, the word itself says ‘I’m possible’! - Audrey Hepburn",
    "Success isn’t overnight. It’s when every day you get a little better than the day before. It all adds up. - Dwayne Johnson",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "The more you praise and celebrate your life, the more there is in life to celebrate. - Oprah Winfrey",
    "Do what you can, with what you’ve got, where you are. - Teddy Roosevelt",
    "Success consists of going from failure to failure without loss of enthusiasm. - Winston Churchill",
    "Women, like men, should try to do the impossible. And when they fail, their failure should be a challenge to others. - Amelia Earhart",
    "Victory is sweetest when you’ve known defeat. - Malcolm S. Forbes",
    "Satisfaction lies in the effort, not in the attainment, full effort is full victory. - Mahatma Gandhi",
    "Energy and persistence conquer all things. - Benjamin Franklin",
    "Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time. - Thomas A. Edison",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "It is better to fail in originality than to succeed in imitation. - Herman Melville",
    "A man can succeed at almost anything for which he has unlimited enthusiasm. - Charles Schwab",
    "In most things success depends on knowing how long it takes to succeed. - Montesquieu",
    "There are no limits. There are only plateaus, and you must not stay there — you must go beyond them. - Bruce Lee",
    "Fortune befriends the bold. - Emily Dickinson",
    "Success is survival. - Leonard Cohen",
    "There is little success where there is little laughter. - Andrew Carnegie",
    "There is no substitute for victory. - Douglas MacArthur",
    "They succeed, because they think they can. - Virgil",
    "It takes 20 years to make an overnight success. - Eddie Cantor",
    "Victory has a thousand fathers, but defeat is an orphan. - John F. Kennedy",
    "If you have no critics you’ll likely have no success. - Malcolm X",
    "Success is never accidental. - Jack Dorsey",
    "Doubt kills more dreams than failure ever will. - Suzy Kassem",
    "The best revenge is massive success. - Frank Sinatra",
    "Men are born to succeed, not to fail. - Henry David Thoreau",
    "Success is the child of audacity. - Benjamin Disraeli",
    "Impatience never commanded success. - Edwin H. Chapin",
    "If opportunity doesn’t knock, build a door. - Milton Berle",
]

def get_random_quote():
    return random.choice(quotes)

if __name__ == "__main__":
    print("Welcome to the Random Quote Generator!")
    input("Press Enter to get a random quote...")

    random_quote = get_random_quote()
    print("\nHere's your random quote:\n")
    print(random_quote)
