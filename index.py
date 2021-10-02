import streamlit as st
import numpy as np
import pandas as pd
from sklearn import tree

st.set_page_config(
    page_title="Predict App",
    page_icon=":smiley:",
    layout="centered",
)

st.write("""
# :sunglasses: Predict apple or orange? :sunglasses:
""")

weight = st.text_input("Weight", "Please enter weight...")

option = st.selectbox(
    'Choose the skin',
    ('Smooth', 'Bumpy'))
st.write('Your weight entered:', weight)
st.write('Your skin selected:', option)

submit = st.button('Enter')


def clicked():
    features = [[140, 1], [130, 1], [150, 0], [170, 0]]
    labels = [0, 0, 1, 1]

    if weight == "":
        st.write("Please enter weight :(")
    else:
        if option == 'Smooth':
            skin = 1
        else:
            skin = 0

        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(features, labels)
        x = clf.predict([[weight, skin]])

        if x == 0:
            st.write("""# This is a apple! :apple:""")
        else:
            st.write("""# This is a orange! :tangerine:""")


if submit:
    st.write('I predict this is...')
    clicked()
