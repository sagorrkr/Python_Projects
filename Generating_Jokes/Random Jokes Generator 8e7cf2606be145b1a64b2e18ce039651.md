# Random Jokes Generator

pyJokes is a Python library that allows users to access a collection of jokes through a simple API. The library can be easily installed using pip by running the command `pip install pyjokes`. Once installed, the library can be imported into your Python code to retrieve a random joke from the collection or search for a specific type of joke. Here is a example how to generate jokes. 

```python
import pyjokes

joke1 = pyjokes.get_joke(language="en", category="all")
print(joke1,"\n")

joke2 = pyjokes.get_joke(language="en", category="neutral")
print(joke2,"\n")

jokes = pyjokes.get_jokes(language="en", category="neutral")

for i in range(5):
    print(i+1,".",jokes[i],"\n")

```