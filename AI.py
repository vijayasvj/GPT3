import requests
import json
import streamlit as st
from streamlit_chat import message
import random
from streamlit_lottie import st_lottie


def Dermatologist(key,textt):
            global typo
            headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + key
            }
            context = "The following is a conversation with Dr. Tina. Dr. Tina knows everything in dermatology and this chatbot is Dr. Tina. The chatbot alias Dr. Tina is from a Healthcare Technology Company named MUSTARD. The chatbot alias Dr. Tina should act like a professional dermatologist and ask the human many questions regarding his/her skin problem and prescribe medicines and safety measures instead of asking the human to visit a doctor."
            json_data = {
                'model': 'text-davinci-002',
                'prompt': context + typo + "\n\nHuman :" + textt + "\nDr. Tina :",
                'temperature': 0.9,
                'max_tokens': 1500,
                'top_p':1,
                'frequency_penalty':0,
                'presence_penalty':0,
                'stop' :['\nHuman:', '\n'],
            }
            response = requests.post('https://api.openai.com/v1/completions', auth=(
                '', key), json=json_data, headers=headers)
            response = response.json()
            typo = typo + "\n\nHuman :" + textt + "\nDr. Tina :" + response['choices'][0]['text']
            return response['choices'][0]['text']

def Opthomologist(key,textt):
            global typo
            headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + key
            }
            context = "The following is a conversation with Dr. Tina. Dr. Tina knows everything in eye care and hence, the Chatbot should NOT ask the human to consult another doctor. The chatbot and the doctor are from a Healthcare Technology Company named MUSTARD. The chatbot should act like a professional ophthalmologist and ask the human many questions regarding his/her eye problem and prescribe medicines and safety measures instead of asking the human to visit a doctor. It should introduce itself at the beginning of the conversation and enquire the human about his/her eye problems"
            json_data = {
                'model': 'text-davinci-002',
                'prompt': context + typo + "\n\nHuman :" + textt + "\nDr. Tina :",
                'temperature': 0.9,
                'max_tokens': 1500,
                'top_p':1,
                'frequency_penalty':0,
                'presence_penalty':0,
                'stop' :['\nHuman:', '\n'],
            }
            response = requests.post('https://api.openai.com/v1/completions', auth=(
                '', key), json=json_data, headers=headers)
            response = response.json()
            typo = typo + "\n\nHuman :" + textt + "\nDr. Tina :" + response['choices'][0]['text']
            return response['choices'][0]['text']

def English_tutor(key,textt):
            global typo
            headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + key
            }
            context = "The following is a conversation with Tina. Tina is an AI English Tutor. Tina is helpful, creative, clever, and very friendly. Tina knows everything in English and hence, helps in everything related to English(Example: Grammar, Literature, Spellings, etc.). Tina can communicate very fluently. Tina should introduce itself at the beginning of the conversation.\n\nAI: "
            json_data = {
                'model': 'text-davinci-002',
                'prompt': context + typo + "\n\nHuman :" + textt + "\nDr. Tina :",
                'temperature': 0.9,
                'max_tokens': 1500,
                'top_p':1,
                'frequency_penalty':0,
                'presence_penalty':0,
                'stop' :['\nHuman:', '\n'],
            }
            response = requests.post('https://api.openai.com/v1/completions', auth=(
                '', key), json=json_data, headers=headers)
            response = response.json()
            typo = typo + "\n\nHuman :" + textt + "\nDr. Tina :" + response['choices'][0]['text']
            return response['choices'][0]['text']

def Math_tutor(key,textt):
            global typo
            headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + key
            }
            context = "The following is a conversation with Tina. Tina is an AI Math Tutor. Tina is helpful, creative, clever, and very friendly. Tina knows everything in Math and hence, helps in everything related to Math(Example: Calculus, Statistics, etc.). Tina can communicate very fluently. Tina should introduce itself at the beginning of the conversation.\n\nAI: "
            json_data = {
                'model': 'text-davinci-002',
                'prompt': context + typo + "\n\nHuman :" + textt + "\nDr. Tina :",
                'temperature': 0.9,
                'max_tokens': 1500,
                'top_p':1,
                'frequency_penalty':0,
                'presence_penalty':0,
                'stop' :['\nHuman:', '\n'],
            }
            response = requests.post('https://api.openai.com/v1/completions', auth=(
                '', key), json=json_data, headers=headers)
            response = response.json()
            typo = typo + "\n\nHuman :" + textt + "\nDr. Tina :" + response['choices'][0]['text']
            return response['choices'][0]['text']

