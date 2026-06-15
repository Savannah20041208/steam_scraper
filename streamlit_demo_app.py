import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Streamlit Demo", layout="wide")

st.title("Streamlit Demo")
st.write("这是一个用于验证 Streamlit 运行环境的示例页面。")

values = pd.DataFrame(
    {
        "category": ["A", "B", "C", "D"],
        "value": [12, 19, 7, 15],
    }
)

fig = px.bar(values, x="category", y="value", title="Demo Chart")
st.plotly_chart(fig, use_container_width=True)

number = st.slider("选择一个数", 0, 100, 25)
st.write(f"当前值：{number}，平方：{number ** 2}")
