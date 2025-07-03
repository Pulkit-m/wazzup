import streamlit as st  
from utils.news_wrapper import NewsCoo
# from streamlit.logger import get_logger
import logging 
from typing import List

@st.cache_data
def get_news_sources(): 
    logger.info("Fetching sources")
    sources = newsCoo.get_sources() #cache this. 
    return sources


def display_article(article):
    with st.container():
        # Create two columns: left (image), right (text)
        img_col, text_col = st.columns([3, 4])  # Ratio of widths

        with img_col:
            if article.get("urlToImage"):
                st.image(article["urlToImage"], width=300)  # small square image

        with text_col:
            st.markdown(
                f"**[{article['title']}]({article['url']})**",
                unsafe_allow_html=True
            )
            st.caption(article.get("description", "No summary available."))

        st.markdown("---")


newsCoo = NewsCoo(st.secrets["newsapikey"])
logging.basicConfig(filename='logs/app_log.log', level=logging.DEBUG, 
                    format='%(asctime)s::%(message)s',
                    filemode='w')
logger = logging.getLogger() 
logger.info("Logger initiated again. App reloading.")
sources = get_news_sources()
st.write(f"""
# What's New! 
Extremely sorry for the shitty interface!
""")



# Step 1: Let user choose between category or source
filter_type = st.radio(
    "Search news by:",
    options=["Category", "Source"],
    horizontal=True
)

# Step 2: Conditional input based on selection
selected_category = ""
selected_source = ""

# Sample categories (as per NewsAPI docs)
category_options = [
    "business", "entertainment", "general", 
    "health", "science", "sports", "technology"
]

# Sample sources — replace with actual from NewsAPI
source_options = get_news_sources()

with st.form("news_filter_form"):
    st.subheader("🔎 Filter Options")

    if filter_type == "Category":
        selected_category = st.selectbox("Select a news category:", category_options)
    elif filter_type == "Source":
        selected_source = st.selectbox("Select a news source:", source_options)


    # Submit button
    submitted = st.form_submit_button("🔍 Search")

# 3️⃣ Step 3: Handle API call only after form submission
if submitted:
    # Build API parameters
    params = {}

    if filter_type == "Category":
        params["category"] = selected_category
    elif filter_type == "Source":
        params["sources"] = selected_source

    # Save to session for re-render / pagination
    st.session_state.search_params = params

# 4️⃣ Step 4: Display results if search_params exists
if "search_params" in st.session_state:
    params = st.session_state.search_params
    st.success(f"Fetching news for: {params}")

    # 🔻 Replace with actual API call function
    # articles = fetch_articles(**params)
    if "category" in params: 
        st.write("Showing results by Category")
        articles = newsCoo.get_top_headlines(category=params["category"])
        logger.info(f"num of articles in category {params['category']}: {len(articles)}")
    elif "sources" in params: 
        st.write("Showing results by Source")
        articles = newsCoo.get_top_headlines(sources=params["sources"])
        logger.info(f"num of articles by {params['sources']}: {len(articles)}")

    # In your app logic:
    for article in articles:
        display_article(article)








