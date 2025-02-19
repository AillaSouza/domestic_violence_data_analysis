import streamlit as st
import os
import pandas as pd
import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")


# ------------------ Page Config ------------------
st.set_page_config(page_title="She Speaks, Data Listens", page_icon=":cherry_blossom:", layout="wide")

st.markdown(
    """
    <h1 style="text-align: center;">Violence Against Women Data Explorer</h1>
    """, 
    unsafe_allow_html=True)

st.sidebar.markdown("<br><br><br><br><br><br><br><br><br><br><br><br>", unsafe_allow_html=True)
st.sidebar.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExcmczajBmYWVnYjBoNGp2MGJwaW1tcmNzeWxnMnBmeTM0M25lOHo0MiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/eiGDTvCP5migmm5hut/giphy.gif", width=200)

# ------------------ Data ------------------

project_folder = os.getcwd()
data_path = "/Users/aillapriscila/Desktop/BootCamp/Unit_07 /Final_project /data"
clean_folder = os.path.join(data_path, 'clean')
data_file = os.path.join(clean_folder, 'final_translated_df.csv')
df = pd.read_csv(data_file)

# ------------------ Tab1 ------------------
# Define the categorized questions
question_categories = {
    "General perception of violence against women": [
        "In general, do you think women are treated with respect in Brazil?",
        "For you, in recent years, domestic and family violence against women:",
        "And what was the type of violence suffered?",
        "What does it lead a woman not to denounce the aggression?"
    ],
    "The violence lived / witnessed": [
        "Have you ever suffered any kind of domestic or familiar violence caused by a man?",
        "And what was the type of violence suffered?",
        "At the time of aggression, the aggressor was:",
        "Has any friend, familiar or known have you suffered some kind of domestic or family violence?",
        "At the time of aggression, the aggressor was:"
    ],
    "Profile": [
        "What is your occupation?",
        "How old are you?",                           
        "Which region are you talking about?",                  
        "What is your education?",                              
        "Federation unit",                                      
        "What is your color or race?",                          
        "What is your religion or belief?",                    
        "What is your gross family income per month?",          
        "What is your gross individual income per month?",      
        "What is your marital status?"
    ],
    "Service and Support Network / Complaint": [
        "In that case, who would you look first?",                                                                                                            
        "You know or have heard of the protection services for women provided:",                                       
        "If you witnessed an act of physical aggression to a woman, whom would you first denounce the aggression?",     
        "Do you think the contents conveyed by the press help to reduce domestic violence against women?",              
        "In your opinion, do women who suffer aggression often report the fact to the authorities?",                   
        "Do you know any other women protection service?"  
    ],
    "Society and domestic and family violence": [
        "What do you think society can do to decrease or prevent domestic and family violence against women?",
        "If you witnessed an act of aggression against a woman, you would report:",
        "In what situations would you report?",
        "In general, you consider Brazil a country:"
    ]
}

# Function to plot question distribution
def plot_question_distribution(df, question, year=None, avg=False):
    overview_df = df[df["question"] == question]
    
    if year and not avg:
        overview_df = overview_df[overview_df["year"] == year]
    if avg:
        overview_df = overview_df.groupby("answer", as_index=False)["percentage"].mean()
    
    if overview_df.empty:
        st.write(f"No data available for question: {question} in year: {year if year else 'All Years'}")
        return

    df_pivot = overview_df.set_index("answer")[["percentage"]]
    num_colors = len(df_pivot)
    colors = plt.cm.PuRd(range(50, 250, max(1, 200 // num_colors)))  

    plt.figure(figsize=(12, 6))
    plt.bar(df_pivot.index, df_pivot["percentage"], color=colors, width=0.6)
    
    title_text = f"{question}" + (f" in {year}" if year else " (Average Across Years)" if avg else "")
    plt.title(title_text, fontsize=14, fontweight='bold', color="#800080")
    plt.xlabel("Answer", fontsize=12, fontweight='bold', color="#C71585")
    plt.ylabel("Percentage", fontsize=12, fontweight='bold', color="#C71585")
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    
    st.pyplot(plt)

# Extract only relevant questions present in the dataset
df_questions = df['question'].unique().tolist()
filtered_questions = {
    category: [q for q in questions if q in df_questions]
    for category, questions in question_categories.items()
}


years = sorted(df["year"].dropna().unique().tolist(), reverse=True)

# ------------------ Streamlit UI ------------------

# Create three columns with spacing
col1, col2, col3 = st.columns([1, 2, 1]) 
tabs = st.tabs(["General", "Violence", "Profile", "Support", "Society"])

# Tabs for question selection
with tabs[0]:  # General Perception
    st.subheader("General Perception of Violence Against Women")
    if filtered_questions["General perception of violence against women"]:
        selected_question = st.selectbox("Select a question", filtered_questions["General perception of violence against women"], key="general")
        
        # Year selection & average toggle (placed below question)
        selected_year = st.selectbox("Select a Year", ["All Years"] + years, key="year_general")
        avg_selected = st.checkbox("Show Average Across Years", value=False, key="avg_general")

        plot_question_distribution(df, selected_question, None if selected_year == "All Years" else selected_year, avg_selected)

with tabs[1]:  # Violence lived/witnessed
    st.subheader("The Violence Lived / Witnessed")
    if filtered_questions["The violence lived / witnessed"]:
        selected_question = st.selectbox("Select a question", filtered_questions["The violence lived / witnessed"], key="violence")

        selected_year = st.selectbox("Select a Year", ["All Years"] + years, key="year_violence")
        avg_selected = st.checkbox("Show Average Across Years", value=False, key="avg_violence")

        plot_question_distribution(df, selected_question, None if selected_year == "All Years" else selected_year, avg_selected)

with tabs[2]:  # Profile
    st.subheader("Profile Information")
    if filtered_questions["Profile"]:
        selected_question = st.selectbox("Select a question", filtered_questions["Profile"], key="profile")

        selected_year = st.selectbox("Select a Year", ["All Years"] + years, key="year_profile")
        avg_selected = st.checkbox("Show Average Across Years", value=False, key="avg_profile")

        plot_question_distribution(df, selected_question, None if selected_year == "All Years" else selected_year, avg_selected)

with tabs[3]:  # Service and Support Network / Complaint
    st.subheader("Service and Support Network / Complaint")
    if filtered_questions["Service and Support Network / Complaint"]:
        selected_question = st.selectbox("Select a question", filtered_questions["Service and Support Network / Complaint"], key="support")

        selected_year = st.selectbox("Select a Year", ["All Years"] + years, key="year_support")
        avg_selected = st.checkbox("Show Average Across Years", value=False, key="avg_support")

        plot_question_distribution(df, selected_question, None if selected_year == "All Years" else selected_year, avg_selected)

with tabs[4]:  # Society and domestic and family violence
    st.subheader("Society and Domestic and Family Violence")
    if filtered_questions["Society and domestic and family violence"]:
        selected_question = st.selectbox("Select a question", filtered_questions["Society and domestic and family violence"], key="society")

        selected_year = st.selectbox("Select a Year", ["All Years"] + years, key="year_society")
        avg_selected = st.checkbox("Show Average Across Years", value=False, key="avg_society")

        plot_question_distribution(df, selected_question, None if selected_year == "All Years" else selected_year, avg_selected)
