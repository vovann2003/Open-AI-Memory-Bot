import streamlit as st
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationEntityMemory
from langchain.chains.conversation.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE


# Function for input text
def get_text():
    input_text = st.text_input('You: ', st.session_state['input'], key='input',
                               placeholder='Your AI assistant here! Ask me anything...',
                               label_visibility='hidden')
    return input_text


# Create a new session chat and save the last sessions
def new_chat():
    info = []

    with st.expander('New Chat'):
        for i in range(len(st.session_state['generated_response']) - 1, -1, -1):
            info.append(f'User: {st.session_state["past"][i]}')
            info.append(f'Bot: {st.session_state["generated_response"][i]}')

    st.session_state['stored_session'].append(info)
    st.session_state['input'] = ''
    st.session_state['generated_response'] = []
    st.session_state['past'] = []


if 'generated_response' not in st.session_state:
    st.session_state['generated_response'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

if 'input' not in st.session_state:
    st.session_state['input'] = ''

if 'stored_session' not in st.session_state:
    st.session_state['stored_session'] = []

st.set_page_config(
    page_title='Open AI Chat Bot',
    page_icon=':parrot:'
)

# Set the title
st.title('Open AI Chat Memory Bot')
st.subheader('Produced by: LangChain🦜 and Streamlit')

# Create API key at sidebar
api = st.sidebar.text_input(label='API-Key', type='password', placeholder='Input your API Key')

# Create models for Open AI
model = st.sidebar.selectbox(label='Model', options=['gpt-3.5-turbo', 'text-davinci-003', 'text-davinci-002'])

# Create a number of conversations in memory
conversation_count = st.sidebar.slider(label='Conversations Count', min_value=1, max_value=100)

# Create new chat button
new_chat = st.sidebar.button('New Chat', on_click=new_chat)

if api:
    # Create openai model
    llm = OpenAI(
        temperature=0,
        openai_api_key=api,
        model_name=model,
    )

    # Create memory
    if 'entity_memory' not in st.session_state:
        st.session_state.entity_memory = ConversationEntityMemory(llm=llm, k=conversation_count)

    # Create conversation chain
    conversation = ConversationChain(
        llm=llm,
        prompt=ENTITY_MEMORY_CONVERSATION_TEMPLATE,
        memory=st.session_state.entity_memory
    )
else:
    st.sidebar.warning("API is not valid")

# User input
user_input = get_text()

if user_input:
    # Getting response from openai model
    response = conversation.run(user_input)

    # Add current input and response to session
    st.session_state.past.append(user_input)
    st.session_state.generated_response.append(response)

# Create container of user conversations
with st.expander('Conversation'):
    for i in range(len(st.session_state['generated_response']) - 1, -1, -1):
        st.info(st.session_state['past'][i])
        st.success(st.session_state['generated_response'][i], icon='🤖')

for i in range(len(st.session_state['stored_session']) - 1, -1, -1):
    with st.sidebar.expander(f'Conversation-Session: {i}'):
        st.write(st.session_state['stored_session'][i])

delete_btn = st.sidebar.button('Delete')

if delete_btn:
    del st.session_state['stored_session']
