import streamlit as st

st.title("My Streamlit App")
st.write("Welcome to my Streamlit application! This is a simple app to demonstrate the capabilities of Streamlit.")

name = st.text_input("Enter your name:")
st.write("Hello,", name)

age = st.number_input("Enter your age:")
st.write("Your age is", age)

if st.button("Click Me"):
    st.write("You clicked the button! 🎉")

number = st.slider("Pick a number", 0, 100)
st.write("You picked:", number)

city = st.selectbox("Choose your city", ["Chennai", "Delhi", "Mumbai"])
st.write("You selected:", city)

agree = st.checkbox("I agree to the terms")
if agree:
    st.write("Thank you for agreeing!")

st.success("This is a success message (green).")
st.info("This is an info message (blue).")
st.warning("This is a warning message (yellow).")
st.error("This is an error message (red).")

# 1. Title
st.title("BMI Calculator")
st.write("Enter your details to calculate your BMI.")

# 2. Get inputs from the user
weight = st.number_input("Enter your weight (kg):", min_value=1.0)
height = st.number_input("Enter your height (meters):", min_value=0.1)

# 3. Button to calculate
if st.button("Calculate BMI"):
    bmi = weight / (height * height)
    st.write("Your BMI is:", round(bmi, 2))

    # 4. Give a message based on the result
    if bmi < 18.5:
        st.warning("You are underweight.")
    elif bmi < 25:
        st.success("You have a normal weight. 👌")
    else:
        st.error("You are overweight.")