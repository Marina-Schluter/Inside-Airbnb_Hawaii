# --------------------LIBRARIES----------------------------#

import streamlit as st
import pandas as pd
import plotly.express as px
import base64

# -----------------SITE CONFIGURATION----------------#

st.title("Distribution and Type of Accommodation Graphs")

#-------------------BACKGROUND IMAGE---------------------#

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

# --------------------SIDEBAR-----------------------------#

logo="Multipage_app/pages/pages/hawaii t-shirt design_6170575.png"             
st.sidebar.image(logo, width=120)

# -----------------------GRAPHS ----------------------------#

st.markdown("### **Highlights:**")
st.markdown("- Maui offers the most accommodations, with Kauai having about half as many.")
st.markdown("- Kauai lacks shared rooms.")
st.markdown("- Honolulu's Primary Urban Center offers the most varied accommodations.")
st.markdown("- Average bedrooms per acccomodation is 1 in shared accomodations and between 1-2 in others.")
st.markdown("- Average capacity: 3-4 in shared/private rooms, 4-6 in others, with hotels having the highest.")
st.markdown("- Maximum capacity: 12 in shared, 16 in others.")
st.markdown("- Average bathrooms: 1 in private, 2 in others.")

#Graph 1

counts_by_neighbourhood_group = df.groupby("neighbourhood_group").size().reset_index(name="Total")
fig = px.bar(counts_by_neighbourhood_group, x="neighbourhood_group", y="Total", color="neighbourhood_group",
             title="Total Accommodation per Neighbourhood Group", text_auto=True,
             labels={"neighbourhood_group": "Neighbourhood Group", "Total": "Total number of Accommodations"},
             template="plotly_dark")
fig.update_yaxes(tickformat=".0f") 
fig.update_layout(showlegend=False)
st.plotly_chart(fig)

st.markdown("Maui is the neighborhood that offers the highest number of accommodations. Kauai, with about half of the accommodations of Maui, is the neighborhood group the lowest number of accommodations.")


#Graph 2

fig = px.histogram(df, x="neighbourhood_group", title="Accommodation distribution by neighbourhood",
                   template="plotly_dark", color="neighbourhood", text_auto=True, 
                   labels={"neighbourhood_group": "Neighbourhood Group", "count": "Total number of Accommodations"})
fig.update_layout(legend_title_text="Neighbourhood")
st.plotly_chart(fig)

st.markdown("The majority of accommodations in Kauai are located between North Shore Kauai and Poipu.")
st.markdown("The majority of accommodations in Honolulu are located in the Primary Urban Center.")
st.markdown("The majority of accommodations in Maui are located between Makena and Lahaina.")
st.markdown("The majority of accommodations in Honolulu are located in North Kona.")
        
        
#Graph 3

total_accommodates_by_room_type = df.groupby("room_type")["accommodates"].sum().reset_index()
fig = px.bar(total_accommodates_by_room_type, x="room_type", y="accommodates", 
             title="Total Accommodates by Room Type", 
             template="plotly_dark", text="accommodates",
             labels={"accommodates": "Total Accommodates", "room_type": "Room Type"})
fig.update_layout(legend_title_text="Room Type")
st.plotly_chart(fig)

st.markdown("The most common type of accommodation is **Entire Home/apt**.")


#Graph 4

fig = px.histogram(df, x="neighbourhood_group", title="Room Type Distribution by Neighbourhood Group", template="plotly_dark",
                   color="room_type",text_auto=True,
                   labels={"neighbourhood_group": "Neighbourhood Group", "count":"Total number of Accommodations"})
fig.update_layout(legend_title_text="Room Type")
st.plotly_chart(fig)

st.markdown("Kauai is the only neighbourhood group that does not offer shared rooms.")


#Graph 5

room_type_distribution = df.groupby(['neighbourhood_group', 'neighbourhood', 'room_type']).size().reset_index(name='count')

fig = px.bar(room_type_distribution, x="neighbourhood", y="count", color="room_type",
             labels={"neighbourhood": "Neighbourhood","count": "Total number of Accommodations"},
             template="plotly_dark", title="Room Type Distribution by Neighbourhood")
fig.update_layout(legend_title_text="Room Type")

st.plotly_chart(fig)

st.markdown("Primary Urban Center, in Honolulu, is the neighborhood that offers the highest number of accommodations and provides all types of accommodations.")


#Graph 6

mean_bedrooms_by_room_type = df.groupby("room_type")["bedrooms"].mean().round(2).reset_index()
fig = px.bar(mean_bedrooms_by_room_type, x="room_type", y="bedrooms", 
             title="Average Number of Bedrooms by Room Type", text_auto=True, color="room_type",
             labels={"bedrooms": "Average Number of Bedrooms", "room_type": "Room Type"},
             template="plotly_dark")
fig.update_layout(showlegend=False)
st.plotly_chart(fig)

st.markdown("The average number of bedrooms per accommodation type is 1 for shared accommodations and between 1 and 2 for the rest of accommodation types.")

#Graph 7

mean_bedrooms_by_room_type = df.groupby("room_type")["accommodates"].mean().round(2).reset_index()
fig = px.bar(mean_bedrooms_by_room_type, x="room_type", y="accommodates", 
             title="Average capacity by Room Type", text_auto=True, color="room_type",
             labels={"accommodates": "Average capacity", "room_type": "Room Type"},
             template="plotly_dark")
fig.update_layout(showlegend=False)
st.plotly_chart(fig)

st.markdown("The average capacity per accommodation type is between 3 and 4 for shared and for privates rooms, and betwwen 4 and 6 for the rest. Hotel rooms has the higher avarage capacity")


#Graph 8

max_capacity_by_room_type = df.groupby("room_type")["accommodates"].max().reset_index()
fig = px.bar(max_capacity_by_room_type, x="room_type", y="accommodates", 
             title="Maximum Capacity by Room Type", text_auto=True, color="room_type",
             labels={"accommodates": "Maximum capacity", "room_type": "Room Type"},
             template="plotly_dark")
fig.update_layout(showlegend=False)
st.plotly_chart(fig)

st.markdown("The maximum capacity per accommodation type is 12 for shared rooms and 16 for the other room types.")


#Graph 9

mean_bathrooms_by_room_type = df.groupby("room_type")["bathrooms"].mean().round().reset_index()
fig = px.bar(mean_bathrooms_by_room_type, x="room_type", y="bathrooms",
             title="Average Bathrooms per Room Type", text_auto=True, color="room_type",
             labels={"bathrooms": "Average Bathrooms", "room_type": "Room Type"},
             template="plotly_dark")
fig.update_layout(showlegend=False)

st.plotly_chart(fig)

st.markdown("The average bathrooms per room type is1 for private rooms and 2 for the other room types")



