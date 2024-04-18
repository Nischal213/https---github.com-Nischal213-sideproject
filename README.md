Change bg color in py.subplot() - [Here](https://www.geeksforgeeks.org/how-to-set-plot-background-color-in-matplotlib/)

Change text color in py.subplot() - [Here](https://stackoverflow.com/questions/27898830/python-how-to-change-autopct-text-color-to-be-white-in-a-pie-chart)

SHA-256 explanation - [Here](https://www.youtube.com/watch?v=orIgy2MjqrA)

Rotate right explanation - [Here](https://www.youtube.com/watch?v=m_08FbT0_WY)

Right shift explanation - [Here](https://www.youtube.com/watch?v=m_08FbT0_WY)

Binary to denary easier method - [Here](https://www.bbc.co.uk/bitesize/guides/zd88jty/revision/3)


FUTURE IDEAS:
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
