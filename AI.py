import requests
import json
import openai
import streamlit as st
from streamlit_chat import message
import random
from streamlit_lottie import st_lottie
from PIL import Image
import tensorflow as tf

def Dermatologist(key, text):
    openai.api_key = key
    global typo
    typo = typo + "\n" + "Human: " +  text + "\n" + "AI: " 
    response = openai.Completion.create(
        engine="davinci",
        prompt= typo,
        temperature=0.9, 
        max_tokens=250,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["\n", " Human:", " AI:"]
    )

    answer = response.choices[0]['text']
    typo = typo + answer + "\n"
    return answer

# Opening JSON file
f = open('skin_best_model_arch.json')
data = json.load(f)

loaded_model = tf.keras.models.model_from_json(
    data, custom_objects=None
)
loaded_model.load_weights('skin_best_model.h5')

def predict(filename):
    name_list = ["akiec", "bcc", "bkl", "df", "mel", "nv", "vasc"]
    im = Image.open(filename)
    im = im.resize((224,224))
    x = tf.keras.utils.img_to_array(im)
    x = x.reshape((1,224,224,3))
    res = loaded_model.predict(x).tolist()[0]
    max = res[0]
    index = 0
    for i in range(1,len(res)):
        if res[i] > max:
            max = res[i]
            index = i
    return name_list[index]

st.set_page_config(layout = "wide")

body = st.container()

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_zrqthn6o.json")


with st.sidebar:
    key_input = st.text_input('Enter your OpenAI API ')


st.title("EYES TO GPT-3")
st.markdown("An AI - Dermatologist")
st.markdown("We will add a lot more in the future")
st.write("##")
st_lottie(lottie, height=300, key="coding")
st.write("##")
st.markdown("The Dermatologist is named Dr. Tina and Dr. Tina also has a computer vision based assistant who will help her to create or generate report for the image you will provide later.")
st.write("##")
if key_input:

    st.title("Upload the photo of your skin")
    uploaded_file = st.file_uploader("Choose a file", type=["png","jpg","jpeg"], accept_multiple_files=False, key=None, help="content image")
    st.markdown("Uploading a picture of your skin here will help us generate a report about your skin and we will send it to Dr. Tina, the Dermatologist who will help you cure all your skin based problems.")
    if uploaded_file:
        dname = predict(uploaded_file)
        typo = "The following is a conversation with Dr. Tina. Dr. Tina knows everything in dermatology and this chatbot is Dr. Tina. The chatbot alias Dr. Tina is from a Healthcare Technology Company named MUSTARD. The chatbot alias Dr. Tina should act like a professional dermatologist and ask the human many questions regarding his/her skin problem and prescribe medicines and safety measures instead of asking the human to visit a doctor. And this dermatologist alias Dr. Tina alias Chat bot has a computer vision assistant which predicted that the human is affected by " + dname +" type of skin cancer. So now this chatbot has to strongly remember that the human has "+ dname + " type skin cancer throughout the conversation. And in the beginning of the conversation the chatbot should let the patient know what type of cancer he is affected."
            
        st.header("Talk to a AI Dermatologist")
        if 'generated' not in st.session_state:
            st.session_state['generated'] = []

        if 'past' not in st.session_state:
            st.session_state['past'] = []


        with st.form("form", clear_on_submit=True):
            user_input = st.text_input('Start your conversation with a HI and end it with a BYE', '') 
            submitted = st.form_submit_button('Send')


        if submitted and user_input:
            answer = Dermatologist(key_input, user_input)
            st.session_state.past.append(user_input)
            st.session_state.generated.append(answer)

            
        message("Hi I am Dr. Tina, my computer vision assistant just predicted that you have " + dname + " type skin cancer", key=str(0)+'_bot')
        for i in range(len(st.session_state['past'])):
            message(st.session_state['past'][i], is_user=True, key=str(i+1)+'_user') 
            if len(st.session_state['generated']) > i:
                message(st.session_state['generated'][i], key=str(i+1)+'_bot')
