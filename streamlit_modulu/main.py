import streamlit as st
import requests as req
import pandas as pd

st.set_page_config(
    page_title="Hello World, This is my first Streamlit Project",
    page_icon= ":wave:",
    layout= "wide"
)



st.title("Hello World !!!")
st.header("A, Header")
st.subheader("I. SubHeader")
st.divider()
#st.text(): Hiçibir tasarım özelliği olmadan eklenen metindir, genel olarak kullanılmaz.

st.text("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed a dictum elit. Nam bibendum facilisis libero ut tincidunt.")

st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed a dictum elit. Nam bibendum facilisis libero ut tincidunt. Curabitur vestibulum quis metus quis euismod. Maecenas eu fermentum elit. Sed tempus id neque eu blandit. Nulla luctus rhoncus nunc, et faucibus nisi eleifend in. Nunc non enim iaculis, porttitor sapien sit amet, viverra augue. Nullam lacinia ultricies mauris, at semper ipsum aliquet id. Vivamus pellentesque posuere sem ac pretium. Maecenas ultricies eget sapien eget pulvinar. Fusce fringilla leo malesuada, viverra tortor in, malesuada nunc. Praesent maximus at ex in pulvinar. Etiam lobortis blandit ex ut egestas. Maecenas euismod mollis leo, eget gravida odio ultricies vel.")

st.divider()

c1,c2,c3 = st.columns([2,1,2], gap="small")

with c1:
    st.subheader("&copy; Column One")
    st.divider()
    st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed a dictum elit. Nam bibendum facilisis libero ut tincidunt. Curabitur vestibulum quis metus quis euismod. Maecenas eu fermentum elit. Sed tempus id neque eu blandit. Nulla luctus rhoncus nunc, et faucibus nisi eleifend in. Nunc non enim iaculis, porttitor sapien sit amet, viverra augue. Nullam lacinia ultricies mauris, at semper ipsum aliquet id. Vivamus pellentesque posuere sem ac pretium. Maecenas ultricies eget sapien eget pulvinar. Fusce fringilla leo malesuada, viverra tortor in, malesuada nunc. Praesent maximus at ex in pulvinar. Etiam lobortis blandit ex ut egestas. Maecenas euismod mollis leo, eget gravida odio ultricies vel.")

with c2:
    st.subheader("Column Two")
    st.divider()
    st.image("https://picsum.photos/450/800?random=1", "Column Two İmages", use_column_width=True)

with c3:
    st.subheader("Column Three")
    st.divider()
    liste = [
        "Curabitur eu diam id est ornare vulputate id non metus.",
        "Praesent vel mauris facilisis, vehicula augue quis, feugiat lacus.",
        "Integer vestibulum metus a ipsum euismod, efficitur vehicula orci volutpat.",
        "Aliquam sed lectus eu neque vestibulum fringilla vel quis tortor.",
        "Sed eget ligula sit amet dui tincidunt pulvinar a tempor urna.",
        "Nunc feugiat ipsum id porta ultricies."
    ]
    for i in liste:
        st.write("*", i)


url = "https://dummyjson.com/recipes?limit=0"
res = req.get(url)
if res.status_code == 200:
    st.subheader("Recipes from Dummyjson:")
    recipes = res.json()['recipes']
    df = pd.DataFrame(recipes)
    df = df[['id', 'name', 'cuisine', 'mealType', 'tags', 'difficulty']]
    st.dataframe(df, use_container_width= True)



