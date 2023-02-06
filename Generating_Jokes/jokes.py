import pyjokes



joke1 = pyjokes.get_joke(language="en", category="all")
print(joke1,"\n")

joke2 = pyjokes.get_joke(language="en", category="neutral")
print(joke2,"\n")

jokes = pyjokes.get_jokes(language="en", category="neutral")

'''for i in range(5):
    print(i+1,".",jokes[i],"\n")'''