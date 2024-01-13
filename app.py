from txtai import Embeddings
from db_facts import get_all_facts_text, get_fact_by_text, add_fact, delete_fact, update_fact
import streamlit as st

st.set_page_config(
    page_title="Fun Facts",
    page_icon="assets/favicon.ico",
    initial_sidebar_state="expanded", 
)

if 'embeddings' not in st.session_state:
  st.session_state.embeddings = None

if 'facts' not in st.session_state:
    st.session_state.facts = get_all_facts_text()
    st.session_state.embeddings = Embeddings({"path": "sentence-transformers/nli-mpnet-base-v2"})
    st.session_state.embeddings.index(st.session_state.facts)


st.header(":violet[Fun Facts Explorer]")

with st.form(key='query_form'):
  query = st.text_input(label='What are you curious about?')
  submit_button = st.form_submit_button(label='Find Fact')

if submit_button and query != '' and st.session_state.embeddings is not None:
    with st.spinner('Searching...'):
      uid = st.session_state.embeddings.search(query,1)[0][0]
      st.markdown(f'##### :star: {st.session_state.facts[uid]}')

st.divider()

def create_add_form():
  with st.expander("Unleash Your Fact!", expanded=False):
    with st.form(key='add_form', clear_on_submit=True):
      fact = st.text_input(label="What's Your Fun Fact?", key='fact_input', )
      submit_button = st.form_submit_button(label='Add Fact', )

    if submit_button and fact != '':
      if add_fact({"fact":fact}):
        st.session_state.facts.append(fact)
        st.session_state.embeddings.index(st.session_state.facts)
        st.success('Fact added!')
      else:
        st.error('Error adding fact')


create_add_form()



    

