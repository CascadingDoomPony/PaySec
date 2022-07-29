import streamlit as st

#page config function
st.set_page_config(
    page_title= "SDK-paysec",
    page_icon="chart_with_upwards_trend",
      initial_sidebar_state="expanded",
    layout="wide"
)

st.markdown("# SDK Page")

if "seller_wallet" not in st.session_state:
    st.session_state["seller_wallet"]= ""

if "buyer_wallet" not in st.session_state:
    st.session_state["buyer_wallet"]= ""

if "escrow_wallet" not in st.session_state:
    st.session_state["escrow_wallet"]= ""


seller_wallet = st.text_input("Enter seller_wallet adress", st.session_state["seller_wallet"])
buyer_wallet = st.text_input("Enter buyer_wallet adress", st.session_state["buyer_wallet"])
escrow_wallet = st.text_input("Enter escrow_wallet adress", st.session_state["escrow_wallet"])

submit = st.button("submit")


if submit: 
    st.session_state["seller_wallet"] = seller_wallet
    st.session_state["buyer_wallet"] = buyer_wallet
    st.session_state["escrow_wallet"] = escrow_wallet

    st.write("you entered:", seller_wallet)
    st.write("you entered:", buyer_wallet)
    st.write("you entered:", escrow_wallet)
