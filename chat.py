import streamlit as st
import spacy

from spacy.tokens import Span

nlp = spacy.load("en_core_web_sm")

st.write("NLP (Natural Language Processing) tool. Simply paste the article you wish to be processed, and choose what type of processing.")


option = st.selectbox('Which NLP ?', ['Removal of Common Words', 'Lemmatization', 'Entity Recognition'])

r_text = st.text_input("Text...", key="name")

doc = nlp(r_text)

f_text = []

match option:
    case 'Removal of Common Words':
        for token in doc:
             if not token.is_stop:
                 f_text.append(token)
    
    case 'Lemmatization':
        for token in doc:
            f_text.append(token.lemma_)

if option == "Entity Recognition":
    for ent in doc.ents:
        f_text.append(f"{ent.text} ({ent.label_})")

st.write(" ".join(str(token) for token in f_text))
                
