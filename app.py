
import streamlit as st
import google.generativeai as genai

# Configure API Key
genai.configure(api_key="AIzaSyCLdje77mjIsdSB0W8PNDXpj5K5ntJ3ieo")

# Function to generate content
def generate_content(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI

if "signup" not in st.session_state:
    st.session_state.signup=False

if st.sidebar.button("signup"):
    st.session_state.signup=True



if st.session_state.signup:
    emailid= st.sidebar.text_input("Enter your Email id here")
    password = st.sidebar.text_input("Set password here",type="password")
    confirmpass = st.sidebar.text_input("Confirm password here",type="password")

    if "createaccount" not in st.session_state:
        st.session_state.createaccount=False

    if st.sidebar.button("createaccount"):
        st.session_state.createaccount=True

    if st.session_state.createaccount:
        if not emailid or not password or not confirmpass :
            st.sidebar.error("Please Fill all the fields!!")
        elif "@gmail.com" not in emailid:
            st.sidebar.error("Email should contain @gmail.com")

        elif not  any(char.isupper() for char in password):
            st.sidebar.error("Password should contain atleast one upper case character!!!")
        elif not  any(char.islower() for char in password):
            st.sidebar.error("Password should contain atleast one lower case character!!!")
        elif not  any(char.isdigit() for char in password):
            st.sidebar.error("Password should contain atleast one digit!!!")
        elif not  any(char in "!@#$%^&*()-_+=<>?/{}[]" for char in password):
            st.sidebar.error("Password should contain atleast one !@#$%^&*()-_+=<>?/{}[] character!!!")
        elif not len(password)>7 :
            st.sidebar.error("Password should contain more than 7 characters")

        elif password==confirmpass:
            st.sidebar.success("Account Created!!")
            st.sidebar.write("Data Stored in file!!! Thankyou!!!")
        else:
            st.sidebar.warning("Password and Confirm pass doesn't match!!")




st.sidebar.button("Sign in")
st.title("AI-Powered Content Generator 🚀")
# upload_file=st.file_uploader("Input your file TXT, PDF, DOCX, CSV,JSON")
# uploaded_file=upload_file.read()
st.write("Generate high-quality content in seconds using Google Gemini AI!")

# User Inputs
topic = st.text_input("Enter a topic for content generation:")
tone = st.selectbox("Choose the tone:", ["Professional", "Casual", "Humorous", "Persuasive"])
length = st.selectbox("Choose the length:", ["Short", "Medium", "Long"])

if st.button("Generate Content"):
    prompt = f"Write a {length} article on '{topic}' in a {tone} tone."
    output = generate_content(prompt)
    st.subheader("Generated Content:")
    count= len(output.split())
    st.write("total count is:-",count,"words")
    st.write(output)


    # Save output to a file
    file_name = f"{topic.replace(' ', '_')}_content.txt"
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(output)
    st.success(f"✅ Content saved as '{file_name}'")

import streamlit as st
import google.generativeai as genai

# Configure API Key
genai.configure(api_key="AIzaSyCLdje77mjIsdSB0W8PNDXpj5K5ntJ3ieo")

# Function to generate content
def generate_content(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI

if "signup" not in st.session_state:
    st.session_state.signup=False

if st.sidebar.button("signup"):
    st.session_state.signup=True



if st.session_state.signup:
    emailid= st.sidebar.text_input("Enter your Email id here")
    password = st.sidebar.text_input("Set password here",type="password")
    confirmpass = st.sidebar.text_input("Confirm password here",type="password")

    if "createaccount" not in st.session_state:
        st.session_state.createaccount=False

    if st.sidebar.button("createaccount"):
        st.session_state.createaccount=True

    if st.session_state.createaccount:
        if not emailid or not password or not confirmpass :
            st.sidebar.error("Please Fill all the fields!!")
        elif "@gmail.com" not in emailid:
            st.sidebar.error("Email should contain @gmail.com")

        elif not  any(char.isupper() for char in password):
            st.sidebar.error("Password should contain atleast one upper case character!!!")
        elif not  any(char.islower() for char in password):
            st.sidebar.error("Password should contain atleast one lower case character!!!")
        elif not  any(char.isdigit() for char in password):
            st.sidebar.error("Password should contain atleast one digit!!!")
        elif not  any(char in "!@#$%^&*()-_+=<>?/{}[]" for char in password):
            st.sidebar.error("Password should contain atleast one !@#$%^&*()-_+=<>?/{}[] character!!!")
        elif not len(password)>7 :
            st.sidebar.error("Password should contain more than 7 characters")

        elif password==confirmpass:
            st.sidebar.success("Account Created!!")
            st.sidebar.write("Data Stored in file!!! Thankyou!!!")
        else:
            st.sidebar.warning("Password and Confirm pass doesn't match!!")




st.sidebar.button("Sign in")
st.title("AI-Powered Content Generator 🚀")
# upload_file=st.file_uploader("Input your file TXT, PDF, DOCX, CSV,JSON")
# uploaded_file=upload_file.read()
st.write("Generate high-quality content in seconds using Google Gemini AI!")

# User Inputs
topic = st.text_input("Enter a topic for content generation:")
tone = st.selectbox("Choose the tone:", ["Professional", "Casual", "Humorous", "Persuasive"])
length = st.selectbox("Choose the length:", ["Short", "Medium", "Long"])

if st.button("Generate Content"):
    prompt = f"Write a {length} article on '{topic}' in a {tone} tone."
    output = generate_content(prompt)
    st.subheader("Generated Content:")
    count= len(output.split())
    st.write("total count is:-",count,"words")
    st.write(output)


    # Save output to a file
    file_name = f"{topic.replace(' ', '_')}_content.txt"
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(output)
    st.success(f"✅ Content saved as '{file_name}'")