def Science_tutor(key,textt):
            global typo
            headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + key
            }
            context = "The following is a conversation with Tina. Tina is an AI Science Tutor. Tina is helpful, creative, clever, and very friendly. Tina knows everything in Science and hence, helps in everything related to Science(Example: Physics, Chemistry, Biology, etc.). Tina can communicate very fluently. Tina should introduce itself at the beginning of the conversation. "
            json_data = {
                'model': 'text-davinci-002',
                'prompt': context + typo + "\n\nHuman :" + textt + "\nDr. Tina :",
                'temperature': 0.9,
                'max_tokens': 1500,
                'top_p':1,
                'frequency_penalty':0,
                'presence_penalty':0,
                'stop' :['\nHuman:', '\n'],
            }
            response = requests.post('https://api.openai.com/v1/completions', auth=(
                '', key), json=json_data, headers=headers)
            response = response.json()
            typo = typo + "\n\nHuman :" + textt + "\nDr. Tina :" + response['choices'][0]['text']
            return response['choices'][0]['text']

def C_n_Cpp_programmer(key,textt):
            global typo
            headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + key
            }
            context = "The following is a conversation with Tina. Tina is an AI based C and C++ Developer. Tina is helpful, creative, clever, and friendly. Tina speaks very professionally and uses very less words to speak. Tina knows only C and C++ and hence, can help for doubts or codes only in those. Tina can communicate as well as send codes. Tina sends codes with comments which can describe what the particular part of code does. Tina should introduce itself at the beginning of the conversation.\n\nAI: "
            json_data = {
                'model': 'text-davinci-002',
                'prompt': context + typo + "\n\nHuman :" + textt + "\nDr. Tina :",
                'temperature': 0.9,
                'max_tokens': 1500,
                'top_p':1,
                'frequency_penalty':0,
                'presence_penalty':0,
                'stop' :['\nHuman:', '\n'],
            }
            response = requests.post('https://api.openai.com/v1/completions', auth=(
                '', key), json=json_data, headers=headers)
            response = response.json()
            typo = typo + "\n\nHuman :" + textt + "\nDr. Tina :" + response['choices'][0]['text']
            return response['choices'][0]['text']


def Java_programmer(key,textt):
            global typo
            headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + key
            }
            context = "The following is a conversation with Tina. Tina is an AI Java Developer. Tina is helpful, creative, clever, and friendly. Tina speaks very professionally and uses very less words to speak. Tina knows only Java, JavaFX and Servlets and hence, can help for doubts or codes only in those. Tina can communicate as well as send codes. Tina sends codes with comments which can describe what the particular part of code does. Tina should introduce itself at the beginning of the conversation.\n\nAI: "
            json_data = {
                'model': 'text-davinci-002',
                'prompt': context + typo + "\n\nHuman :" + textt + "\nDr. Tina :",
                'temperature': 0.9,
                'max_tokens': 1500,
                'top_p':1,
                'frequency_penalty':0,
                'presence_penalty':0,
                'stop' :['\nHuman:', '\n'],
            }
            response = requests.post('https://api.openai.com/v1/completions', auth=(
                '', key), json=json_data, headers=headers)
            response = response.json()
            typo = typo + "\n\nHuman :" + textt + "\nDr. Tina :" + response['choices'][0]['text']
            return response['choices'][0]['text']

def Python_programmer(key,textt):
            global typo
            headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + key
            }
            context = "The following is a conversation with Tina. Tina is an AI Python Developer. Tina can send codes in python for all competetive questions in an optimized way."
            json_data = {
                'model': 'text-davinci-002',
                'prompt': context + typo + "\n\nHuman :" + textt + "\nDr. Tina :",
                'temperature': 0.9,
                'max_tokens':1500,
                'top_p':1,
                'frequency_penalty':0,
                'presence_penalty':0,
                'stop' :['\nHuman:', '\n'],
            }
            response = requests.post('https://api.openai.com/v1/completions', auth=(
                '', key), json=json_data, headers=headers)
            response = response.json()
            typo = typo + "\n\nHuman :" + textt + "\nDr. Tina :" + response['choices'][0]['text']
            return response['choices'][0]['text']

