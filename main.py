import streamlit as st
from scrape import (scrape_website, extract_body_content, clean_content, split_content)
from parser import parse_with_llm

url = st.text_input("enter url")
scrape_button = st.button("Scrape")
if url and scrape_button:
    result = scrape_website(url)
    content = extract_body_content(result)
    cleaned_content = clean_content(content)

    st.session_state.dom_content = cleaned_content

    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleaned_content, height=300)

prompt = st.text_area("Describe what you want to parse")
if st.button("Parse") and prompt:
    dom_content = split_content(st.session_state.dom_content, max_length=6000)
    parsed_result = parse_with_llm(prompt, dom_content)
    st.write(parsed_result)


    #logic for parsing content
