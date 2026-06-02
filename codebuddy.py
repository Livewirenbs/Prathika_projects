import streamlit as st
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi"

allowed_keywords = [
    "python","java","c","c++","javascript","html","css",
    "sql","mysql","jdbc","swing","servlet","jsp",
    "ai","ml","algorithm","dsa","program","code","coding",
    "function","class","object","oop","error","exception","inheritance"
]

def is_education_question(text):
    return any(k in text.lower() for k in allowed_keywords)

st.set_page_config(
    page_title="Education Chatbot",
    page_icon="📚",
    layout="wide"
)

# ---------------- Session ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- UI ----------------
st.markdown("""
<style>
.stApp {
    background-image: url("https://images.unsplash.com/photo-1519389950473-47ba0277781c");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}
section[data-testid="stSidebar"] {
    width: 260px !important;
}
.chat-container {
    max-width: 900px;
    margin: auto;
    padding-top: 20px;
}
.user-message {
    background-color: #d1e7dd;
    padding: 12px 16px;
    border-radius: 15px;
    margin: 10px 0;
    text-align: right;
    font-weight: bold;
}
.bot-message {
    background-color: #f5efe6;
    padding: 15px 18px;
    border-radius: 15px;
    margin: 10px 0;
    text-align: left;
    line-height: 1.6;
}
.stTextInput>div>div>input {
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 style='color:white; font-style:italic; text-align:center; font-weight:bold; text-shadow:2px 2px 6px black;'>
📚 CodeBuddy Chatbot ❤️
</h1>
""", unsafe_allow_html=True)

st.markdown(
    "<p style='color:white; text-align:center;'>Ask coding or programming questions only</p>",
    unsafe_allow_html=True
)

# ---------------- Sidebar ----------------
with st.sidebar:
    st.title("📜 Chat History")

    if not st.session_state.messages:
        st.write("No chats yet.")
    else:
        for chat in st.session_state.messages:
            st.markdown(
                f"<div style='font-size:13px; margin-bottom:8px;'>• {chat['question']}</div>",
                unsafe_allow_html=True
            )

# ---------------- Chat Display ----------------
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

for chat in st.session_state.messages:
    st.markdown(f"<div class='user-message'>{chat['question']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='bot-message'>{chat['answer']}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- Normalize ----------------
def normalize_question(question):
    q = question.lower().strip()
    if q in ("oops", "what is oops", "oops full form"):
        return "What is OOPS in Object-Oriented Programming?"
    return question

# ---------------- Form (AUTO CLEAR INPUT) ----------------
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("💬 Type your question here")
    submit = st.form_submit_button("Ask")

# ---------------- Logic ----------------
if submit:

    if not user_input.strip():
        st.warning("Type a question")

    elif not is_education_question(user_input):
        st.error("Only education / coding questions allowed")

    else:
        fixed_question = normalize_question(user_input)

        SYSTEM_PROMPT = """You are CodeBuddy, a strict and expert Computer Science tutor..."""

        payload = {
            "model": MODEL_NAME,
            "prompt": SYSTEM_PROMPT + f"\nQuestion: {fixed_question}\nAnswer:",
            "stream": False,
            "options": {
                "num_predict": 60,
                "temperature": 0.0,
                "top_p": 0.9
            }
        }

        try:
            with st.spinner("Thinking... 🤔"):
                response = requests.post(
                    OLLAMA_URL,
                    json=payload,
                    timeout=60
                )
                data = response.json()
                answer = data.get("response", "").strip()

                if answer:
                    st.session_state.messages.append({
                        "question": user_input,
                        "answer": answer
                    })

                    st.rerun()

        except Exception as e:
            st.error(f"Error: {e}")