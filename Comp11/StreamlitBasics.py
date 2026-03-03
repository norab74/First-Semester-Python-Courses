import streamlit as st
from PIL import Image
st.title("Hello Streamlit!")

st.header("This is a header")
st.subheader("Underneath that, a subheader")
st.text("Usually online you'll find some text under subheaders, that's me.")
st.markdown("### Markdown is also supported, this is a level 3 header using markdown formatting")
st.markdown("## Level 2")
st.markdown("# Level 1")
st.success("Success")
st.info("Information")
st.warning("Warning")
st.error("Error")
exp = ZeroDivisionError("Trying to divide by zero")
st.exception(exp)
#write hardcoded text
st.write("Text with write")
#writing python inbuilt function range()
st.write(range(10))
img = Image.open("streamlit.png")
st.image(img, width=200)

#Display a checkbox with the label 'show/hide'
if st.checkbox("Show/Hide"):
    #show this text when the box is checked
    st.text("Someone touched the box")
#Create a radio button to select a gender, you may pick only one
status = st.radio("Select Gender:", ['Binary Male', 'Binary Female', 'Nonbinary Masc', 'Nonbinary Femme', 'Unlisted Neogender'])
#Display the selected option using success message
if status is not False:
    st.success(f'"{status}" selected')
    
#Create a dropdown menu for selecting a hobby
hobby = st.selectbox("Select a Hobby:", ['Extreme Mini-golf', 'Sport', '"Cowabunga-ing" off of ravines'])
st.write("Your hobby is:", hobby)

#Create a multi select box for selecting foods
food = st.multiselect("Select your favorite foods:", ['Apples', 'Bananas', 'Carrots', 'Durian', 'Eggplants'])
#Display the number of selected hobbies
st.write("You've selected", len(food), "foods")

#a simple button, it does nothing at all
st.button("Don't click me, I'm useless")

#A button which displays text when clicked
if st.button("Click me"):
    st.text("Oh shit you actually did it, absolute madlad")
    
#Create a text input box with a default placeholder
name = st.text_input("Enter yo name fool", "Type that shit right here...")

#Display the name after clicking the submit button
if st.button("Submit"):
    result = name.title()
    st.success(f"Ah, so your name is '{result}'?")
    
#Creater a slider to select a level between 1 and 5
level = st.slider("Choose a level", min_value=1, max_value=5)

#Display the selected level
st.write(f"Selected Level: {level}")
