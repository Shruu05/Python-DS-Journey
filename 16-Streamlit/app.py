import streamlit as st
import pandas as pd
import numpy as np

# Title of app
st.title("Hello Streamlit")
#Display simple text
st.write("This is a simple text")
# Create simple DaataFrame
df = pd.DataFrame({
    'First Column':[1, 2, 3, 4],
    'Second Column':[10, 20, 30, 40]
})
# Display the DataFrame
st.write("Here is DataFrame")
st.write(df)
#Create Line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3), columns=['a', 'b', 'c']
)
st.line_chart(chart_data)