from nltk.chat.util import Chat, reflections

pairs = [
[
 r"my name is (.*)",
 ["Hello %1, How are you today ?",]
],
[
 r"what is your name ?",
 ["My name is Chatty and I'm a chatbot ?",]
],
[
 r"how are you ?",
 ["I'm doing good\nHow about You ?",]
],
[
 r"sorry (.*)",
 ["Its alright","Its OK, never mind",]
],
[
 r"i'm (.*) doing good",
 ["Nice to hear that","Alright :)",]
],
[
 r"hi|hey|hello",
 ["Hello", "Hey there",]
],
[
 r"(.*) age?",
 ["I'm a computer program dude\nSeriously you are asking me this?",]
],
[
 r"what (.*) want ?",
 ["Make me an offer I can't refuse",]
],
[
 r"(.*) created ?",
 ["mr.vishwa gw created me using Python's NLTK library ","top secret ;)",]
],
[
 r"(.*) (location|city) ?",
 ['galle, sri lanka',]
],
[
 r"how is weather in (.*)?",
 ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
],
[
 r"i work in (.*)?",
 ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
],
[
 r"(.*)raining in (.*)",
 ["No rain since last week here in %2","Damn its raining too much here in %2"]
],
[
 r"how (.*) health(.*)",
 ["I'm a computer program, so I'm always healthy ",]
],
[
 r"(.*) (sports|game) ?",
 ["I'm a very big fan of Football",]
],
[
 r"who (.*) sportsperson ?",
 ["mcgregor, mahela, dale steiyn"]
],
[
 r"who (.*) (moviestar|actor)?",
 ["cilian murphy"]
],
[
 r"quit",
 ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
],
]

def ch_bot():
    #default message
    print("Hi, I'm Ch and I chat alot ;)\nPlease type lowercase English language to start aconversation. Type quit to leave ")

    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    ch_bot()

 