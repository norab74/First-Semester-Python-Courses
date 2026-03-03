import streamlit as st

#Title the app
st.title("BMI Calculator")

#Input: Weight format selection
weight_unit = st.radio("Select a unit of measurement:", ["Pounds", "Kilograms"])

# Input: Weight in Kilograms
weight = st.number_input(f"Enter your weight in {weight_unit}:", min_value=0.0, format="%.2f")

#Input: Height format selection
height_unit = st.radio("Select a unit of measurement:", ["Centimeters", "Meters", "Feet"])

#Input: Height value based on selected unit
height = st.number_input(f"Enter your height in {height_unit.lower()}:", min_value=0.0, format="%.2f")

#Calculate BMI when a button is pressed
if st.button("Calculate BMI"):
    try:
        #convert height to meters based on selected unit
        if height_unit == "Centimeters":
            height_m = height / 100
        elif height_unit == "Feet":
            height_m = height / 3.28
        else:
            height_m = height
        #Convert pountd to kilograms if needed
        if weight_unit == "Pounds":
            weight_kg = weight / 2.205
        else: 
            weight_kg = weight
        #Prevent division by zero errors
        if height_m <= 0:
            st.error("Height must be greater than zero.")
        else:
            bmi= weight_kg / (height_m **2)
            st.success(f"Your BMI is {bmi:.2f}")
            
            # BMI interpretation
            if bmi < 16:
                st.error("You are Very Underweight, seek medical advice")
            elif 16 <= bmi < 18.5:
                st.warning("You are somewhat underweight")
            elif 18.5 <= bmi < 25:
                st.success("Your BMI is in the healthy range")
            elif 25 <= bmi < 30:
                st.warning("You are somewhat overweight")
            else:
                st.error("You are Very Overweight, seek medical advice")
    except:
        st.error("Please enter valid numeric values.")