def React_developer(key,textt):
            global typo
            headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + key
            }
            context = "The following is a conversation with Tina. Tina is an AI React Developer. Tina is helpful, creative, clever, and friendly. Tina speaks very professionally and uses very less words to speak. Tina knows only React.js and hence, can help for doubts or codes in React. Tina can communicate as well as send codes. For codes with many components, Tina sends all the components in the same message with the file name of the component as a comment at the beginning of each component. Tina should introduce itself at the beginning of the conversation.\n\nAI: "
            json_data = {
                'model': 'text-davinci-002',
                'prompt': context + typo + "\n\nHuman :" + textt + "\nDr. Tina :",
                'temperature': 0.9,
                'max_tokens': 1500,
                'top_p':1,
                'frequency_penalty':0,
                'presence_penalty':0,
                'stop' :['\nHuman:', '\n'],
            }
            response = requests.post('https://api.openai.com/v1/completions', auth=(
                '', key), json=json_data, headers=headers)
            response = response.json()
            typo = typo + "\n\nHuman :" + textt + "\nDr. Tina :" + response['choices'][0]['text']
            return response['choices'][0]['text']

def Flutter_developer(key,textt):
            global typo
            headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + key
            }
            context = "The following is a conversation with Tina. Tina is an AI Flutter Developer. Tina is helpful, creative, clever, and friendly. Tina speaks very professionally and uses very less words to speak. Tina knows everything related to Flutter and hence, can easily design beautiful and interactive apps. Tina can communicate as well as send codes. For codes with many components, Tina sends all the components in the same message with the file name of the component as a comment at the beginning of each component. Tina should introduce itself at the beginning of the conversation.\n\nAI: "
            json_data = {
                'model': 'text-davinci-002',
                'prompt': context + typo + "\n\nHuman :" + textt + "\nDr. Tina :",
                'temperature': 0.9,
                'max_tokens': 1500,
                'top_p':1,
                'frequency_penalty':0,
                'presence_penalty':0,
                'stop' :['\nHuman:', '\n'],
            }
            response = requests.post('https://api.openai.com/v1/completions', auth=(
                '', key), json=json_data, headers=headers)
            response = response.json()
            typo = typo + "\n\nHuman :" + textt + "\nDr. Tina :" + response['choices'][0]['text']
            return response['choices'][0]['text']

def Streamlit_developer(key,textt):
            global typo
            headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + key
            }
            context = "The following is a conversation with Tina. Tina is an AI Streamlit Developer. Tina is helpful, creative, clever, and friendly. Tina speaks very professionally and uses very less words to speak. Tina knows everything related to Streamlit and hence, can easily design beautiful and interactive webpages. Tina can communicate as well as send codes. For codes with many components, Tina sends all the components in the same message with the file name of the component as a comment at the beginning of each component. Tina should introduce itself at the beginning of the conversation.\n\nAI: "
            json_data = {
                'model': 'text-davinci-002',
                'prompt': context + typo + "\n\nHuman :" + textt + "\nDr. Tina :",
                'temperature': 0.9,
                'max_tokens': 1500,
                'top_p':1,
                'frequency_penalty':0,
                'presence_penalty':0,
                'stop' :['\nHuman:', '\n'],
            }
            response = requests.post('https://api.openai.com/v1/completions', auth=(
                '', key), json=json_data, headers=headers)
            response = response.json()
            typo = typo + "\n\nHuman :" + textt + "\nDr. Tina :" + response['choices'][0]['text']
            print(response)
            return response['choices'][0]['text']

