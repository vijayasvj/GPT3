## Usage of Daisi

It is recommended to use this application on the daisi platform itself using the link https://app.daisi.io/daisies/vijay/GPT-3/app. However, you can still use your own editor using the below method:

### First, load the Packages:

```
import pydaisi as pyd
eyes_to_gpt_3 = pyd.Daisi("vijay/EYES TO GPT-3")
```

### Now, connect to Daisi and access the functions using the following functions:

Image Prediction:

```
eyes_to_gpt_3.predict(filename).value
```

Reply of Dermatologist:

```
gpt_3.Dermatologist(key, text).value
```

### In order to access Chatbot:

```
while text != "bye":
    reply = gpt_3.<botname>(key, context).value
    //Example code: reply = gpt_3.Dermatologist(key, context).value
    context = context + reply
    print(dna + reply)
    text = input("You: ")
    context = context + text
```

Use the above code to make the chatbot run until the input is "bye".

## And done! We have the GPT-3 Chatbot ready!
