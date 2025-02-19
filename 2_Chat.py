import streamlit as st
import random
import time
from difflib import get_close_matches

# ------------------ Page Config ------------------
st.set_page_config(page_title="She Speaks, Data Listens", page_icon=":cherry_blossom:", layout="wide")

st.markdown(
    """
    <h1 style="text-align: center;">Violence Against Women Chat</h1>
    """, 
    unsafe_allow_html=True)

st.sidebar.markdown("<br><br><br><br><br><br><br><br><br><br><br><br>", unsafe_allow_html=True)
st.sidebar.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExcmczajBmYWVnYjBoNGp2MGJwaW1tcmNzeWxnMnBmeTM0M25lOHo0MiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/eiGDTvCP5migmm5hut/giphy.gif", width=200)

# ------------------ Main Content ------------------


# Introduction with Quote
st.markdown("""
> "Among all types of violence against women worldwide, the one that occurs within the family environment is among the most cruel and perverse. The home, typically seen as a place of warmth and comfort, in these cases becomes a space of continuous danger, resulting in a state of permanent fear and anxiety.  
>  
> Entangled in a web of emotions and affective relationships, domestic violence against women remains, to this day, a lingering shadow in our society."

📜 *(FEDERAL SENATE. Subsecretariat for Research and Public Opinion. Research Report SEPO 03/2005 - Domestic Violence Against Women. March 2005.)*

---
:calling: If you or someone you know needs help, call **180** for support.
""")


# ------------------ Chatbot ------------------
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Tell me how I can help you today. :tulip: "}]

# Predefined responses
response_dict = {
    "what number should I call": ["📞 **Call 180** - a free, 24-hour service in Brazil for reporting violence against women."],
    "where can I report violence": ["🏢 **You can report violence at:**\n- A **police station** (Delegacia da Mulher)\n- **Ligue 180** (national violence helpline)\n- **Social assistance centers**"],
    "what should I do if I'm attacked": ["🚨 **Stay safe:**\n- **Call 190** (Police Emergency)\n- **Call 180** for women’s support\n- Seek a **women’s shelter** or **legal assistance**"],
    "how can I help a victim": ["🆘 **Support a victim by:**\n- Encouraging her to **call 180**\n- Accompanying her to a **police station**\n- Providing **emotional and legal support**"],
    "what is domestic violence": ["💔 **Domestic violence includes:**\n- Physical aggression\n- Psychological abuse\n- Financial control\n- Threats and coercion\n- Sexual violence"],
    "what are my rights": ["⚖ **Your legal rights:**\n- Protection under the **Maria da Penha Law**\n- Right to file a police report (BO)\n- Right to restraining orders\n- Access to women's shelters"],
    "what is the maria da penha law": ["📜 **Maria da Penha Law (2006):**\nA Brazilian law that protects women against domestic violence and ensures severe punishment for aggressors."],
    "how common is violence against women": ["📊 Studies show that **1 in 3 women** worldwide experience some form of violence in their lifetime."],
    "why don't women report violence": ["😞 Many victims **don’t report** due to:\n- Fear of retaliation\n- Economic dependence\n- Lack of trust in authorities\n- Social stigma"],
    "what help is available": ["🤝 **Support available:**\n- **Ligue 180** (24-hour helpline)\n- **Women’s shelters**\n- **Legal assistance services**\n- **Psychological support centers**"],
    "can i report violence anonymously": ["✅ **Yes!** You can report anonymously via **180** or by calling **100**."],
    "where can i find a women's shelter": ["🏠 **Women's shelters** are available in many cities. Contact **180** to find one near you."]
}

# Fuzzy matching function
def get_best_match(user_input, threshold=0.5):
    matches = get_close_matches(user_input.lower(), response_dict.keys(), n=1, cutoff=threshold)
    return matches[0] if matches else None

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("How can I help you?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        # Get best-matching response
        matched_key = get_best_match(prompt)
        if matched_key:
            assistant_response = random.choice(response_dict[matched_key])
        else:
            assistant_response = "I'm not sure about that. Try rephrasing your question or call **180** for more information."

        # Simulated typing effect
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})
