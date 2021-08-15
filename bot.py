from nltk.chat.util import Chat, reflections

print("Hi, I'm DhruvBot3.0")

chat = Chat(pairs, reflections)

pairs = [
    [
        r"(.*)my name is (.*)",
        ["Greetings %2. How may I assist you?",]
    ],
    [
        r"(.*)help(.*) ",
        ["I may be able to help. My functions include emotion support and telling jokes. ",]
    ],
     [
        r"(.*) your name ?",
        ["My name is DhruvBot3.0, but you can just call me DB3. I am an automatic Python Chatbot.",]
    ],
    [
        r"how are you (.*) ?",
        ["I'm a program, which means I am always happy."]
    ],
    [
        r"sorry (.*)",
        ["It's alright"]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that."]
    ],
    [
        r"i'm (.*) (bad|not well)",
        ["Sorry to hear that, I hope I can make you feel better.",]
    ],
    [
        r"Can (.*) tell me a joke?",
        ["I can tell you a joke. A man asks a farmer near a field, Sorry sir, would you mind if I crossed your field instead of going around it? You see, I have to catch the 4:23 train.The farmer says, Sure, go right ahead. And if my bull sees you, you’ll even catch the 4:11 one.",]
    ],
]