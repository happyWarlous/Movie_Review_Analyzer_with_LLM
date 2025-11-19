import streamlit as st
from rag_chain import build_rag_chain
from KEY_FILE import MISTRAL_API_KEY
import os
import json
from datetime import datetime

os.environ["MISTRAL_API_KEY"] = MISTRAL_API_KEY

st.set_page_config(page_title="Movie Review Rating — RAG Demo", page_icon="🎬")

st.title("🎬 Movie Review Rating")
st.write("Enter your review, and the system will rate it on a scale of 1–10 using RAG on past reviews.")

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'current_review' not in st.session_state:
    st.session_state.current_review = ""

@st.cache_resource
def load_chain():
    return build_rag_chain()

rag_chain = load_chain()

def process_review(review_text):
    if not review_text.strip():
        st.warning("Enter your review text.")
        return None
    
    with st.spinner("Generating response..."):
        try:
            resp = rag_chain.invoke(review_text)
            
            history_entry = {
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'review': review_text,
                'response': resp.content,
                'id': len(st.session_state.chat_history) + 1
            }
            st.session_state.chat_history.insert(0, history_entry)
            
            return resp.content
        except Exception as e:
            st.error(f"An error has occurred: {str(e)}")
            return None

 
def clear_text():
    st.session_state.current_review = ""
    


review_text = st.text_area(
    "📝 New review", 
    placeholder="Write your movie review here...",
    value=st.session_state.current_review,
    key="review_input",
    height=150
)

col1, col2 = st.columns([1, 1])

with col1:
    if st.button("🎯 Rate this review", use_container_width=True, type="primary"):
        result = process_review(review_text)
        if result:
            st.session_state.current_review = ""
            st.rerun()

# with col2:
#     if st.button("🗑️ Clear the field", use_container_width=True):
#         clear_text()
#         st.rerun()   

 
if st.session_state.chat_history:
    latest = st.session_state.chat_history[0]
    st.subheader("📊 Latest result")
    st.write(latest['response'])
    st.caption(f"🕐 {latest['timestamp']}")

 
st.markdown("---")
st.subheader("📋 Request history")

if not st.session_state.chat_history:
    st.info("Your query history will be displayed here.")
else:
     
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button("Clear history"):
            st.session_state.chat_history = []
            st.rerun()
    
    with col2:
        if st.button("Export history"):
            export_data = {
                'exported_at': datetime.now().isoformat(),
                'total_entries': len(st.session_state.chat_history),
                'history': st.session_state.chat_history
            }
            st.download_button(
                label="Download JSON",
                data=json.dumps(export_data, ensure_ascii=False, indent=2),
                file_name=f"movie_reviews_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json"
            )

     
    for i, entry in enumerate(st.session_state.chat_history):
        with st.expander(f"📝 Request #{entry['id']} - {entry['timestamp']}", expanded=i==0):
            st.write("**Review:**")
            st.write(entry['review'])
            st.write("**score:**")
            st.write(entry['response'])
            
            if st.button(f"Use this review again", key=f"reuse_{entry['id']}"):
                st.session_state.current_review = entry['review']
                st.rerun()