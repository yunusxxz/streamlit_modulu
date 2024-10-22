import streamlit as st

st.set_page_config(layout="wide")

c1, c2, c3 = st.columns(3, gap="small")

with c1:
    with st.form("numbers"):
        age = st.number_input("Your Age?", min_value=0, max_value=100)
        height = st.slider("Your Height?", min_value=100, max_value=250, step=1)
        city = st.selectbox("Your birth city?", ["İstanbul", "İzmir", "Ankara", "Sivas"])
        fav_color = st.radio("Your Favorite Color?", [None, "Red", "Green", "Blue"])
        smoking = st.checkbox("Smoking?")
        age_btn = st.form_submit_button("Send")
    if age_btn:
        st.write(f"Your Age:{age}")
        st.write(f"Your height:{height}")
        st.write(f"Your City of Birth:{city}")

with c2:
    with st.form("my_form"):
        st.subheader("Sample Form")
        st.divider()
        name = st.text_input("Fullname")
        email = st.text_input("E-Mail Address:")
        subject = st.text_input("Subject:")
        message =st.text_area("Message:")
        btn = st.form_submit_button("Send")
    if btn:
        st.write(f"Fullname:{name}")
        st.write(f"E-Mail:{email}")
        st.write(f"Subject:{subject}")
        st.write(f"Message:{message}")

with c3:
    with st.form("Advance"):
        hobbies= st.multiselect("Select your hobbies:", ["Swim", "Run", "Coffee", "Gaming", "Reading"])
        dt1, dt2 = st.columns(2, gap="small")
        with dt1:
            start= st.date_input("Start date:")
        with dt2:
            end= st.date_input("Ende date")

        color= st.color_picker("Select a Color:")

        file = st.file_uploader("Upload an İmage:", type=['png', 'jpg', 'bmp'])

        adv_btn = st.form_submit_button("Send")

    if file:
        st.image(file)
        st.write(file.name)
        with open(file.name, "wb") as f:
            f.write(file.getbuffer())

