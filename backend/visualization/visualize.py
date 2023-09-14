import streamlit as st
from helpers import get_most_popular_tags, get_pages, get_most_popular_authors
from pandas import DataFrame


# Add a selectbox to the sidebar:
tags_page_selectbox = st.sidebar.selectbox(
    'What page would you like to view tags for?',
    list(range(1, get_pages()+1))
)

left_column, right_column = st.columns(2)

most_popular_tags: DataFrame = get_most_popular_tags()
most_popular_tags_per_page: DataFrame = get_most_popular_tags(page=tags_page_selectbox)
most_popular_authors: DataFrame = get_most_popular_authors()
left_column.bar_chart(
    most_popular_tags_per_page,
    x='name',
    y='count'
)
right_column.bar_chart(
    most_popular_tags,
    x='name',
    y='count'
)
st.bar_chart(
    most_popular_authors,
    x='name',
    y='count'
)