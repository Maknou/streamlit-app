import chart_studio.plotly as py
import plotly.figure_factory as ff
import pandas as pd
import plotly
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objs as go
from PIL import Image
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import altair as alt
alt.renderers.enable('altair_viewer')

#add_selectbox = st.sidebar.selectbox(
#    "Which Player is the Best in the world",
#    ("Leo Messi","Cristiano Ronaldo","Neymar")
#)


st.title('FIFA 19')

st.header('FIFA 19 Game Trailer')

if st.checkbox('Watch FIFA19 Trailer'):
    video_file = open('C:/Users/Makram/Desktop/VID.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
if st.checkbox('Listen to FIFA19 Soundtrack'):
    audio_file = open('C:/Users/Makram/Desktop/audio.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/ogg')

df = pd.read_csv('C:/Users/Makram/Desktop/data.csv')
df1=df[['Name', 'Age', 'Nationality',
       'Overall','Club',  'Value', 'Wage', 'Special',
       'Preferred Foot','Position','Height', 'Weight', 'LS', 'ST', 'RS', 'LW', 'LF', 'CF', 'RF', 'RW',
       'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LWB', 'LDM',
       'CDM', 'RDM', 'RWB', 'LB', 'LCB', 'CB', 'RCB', 'RB', 'Crossing',
       'Finishing', 'HeadingAccuracy', 'ShortPassing', 'Volleys', 'Dribbling',
       'Curve', 'FKAccuracy', 'LongPassing', 'BallControl', 'Acceleration',
       'SprintSpeed', 'Agility', 'Reactions', 'Balance', 'ShotPower',
       'Jumping', 'Stamina', 'Strength', 'LongShots', 'Aggression',
       'Interceptions', 'Positioning', 'Vision', 'Penalties', 'Composure',
       'Marking', 'StandingTackle', 'SlidingTackle', 'GKDiving', 'GKHandling',
       'GKKicking', 'GKPositioning', 'GKReflexes', 'Release Clause']]

add_selectbox = st.sidebar.title(
    'Welcome to FIFA 19')
add_selectbox = st.sidebar.image("https://i.postimg.cc/Z0kL7LJg/game.jpg")

add_selectbox = st.sidebar.selectbox('How much you like the FIFA game ?',("Very Much","Don't Like it","Never Played It Before"))

if add_selectbox == "Very Much":
        st.sidebar.markdown(":heart_eyes:")
elif add_selectbox == "Don't Like it":
        st.sidebar.markdown(":unamused:")
elif add_selectbox == "Never Played It Before":
        st.sidebar.markdown(":expressionless:")        


teams = df1['Club'].drop_duplicates()
make_choice = st.sidebar.selectbox('Select your Favorite Team:', teams)
players = df1["Name"].loc[df1["Club"] == make_choice]
players_choice = st.sidebar.selectbox('', players)
overall = df1["Overall"].loc[(df1["Name"] == players_choice)&(df1["Club"] == make_choice)]
players_overall = st.sidebar.write(overall)



st.header("FIFA19 Players Details")

st.dataframe(df1)

st.header("Top 3 Players Attributes")

df_91= df1[df1['Overall'] > 91]

st.altair_chart(
  alt.Chart(df_91)
    .transform_fold(["Dribbling", "Finishing","Acceleration","Agility","Stamina","Positioning","Vision"], as_=["Player", "Score"])
    .mark_bar()
    .encode(
        x="Player:N",
        y="Score:Q",
        color="Score:N",
        column="Name",
    ).properties(width=200,height=400)
)

option = st.selectbox('Which Player you think then he is the Best in your Opinion',
     ("Leo Messi","Cristiano Ronaldo","Neymar","Other"))
if option == "Leo Messi":
    st.image("https://i.postimg.cc/764Zmrky/Messi.jpg")
elif option == "Cristiano Ronaldo":
    st.image("https://i.postimg.cc/Yqx2qsYX/Ronaldo.jpg")
elif option == "Neymar":
    st.image("https://i.postimg.cc/dtgkrXLJ/neymar.jpg")
elif option == "Other":
    st.image("https://i.postimg.cc/zG1h4650/depositphotos-25225399-stock-photo-who-3d-word-question-mark.jpg")
'You selected: ', option

#image = Image.open('https://images.app.goo.gl/zjuuvFLzWur8tDNj8')
#st.image(image, caption='Leo Messi')


    
st.header("Players count by Nationality")
counts_Nationality = df.Nationality.value_counts()
counts_Nationality = counts_Nationality.reset_index()
counts_Nationality.columns= ["Nationality","Counts"]
if st.checkbox('Show Nationalities Count'):
    st.write(counts_Nationality)

#st.dataframe(counts_Nationality)
counts_Nationality=counts_Nationality[0:50]
#st.bar_chart(counts_Nationality['Counts'])

chart=alt.Chart(counts_Nationality).mark_bar(size=10).encode(
    x=alt.X('Nationality:O', sort='-y'),
    y=alt.Y('Counts:Q', sort='-x'),color=alt.condition(
        alt.datum.Nationality == 'England',  
        alt.value('orange'),     # which sets the bar orange.
        alt.value('steelblue')   # And if it's not true it sets the bar steelblue.
    )
).properties(width=600,height=1000)

#chart.show()
st.altair_chart(chart, use_container_width=True)


st.header("Position of Players Count")

positions = df1.Position.value_counts()
positions = positions.reset_index()
positions.columns= ["positions","Counts"]
          
if st.checkbox('Show Positions Count'):
    st.write(positions)
          
chart=alt.Chart(positions).mark_bar(size=10).encode(
    x=alt.X('positions:O'),
    y=alt.Y('Counts:Q'),color=alt.condition(
        alt.datum.positions == 'ST',  
        alt.value('Red'),     # which sets the bar orange.
        alt.value('Blue')   # And if it's not true it sets the bar steelblue.
    )
).properties(width=400,height=500)

#chart.show()
st.altair_chart(chart, use_container_width=True)

st.header("Players Above Overall 86")

above_85= df1[df1['Overall'] > 85]

values = st.slider(
     'Select a range of values',
    86, 100, 86)
st.write('Values:', values)
filtered_data = above_85[above_85['Overall'] >= values]
st.subheader('Map of all players above Overall %s' % values)

chart=alt.Chart(filtered_data).mark_point().encode(
    x=alt.X('Name:O'),
    y=alt.Y('Overall:Q')
).properties(width=600,height=500)

#chart.show()
st.altair_chart(chart, use_container_width=True)

barcelona = df1[df1['Club']=='FC Barcelona']
counts_Nationality = barcelona.Nationality.value_counts()
counts_Nationality = counts_Nationality.reset_index()
counts_Nationality.columns= ["Nationality","Counts"]

st.header('FC Barcelona Players Count by nationality')
bars = alt.Chart(counts_Nationality).mark_bar().encode(
    x=alt.X('Counts:Q'),
    y=alt.Y('Nationality:O'),color=alt.condition(
        alt.datum.Nationality == 'Spain',  
        alt.value('red'),     
        alt.value('blue')  
    )
)
text = bars.mark_text(
    align='left',
    baseline='middle',
    dx=3  # Nudges text to right so it doesn't appear on top of the bar
).encode(
    text='Counts:Q'
)

st.altair_chart(((bars + text).properties(height=600,width=1000)),use_container_width=True)