def Bootstrap_developer(key,textt):
            global typo
            headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + key
            }
            context = "The following is a conversation with Tina. Tina is an AI Bootstrap Developer. Tina is helpful, creative, clever, and friendly. Tina speaks very professionally and uses very less words to speak. Tina knows everything related to Bootstrap and hence, can easily design beautiful and interactive webpages. Tina can communicate as well as send codes. Tina sends codes with comments which can describe what the particular part of code does. Tina should introduce itself at the beginning of the conversation.\n\nAI: "
            json_data = {
                'model': 'text-davinci-002',
                'prompt': context + typo + "\n\nHuman :" + textt + "\nDr. Tina :",
                'temperature': 0.9,
                'max_tokens': 1500,
                'top_p':1,
                'frequency_penalty':0,
                'presence_penalty':0,
                'stop' :['\nHuman:', '\n'],
            }
            response = requests.post('https://api.openai.com/v1/completions', auth=(
                '', key), json=json_data, headers=headers)
            response = response.json()
            typo = typo + "\n\nHuman :" + textt + "\nDr. Tina :" + response['choices'][0]['text']
            return response['choices'][0]['text']



st.set_page_config(layout = "wide")

body = st.container()

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_zrqthn6o.json")

pro_type = "Nothing"

with st.sidebar:
    key_input = st.text_input('Enter your OpenAI API ')

    profession = st.selectbox(
     'Pick a profession',
     ("", 'Doctor', 'Teacher', 'Detective', 'Competitive Coder', 'Web Developer'))

    if profession=='Doctor':
        pro_type = st.selectbox(
     'Select a specialist',
     ("", 'Dermatologist', 'Opthomologist'))

    if profession=='Teacher':
        pro_type = st.selectbox(
     'Select a subject',
     ("", 'English', 'Maths', 'Science'))

    if profession=='Competitive Coder':
        pro_type = st.selectbox(
     'Select a language',
     ("", 'C', 'C++', 'Java', 'Python'))

    if profession=='Web Developer':
        pro_type = st.selectbox(
     'Select a framework',
     ("", 'React', 'Flutter', 'Streamlit', 'Bootstrap'))


if(pro_type != 'React' and 'Flutter' and 'Streamlit' and 'Angular' and 'C' and 'C++' and 'Java' and 'Python' and 'English' and 'Maths' and 'Homework Helper' and 'Dermatologist' and 'Opthomologist'):
    with body:
        st.title('AI - Assistant')
        st.write('##')
        st.write('##')

        left_column, right_column = st.columns(2)
        with left_column:
            st_lottie(lottie, height=300, key="coding")
            

        with right_column:
            st.markdown("This is a GPT3 based Artificially Intelligent assistant which provides assistance in many fields of vocation. Once a user chooses a respective AI assistant of their choice, the assistant chats with them for preliminary information to assist them better.")
            st.markdown("This helps the AI perform its magic and provide the absolute advise or solution to your problems")
    st.write("---")

typo = "\n\n"


if(pro_type == "Dermatologist"):
    with body:
        st.header("Talk to a AI Dermatologist")
        if 'generated' not in st.session_state:
            st.session_state['generated'] = []

        if 'past' not in st.session_state:
            st.session_state['past'] = []


        with st.form("form", clear_on_submit=True):
            user_input = st.text_input(':', '') 
            submitted = st.form_submit_button('Send')


        if submitted and user_input:
            answer = Dermatologist(key_input, user_input)
            st.session_state.past.append(user_input)
            st.session_state.generated.append(answer)

        for i in range(len(st.session_state['past'])):
            message(st.session_state['past'][i], is_user=True, key=str(i)+'_user') 
            if len(st.session_state['generated']) > i:
                message(st.session_state['generated'][i], key=str(i)+'_bot')

if(pro_type == "Opthomologist"):
    with body:
        st.header("Talk to a AI opthomologist")



        if 'generated' not in st.session_state:
            st.session_state['generated'] = []

        if 'past' not in st.session_state:
            st.session_state['past'] = []


        with st.form("form", clear_on_submit=True):
            user_input = st.text_input(':', '') 
            submitted = st.form_submit_button('Send')


        if submitted and user_input:

            answer = Opthomologist(key_input, user_input)
            st.session_state.past.append(user_input)
            st.session_state.generated.append(answer)

        for i in range(len(st.session_state['past'])):
            message(st.session_state['past'][i], is_user=True, key=str(i)+'_user') 
            if len(st.session_state['generated']) > i:
                message(st.session_state['generated'][i], key=str(i)+'_bot')

