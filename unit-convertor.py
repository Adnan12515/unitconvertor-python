import streamlit as st

st.title("Unit Converter")

unit_options = ["Length", "Weight", "Temperature", "Volume"]
selected_unit = st.selectbox("Select a unit", unit_options)

value = st.number_input("Enter value to convert", min_value=0.0, format="%.2f")

if selected_unit == "Length":
    unit_conversion_options = ["Meters", "Kilometers", "Feet", "Yards"]
    selected_conversion_unit = st.selectbox("Select a conversion unit", unit_conversion_options)

    conversion_factor = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Feet": 3.28084,
        "Yards": 1.0936,
    }
    if st.button("Convert"):
        converted_value = value * conversion_factor[selected_conversion_unit]
        st.write(f"{value} Meters is equal to {converted_value:.2f} {selected_conversion_unit}")

elif selected_unit == "Weight":
    unit_conversion_options = ["Kilograms", "Pounds", "Ounces"]
    selected_conversion_unit = st.selectbox("Select a conversion unit", unit_conversion_options)

    conversion_factor = {
        "Kilograms": 1,
        "Pounds": 2.20462,
        "Ounces": 35.274,
    }
    if st.button("Convert"):
        converted_value = value * conversion_factor[selected_conversion_unit]
        st.write(f"{value} Kilograms is equal to {converted_value:.2f} {selected_conversion_unit}")

elif selected_unit == "Temperature":
    unit_conversion_options = ["Celsius to Fahrenheit", "Fahrenheit to Celsius"]
    selected_conversion_unit = st.selectbox("Select a conversion type", unit_conversion_options)

    if st.button("Convert"):
        if selected_conversion_unit == "Celsius to Fahrenheit":
            converted_value = (value * 9/5) + 32
            st.write(f"{value}°C is equal to {converted_value:.2f}°F")
        else:
            converted_value = (value - 32) * 5/9
            st.write(f"{value}°F is equal to {converted_value:.2f}°C")

elif selected_unit == "Volume":
    unit_conversion_options = ["Liters", "Gallons", "Barrels"]
    selected_conversion_unit = st.selectbox("Select a conversion unit", unit_conversion_options)

    conversion_factor = {
        "Liters": 1,
        "Gallons": 0.264172,
        "Barrels": 0.00628981,
    }
    if st.button("Convert"):
        converted_value = value * conversion_factor[selected_conversion_unit]
        st.write(f"{value} Liters is equal to {converted_value:.2f} {selected_conversion_unit}")
