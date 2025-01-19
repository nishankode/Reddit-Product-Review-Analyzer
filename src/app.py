import streamlit as st
import redditScrape, tokenValidate, getReport
from IPython.display import Markdown

# Streamlit UI elements for user input
st.title("Reddit Product Review Analyzer")

# Input fields for the user to provide subreddit and thread keyword
subreddit = st.text_input("Enter subreddit name", '')
keyword = st.text_input("Enter keyword to search for", '')


# Button to trigger the scraping and report generation
if st.button('Generate Report'):
    if subreddit and keyword:
        # Scrape reddit threads
        collected = redditScrape.collect_threads(subreddit, keyword)
        
        # Ensure tokens are within limit
        all_content, messages = tokenValidate.ensure_tokens_within_limit(collected)
        
        # Generate the report
        report = getReport.generate_report(all_content, messages)
        
        # Display the result as markdown
        st.markdown(report)
    else:
        st.warning("Please fill all the input fields.")
