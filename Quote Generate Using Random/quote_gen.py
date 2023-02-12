import random

#the list of quotes
quotes = [
    "The best way to predict your future is to create it. - Abraham Lincoln",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "You miss 100% of the shots you don't take. - Wayne Gretzky",
    "It's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
    "If you want to live a happy life, tie it to a goal, not to people or things. - Albert Einstein",
    "Happiness is not something ready made. It comes from your own actions. - Dalai Lama"
]

#to generate a random quote
def generate_quote():
    #to Select a random quote from the list
    quote = random.choice(quotes)
    print(quote)

generate_quote()