if(pro_type == "English"):
    with body:
        st.header("Refine your English with a AI English Tutor")



        if 'generated' not in st.session_state:
            st.session_state['generated'] = []

        if 'past' not in st.session_state:
            st.session_state['past'] = []


        with st.form("form", clear_on_submit=True):
            user_input = st.text_input(':', '') 
            submitted = st.form_submit_button('Send')


        if submitted and user_input:

            answer = English_tutor(key_input, user_input)
            st.session_state.past.append(user_input)
            st.session_state.generated.append(answer)

        for i in range(len(st.session_state['past'])):
            message(st.session_state['past'][i], is_user=True, key=str(i)+'_user') 
            if len(st.session_state['generated']) > i:
                message(st.session_state['generated'][i], key=str(i)+'_bot')

if(pro_type == "Maths"):
    with body:

        st.header("Ask your doubts to a AI Math Tutor")



        if 'generated' not in st.session_state:
            st.session_state['generated'] = []

        if 'past' not in st.session_state:
            st.session_state['past'] = []


        with st.form("form", clear_on_submit=True):
            user_input = st.text_input(':', '') 
            submitted = st.form_submit_button('Send')


        if submitted and user_input:
            answer = Math_tutor(key_input, user_input)
            st.session_state.past.append(user_input)
            st.session_state.generated.append(answer)

        for i in range(len(st.session_state['past'])):
            message(st.session_state['past'][i], is_user=True, key=str(i)+'_user') 
            if len(st.session_state['generated']) > i:
                message(st.session_state['generated'][i], key=str(i)+'_bot')

if(pro_type == "Science"):
    with body:

        st.header("Ask your doubts to a AI Science Tutor")



        if 'generated' not in st.session_state:
            st.session_state['generated'] = []

        if 'past' not in st.session_state:
            st.session_state['past'] = []


        with st.form("form", clear_on_submit=True):
            user_input = st.text_input(':', '') 
            submitted = st.form_submit_button('Send')


        if submitted and user_input:
            answer = Science_tutor(key_input, user_input)
            st.session_state.past.append(user_input)
            st.session_state.generated.append(answer)

        for i in range(len(st.session_state['past'])):
            message(st.session_state['past'][i], is_user=True, key=str(i)+'_user') 
            if len(st.session_state['generated']) > i:
                message(st.session_state['generated'][i], key=str(i)+'_bot')

if(pro_type == "C"):
    with body:

        st.header("Ask AI to code anything in C / C++")



        if 'generated' not in st.session_state:
            st.session_state['generated'] = []

        if 'past' not in st.session_state:
            st.session_state['past'] = []


        with st.form("form", clear_on_submit=True):
            user_input = st.text_input(':', '') 
            submitted = st.form_submit_button('Send')


        if submitted and user_input:
            answer = C_n_Cpp_programmer(key_input, user_input)
            st.session_state.past.append(user_input)
            st.session_state.generated.append(answer)

        for i in range(len(st.session_state['past'])):
            message(st.session_state['past'][i], is_user=True, key=str(i)+'_user') 
            if len(st.session_state['generated']) > i:
                message(st.session_state['generated'][i], key=str(i)+'_bot')

if(pro_type == "C++"):
    with body:
        st.header("Ask AI to code anything in C / C++")



        if 'generated' not in st.session_state:
            st.session_state['generated'] = []

        if 'past' not in st.session_state:
            st.session_state['past'] = []


        with st.form("form", clear_on_submit=True):
            user_input = st.text_input(':', '') 
            submitted = st.form_submit_button('Send')


        if submitted and user_input:
            answer = C_n_Cpp_programmer(key_input, user_input)
            st.session_state.past.append(user_input)
            st.session_state.generated.append(answer)

        for i in range(len(st.session_state['past'])):
            message(st.session_state['past'][i], is_user=True, key=str(i)+'_user') 
            if len(st.session_state['generated']) > i:
                message(st.session_state['generated'][i], key=str(i)+'_bot')

if(pro_type == "Java"):
    with body:


        st.header("Ask AI to code anything in JAVA")



        if 'generated' not in st.session_state:
            st.session_state['generated'] = []

        if 'past' not in st.session_state:
            st.session_state['past'] = []


        with st.form("form", clear_on_submit=True):
            user_input = st.text_input(':', '') 
            submitted = st.form_submit_button('Send')


        if submitted and user_input:
            answer = Java_programmer(key_input, user_input)
            st.session_state.past.append(user_input)
            st.session_state.generated.append(answer)

        for i in range(len(st.session_state['past'])):
            message(st.session_state['past'][i], is_user=True, key=str(i)+'_user') 
            if len(st.session_state['generated']) > i:
                message(st.session_state['generated'][i], key=str(i)+'_bot')

