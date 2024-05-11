FUTURE IDEAS:
-> PRIORITY - When the user goes back a page, session state data is retained
(Plausible idea: temporarily store their username session state data and 
clear all the keys when first entering the page) 
-> A better way of showing user's personal growth as the graph is interactive
    import streamlit as st
    import plotly.express as px

    dates = ["01/01/2024", "02/01/2024","03/01/2024","04/01/2024","05/01/2024","06/01/2024"]
    scores = [9, 5, 43, 21, 56, 78]

    figure = px.line(x=dates, y=scores, labels={"x": "Date", "y": "Score"})

    st.plotly_chart(figure)
-> Do the same thing for pie charts as well
-> Make a captcha to prevent bots from spam making account
-> 2FA verification
-> Change password using email