import streamlit as st
import os
import pandas as pd
import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")

# ------------------ Page Config ------------------
st.set_page_config(page_title="She Speaks, Data Listens", page_icon=":cherry_blossom:", layout="wide")

st.sidebar.markdown("<br><br><br><br><br><br><br><br><br><br><br><br>", unsafe_allow_html=True)
st.sidebar.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExcmczajBmYWVnYjBoNGp2MGJwaW1tcmNzeWxnMnBmeTM0M25lOHo0MiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/eiGDTvCP5migmm5hut/giphy.gif", width=200)

# ------------------ Main Content ------------------

#st.image("https://media.giphy.com/media/3o7TKz9bX9v9KzCnXq/giphy.gif", width=300)
st.markdown(
    """
    <h1 style="text-align: center;">Violence Against Women Data Explorer</h1>
    """, 
    unsafe_allow_html=True)

st.markdown(
    "<br>"
    """
    <div style="
        background-color: white; 
        padding: 15px; 
        border-radius: 10px; 
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        color: black;
        font-size: 16px;
        line-height: 1.6;
    ">
        This project is dedicated to <b>raising awareness about violence against women</b>, 
        using real data collected by <b>DataSenado</b>, the official research body of the <b>Federal Senate of Brazil</b>.<br><br> The survey has been conducted <b>every two years since 2005</b>, 
        providing a comprehensive view of society's perceptions and women's lived experiences.
    </div>
    """
    "<br>"
    , 
    unsafe_allow_html=True
)
# ------------------ Data ------------------

project_folder = os.getcwd()
data_path = "/Users/aillapriscila/Desktop/BootCamp/Unit_07 /Final_project /data"
clean_folder = os.path.join(data_path, 'clean')
data_file = os.path.join(clean_folder, 'final_translated_df.csv')
df = pd.read_csv(data_file)

# ------------------ Function to Plot Trend Over the Years ------------------
def plot_trend_over_years(df, question):
    trend_df = df[df["question"] == question]
    
    if trend_df.empty:
        st.write(f"⚠️ No data available for question: '{question}'")
        return

    df_pivot = trend_df.pivot(index="year", columns="answer", values="percentage")
    colors = ["#FF69B4", "#FF1493", "#C71585", "#800080", "#8A2BE2", "#FF4500", "#32CD32", "#1E90FF"]


    fig, ax = plt.subplots(figsize=(12, 6))  
    for i, answer in enumerate(df_pivot.columns):
        ax.plot(df_pivot.index, df_pivot[answer], marker='o', label=answer, color=colors[i % len(colors)])

    ax.set_title(f"{question} Distribution Over the Years", fontsize=14, fontweight='bold', color="#800080")
    ax.set_xlabel("Year", fontsize=12, fontweight='bold', color="#C71585")
    ax.set_ylabel("Percentage", fontsize=12, fontweight='bold', color="#C71585")
    ax.legend(title="Answer Groups", title_fontsize=12, fontsize=10)
    ax.grid(True, linestyle="--", alpha=0.6)

    st.pyplot(fig)  

# ------------------ Extract Only Relevant Questions ------------------
st.header('What does it lead a woman not to denounce the aggression?', "<br><br>")   
question = 'What does it lead a woman not to denounce the aggression?'
plot_trend_over_years(df, question)
