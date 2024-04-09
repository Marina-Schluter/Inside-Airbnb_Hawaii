# --------------------LIBRARIES----------------------------#

import streamlit as st
import pandas as pd
import plotly.express as px
import base64

# -----------------SITE CONFIGURATION----------------#

st.set_page_config(
    page_title="AIRBNB-HAWAII",
    page_icon="🌴",
    layout="wide", #centered, wire
    initial_sidebar_state="expanded" #auto, collapsed, expanded
)

#-------------------BACKGROUND IMAGE----------------------#

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .main {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        background-attachment: local;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background("Multipage_app/pages/pages/palmeritas.png")


# --------------------CSV UPLOAD--------------------------#

df = pd.read_csv("Multipage_app/pages/pages/hawaii.csv")
df = df.drop(columns=["id","host_id","host_has_profile_pic","picture_url"])

# ---------------------HEADER-----------------------------#

st.title("Airbnb: Hawaii")

# ---------------------SIDEBAR----------------------------#

logo="Multipage_app/pages/pages/hawaii t-shirt design_6170575.png"             

st.sidebar.image(logo, width=120)
st.sidebar.title("Filters")
st.sidebar.write("-------------")

# --------------------FILTERS------------------------------#

# Options sorted for each filter

options_neighbourhood_group = sorted(df["neighbourhood_group"].unique())
options_neighbourhood = sorted(df["neighbourhood"].unique())
options_room_type=sorted(df["room_type"].unique())
options_accommodates=sorted(df["accommodates"].unique())
options_bedrooms=sorted(df["bedrooms"].unique())
options_bathrooms=sorted(df["bathrooms"].unique())
options_price=sorted(df["price"].unique())
options_reviews=sorted(df["review_scores_rating"].unique())

# Show filters in sidebar

filter_neighbourhood_group = st.sidebar.multiselect("Neighbourhood Group", options=options_neighbourhood_group)
filter_neighbourhood = st.sidebar.multiselect("Neighbourhood", options=options_neighbourhood)
filter_room_type = st.sidebar.multiselect("Room type", options=options_room_type)
filter_accommodates = st.sidebar.multiselect("Accommodates", options=options_accommodates)
filter_bedrooms = st.sidebar.multiselect("Bedrooms", options=options_bedrooms)
filter_bathrooms = st.sidebar.multiselect("Bathrooms", options=options_bathrooms)
filter_price = st.sidebar.multiselect("Price", options=options_price) 
filter_reviews = st.sidebar.multiselect("Score rating", options=options_reviews) 

# Apply filters

if filter_neighbourhood_group:
    df = df[df["neighbourhood_group"].isin(filter_neighbourhood_group)]

if filter_neighbourhood:
    df = df[df["neighbourhood"].isin(filter_neighbourhood)]
    
if filter_room_type:
    df = df[df["room_type"].isin(filter_room_type)]

if filter_accommodates:
    df = df[df["accommodates"].isin(filter_accommodates)]
    
if filter_bedrooms:
    df = df[df["bedrooms"].isin(filter_bedrooms)]

if filter_bathrooms:
    df = df[df["bathrooms"].isin(filter_bathrooms)]

if filter_price:
    df = df[df["price"].isin(filter_price)]

if filter_reviews:
    df = df[df["review_scores_rating"].isin(filter_reviews)]
 
           
# --------------------RESET FILTERS-----------------------------#

if st.sidebar.button('Reset filters'):
    df = pd.read_csv("Multipage_app\pages\pages\hawaii.csv")
    df = df.drop(columns=["id","host_id","host_has_profile_pic","picture_url"])

# --------------------BODY----------------------------#

st.dataframe(df.drop(columns=["listing_id"]))
st.markdown("**Data sample**")

# --------------------TABS----------------------------#
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(
    ["Neighbourhood","Room type", "Capacity", "Bedrooms", "Bathrooms", "Price", "Rating", "Map"]
)
            
# -----------------------GRAPHS ----------------------------#

with tab1:
    st.header("Neighbourhood")
    
    fig = px.histogram(df, x="neighbourhood_group", title="Accommodation Distribution by Neighbourhood",
                   template="plotly_dark", color="neighbourhood", text_auto=True,)
    fig.update_layout(legend_title_text="Neighbourhood")
    fig.update_xaxes(title="Neighbourhood Group")
    fig.update_yaxes(title="Sum of Accommodations")
    st.plotly_chart(fig)
        
with tab2:
    st.header("Room type")   
    
    fig = px.histogram(df, x="neighbourhood_group", title="Room Type Distribution by Neighbourhood", template="plotly_dark",
                       color="room_type",text_auto=True)
    fig.update_layout(legend_title_text="Room Type")
    fig.update_xaxes(title="Neighbourhood Group")
    fig.update_yaxes(title="Sum of Accommodations")
    st.plotly_chart(fig)
    
with tab3:
    st.header("Capacity")        
    
    fig = px.histogram(df, x="neighbourhood_group", title="Accomodation Distribution by Capacity", template="plotly_dark", 
                       color="accommodates",text_auto=True)
    fig.update_layout(legend_title_text="Capacity")
    fig.update_xaxes(title="Neighbourhood Group")
    fig.update_yaxes(title="Sum of Accommodations")
    st.plotly_chart(fig)

with tab4:
    st.header("Bedrooms")        
    
    fig = px.histogram(df, x="neighbourhood_group", title="Accomodation Distribution by Number of Bedrooms", template="plotly_dark", 
                       color="bedrooms",text_auto=True)
    fig.update_layout(legend_title_text="Bedrooms")
    fig.update_xaxes(title="Neighbourhood Group")
    fig.update_yaxes(title="Sum of Accommodations")
    st.plotly_chart(fig)

with tab5:
    st.header("Bathroooms")        
    
    fig = px.histogram(df, x="neighbourhood_group", title="Accomodation Distribution by Number of Bathrooms", template="plotly_dark", 
                       color="bathrooms",text_auto=True)
    fig.update_layout(legend_title_text="Bathrooms")
    fig.update_xaxes(title="Neighbourhood Group")
    fig.update_yaxes(title="Sum of Accommodations")
    st.plotly_chart(fig)
    
with tab6:
    st.header("Price")        
    
    fig = px.histogram(df, x="neighbourhood_group", title="Accomodation Distribution by Price", template="plotly_dark", 
                       color="price",text_auto=True)
    fig.update_layout(legend_title_text="Price")
    fig.update_xaxes(title="Neighbourhood Group")
    fig.update_yaxes(title="Sum of Accommodations")
    st.plotly_chart(fig)

with tab7:
    st.header("Rating")        
    
    fig = px.histogram(df, x="neighbourhood_group", title="Accomodation Distribution by Review Rating Score", template="plotly_dark", 
                       color="review_scores_rating",text_auto=True)
    fig.update_layout(legend_title_text="Review Score Rating")
    fig.update_xaxes(title="Neighbourhood Group")
    fig.update_yaxes(title="Sum of Accommodations")
    st.plotly_chart(fig)
    
with tab8:
    st.header("Map")   
    fig = px.scatter_mapbox(df, lat="latitude", lon="longitude", color="neighbourhood",
                        hover_name="neighbourhood_group", hover_data=['room_type', 'price', 'accommodates', 'bedrooms', 'bathrooms', 'shared_bathrooms', 'minimum_nights', 'maximum_nights',"number_of_reviews_ltm_x", 'review_scores_rating'],
                        title="Distribution of Accommodation by Location on the Map",
                        mapbox_style="open-street-map", zoom=7, template="plotly_dark", height=850, width=2000, size="accommodates",size_max=10)
    fig.update_traces(text=df['neighbourhood'], textposition='top center')
    st.plotly_chart(fig)
    