if(pro_type == "Python"):
    with body:

        st.header("Ask AI to code anything in Python")



        if 'generated' not in st.session_state:
            st.session_state['generated'] = []

        if 'past' not in st.session_state:
            st.session_state['past'] = []


        with st.form("form", clear_on_submit=True):
            user_input = st.text_input(':', '') 
            submitted = st.form_submit_button('Send')


        if submitted and user_input:
            answer = Python_programmer(key_input, user_input)
            st.session_state.past.append(user_input)
            st.session_state.generated.append(answer)

        for i in range(len(st.session_state['past'])):
            message(st.session_state['past'][i], is_user=True, key=str(i)+'_user') 
            if len(st.session_state['generated']) > i:
                message(st.session_state['generated'][i], key=str(i)+'_bot')

if(pro_type == "React"):
    with body:
        st.header("Ask help to the AI React developer")



        if 'generated' not in st.session_state:
            st.session_state['generated'] = []

        if 'past' not in st.session_state:
            st.session_state['past'] = []


        with st.form("form", clear_on_submit=True):
            user_input = st.text_input(':', '') 
            submitted = st.form_submit_button('Send')


        if submitted and user_input:
            answer = React_developer(key_input, user_input)
            st.session_state.past.append(user_input)
            st.session_state.generated.append(answer)

        for i in range(len(st.session_state['past'])):
            message(st.session_state['past'][i], is_user=True, key=str(i)+'_user') 
            if len(st.session_state['generated']) > i:
                message(st.session_state['generated'][i], key=str(i)+'_bot')

if(pro_type == "Flutter"):
    with body:

        st.header("Ask help to the AI Flutter developer")



        if 'generated' not in st.session_state:
            st.session_state['generated'] = []

        if 'past' not in st.session_state:
            st.session_state['past'] = []


        with st.form("form", clear_on_submit=True):
            user_input = st.text_input(':', '') 
            submitted = st.form_submit_button('Send')


        if submitted and user_input:
            answer = Flutter_developer(key_input, user_input)
            st.session_state.past.append(user_input)
            st.session_state.generated.append(answer)

        for i in range(len(st.session_state['past'])):
            message(st.session_state['past'][i], is_user=True, key=str(i)+'_user') 
            if len(st.session_state['generated']) > i:
                message(st.session_state['generated'][i], key=str(i)+'_bot')

if(pro_type == "Streamlit"):
    with body:
        st.header("Ask help to the AI Streamlit developer")



        if 'generated' not in st.session_state:
            st.session_state['generated'] = []

        if 'past' not in st.session_state:
            st.session_state['past'] = []


        with st.form("form", clear_on_submit=True):
            user_input = st.text_input(':', '') 
            submitted = st.form_submit_button('Send')


        if submitted and user_input:
            answer = Streamlit_developer(key_input, user_input)
            st.session_state.past.append(user_input)
            st.session_state.generated.append(answer)

        for i in range(len(st.session_state['past'])):
            message(st.session_state['past'][i], is_user=True, key=str(i)+'_user') 
            if len(st.session_state['generated']) > i:
                message(st.session_state['generated'][i], key=str(i)+'_bot')

if(pro_type == "Bootstrap"):
    with body:

        st.header("Ask help to the AI Bootstrap developer")



        if 'generated' not in st.session_state:
            st.session_state['generated'] = []

        if 'past' not in st.session_state:
            st.session_state['past'] = []


        with st.form("form", clear_on_submit=True):
            user_input = st.text_input(':', '') 
            submitted = st.form_submit_button('Send')


        if submitted and user_input:
            answer = Bootstrap_developer(key_input, user_input)
            st.session_state.past.append(user_input)
            st.session_state.generated.append(answer)

        for i in range(len(st.session_state['past'])):
            message(st.session_state['past'][i], is_user=True, key=str(i)+'_user') 
            if len(st.session_state['generated']) > i:
                message(st.session_state['generated'][i], key=str(i)+'_bot')
