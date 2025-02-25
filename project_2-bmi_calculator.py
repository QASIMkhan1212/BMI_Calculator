import streamlit as st 
import pandas as pd 

st.title("BMI Calculator")
height = st.slider("Enter your height (in cm)" , 100, 300 , 150)
weight = st.slider("Enter your weight (in kg)", 40 , 200 , 60)

bmi = weight / ((height/100)**2)
st.write(f"### Your BMI is {bmi:.2f}")

if bmi < 18.5:
  st.write("## You are Underweight.go and eat something")
elif 18.5 <= bmi < 24.9:
  st.write("## Congrats! you have a Normal Weight")
elif 25 <= bmi < 29.9:
  st.write("##  You are Overweight.keep an eye on your diet")
else:
  st.write("##  You have Obesity.Go and do some exercise")
  
st.write("## BMI Categories :- ###")
st.write(" - Underweight:BMI less than 18.5")
st.write(" - Normal weight: BMI between 18.5 and 24.9")
st.write(" - overweight:BMI between 25 and 29.9")
st.write(" - Obesity: BMI 30 or greater")
