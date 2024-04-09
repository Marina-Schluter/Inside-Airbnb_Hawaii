# --------------------LIBRARIES----------------------------#

import streamlit as st
import pandas as pd
import plotly.express as px
import base64

# -----------------SITE CONFIGURATION----------------#

st.title("Conclusions and Graphs based on Price")

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
st.markdown("- ***Neighborhood Prices***: Maui commands the highest average prices (\$485), while Hawaii has the lowest ($333).")
st.markdown("- ***Neighborhood Variances***: Koloa-Poipu in Kauai tops with an average of \$517, while Molokai in Maui is the least expensive at $149.")
st.markdown("- ***Room Type Prices***: Private rooms fetch the highest average price (\$585), while shared rooms are notably cheaper ($160).")
st.markdown("- ***Shared Bathrooms***: Accommodations with shared bathrooms are priced at \$180 on average.")
st.markdown("- ***Superhost Impact***: Being a superhost doesn't significantly affect prices (\$365 vs. $425).")
st.markdown("- ***Host Verification***: Verified hosts charge more on average (\$407 vs. $327).")
st.markdown("- ***Instant Booking Premium***: Options for instant booking generally lead to higher prices (\$449 vs. $343).")
st.markdown("- ***Price per Person***: The average price per person per night stands at \$84.")
st.markdown("- ***Price Ranges***: Most stays fall between $80 and $100 per night, with lower prices observed for larger accommodations (\$57 for 15-person stays).")
st.markdown("- ***Rating Influence***: Ratings between 1 and 2 correlate with higher prices (\$538), contrasting with prices close to $300 for ratings between 2 and 5.")

#Graph 1

mean_prices = df.groupby(["neighbourhood_group"])["price"].mean().round().reset_index()
fig = px.histogram(mean_prices, x="neighbourhood_group", y="price", title="Average Price per Neighbourhood Group",
                   color="neighbourhood_group", template="plotly_dark", text_auto=True, width=800,
                   labels={"neighbourhood_group": "Neighbourhood Group", "sum of price": "Price"})
fig.update_layout(showlegend=False)
fig.update_yaxes(title="Average Price")
st.plotly_chart(fig)

st.markdown("The average prices per neighbourhood group are higher in Maui (\$485) and lower in Hawaii ($333).")


#Graph 2

mean_prices = df.groupby(["neighbourhood", "neighbourhood_group"])["price"].mean().round().reset_index()
fig = px.histogram(mean_prices, x="neighbourhood", y="price", title="Average Price per Neighbourhood",
                   color="neighbourhood_group", template="plotly_dark", text_auto=True, width=800,
                   labels={"neighbourhood": "Neighbourhood"})
fig.update_layout(legend_title_text="Neighbourhood Group")
fig.update_yaxes(title="Average Price")
st.plotly_chart(fig)

st.markdown("The highest average price per neighborhood is in Koloa-Poipu (\$517), Kauai, and the lowest is in Molokai ($149), Maui.")


#Graph 3

mean_prices = df.groupby(["room_type"])["price"].mean().round().reset_index()
fig = px.histogram(mean_prices, x="room_type", y="price", title="Average Price per Type of Accommodation",
                   color="room_type", template="plotly_dark", text_auto=True, width=800,
                   labels={"room_type": "Room Type"})
fig.update_layout(legend_title_text="Room type")
fig.update_yaxes(title="Average Price")
st.plotly_chart(fig)

st.markdown("Private rooms have the highest average price (\$585), while shared rooms have a much lower average price than the rest of room types ($160).")

#Graph 4

mean_prices = df.groupby(["shared_bathrooms"])["price"].mean().round().reset_index()
fig = px.histogram(mean_prices, x="shared_bathrooms", y="price", title="Average Price per Type of Bathroom",
                   color="shared_bathrooms", template="plotly_dark", text_auto=True, width=800,
                   labels={"shared_bathrooms": "Shared Bathrooms"})
fig.update_layout(legend_title_text="Shared Bathrooms")
fig.update_yaxes(title="Average Price")
st.plotly_chart(fig)

st.markdown("Accommodations with shared bathrooms, when known, are cheaper with an average price of $180.")


#Graph 5

mean_prices = df.groupby(["host_is_superhost"])["price"].mean().round().reset_index()
fig = px.histogram(mean_prices, x="host_is_superhost", y="price", title="Average Price per Type of Host",
                   color="host_is_superhost", template="plotly_dark", text_auto=True, width=800,
                   labels={"host_is_superhost": "Superhost"})
fig.update_layout(legend_title_text="Superhost")
fig.update_yaxes(title="Average Price")
st.plotly_chart(fig) 

st.markdown("The fact that the host is a superhost does not increase the price of the accommodation. The average price of accommodations belonging to superhosts is \$365, and the average price of those that are not is $425.")


#Graph 6

mean_prices = df.groupby(["host_identity_verified"])["price"].mean().round().reset_index()
fig = px.histogram(mean_prices, x="host_identity_verified", y="price", title="Average Price per Verified identity",
                   color="host_identity_verified", template="plotly_dark", text_auto=True, width=800,
                   labels={"host_identity_verified": "Verified Identity"})
fig.update_layout(legend_title_text="Verified Identity")
fig.update_yaxes(title="Average Price")
st.plotly_chart(fig)

st.markdown("Accommodations hosted by verified hosts have a higher average price (\$407) compared to those hosted by unverified hosts (\$327).")


#Graph 7

mean_prices = df.groupby(["instant_bookable"])["price"].mean().round().reset_index()
fig = px.histogram(mean_prices, x="instant_bookable", y="price", title="Average Price per Bookable Type",
                   color="instant_bookable", template="plotly_dark", text_auto=True, width=800,
                   labels={"instant_bookable": "Instant Bookable"})
fig.update_layout(legend_title_text="Instant Bookable")
fig.update_yaxes(title="Average Price")
st.plotly_chart(fig)

st.markdown("Accommodations with instant booking option have a higher average price (\$449) compared to those without this option (\$343).")

#Graph 8

mean_price_per_person = (df["price"].mean() / df["accommodates"].mean()).round()
data = {"price_per_person": [mean_price_per_person]}
df_price_per_person = pd.DataFrame(data)
fig = px.bar(df_price_per_person, x=df_price_per_person.index, y="price_per_person",
             title="Average Price per Person per Night",
             labels={"price_per_person": "Price per Person"},
             template="plotly_dark", text_auto=True)
fig.update_yaxes(title="Average Price")
fig.update_xaxes(title="1 Person, 1 Night")
st.plotly_chart(fig)

st.markdown("The average price per person per night is $84.")

#Graph 9

mean_prices = df.groupby(["accommodates"])["price"].mean().round(2).reset_index()
mean_prices["price_per_person"] = (mean_prices["price"] / mean_prices["accommodates"].astype(float)).round(2)
mean_prices["accommodates"] = mean_prices["accommodates"].astype(str)
fig = px.histogram(mean_prices, x="accommodates", y="price_per_person", 
                   title="Average Price per Person per Capacity", color="accommodates",
                   template="plotly_dark", text_auto=True, width=800,
                   labels={"accommodates": "Capacity", "price_per_person": "Price per Person"})
fig.update_yaxes(title="Price per Person")

st.plotly_chart(fig)

st.markdown("The average price per person per night ranges between \$80 and \$100 in more than half of the cases. The lowest average price per person per night is $57 for accommodations with a capacity of 15 people.")

#Graph 10

bins = [0, 1, 2, 3, 4,5]
labels = ["0-1","1-2", "2-3", "3-4", "4-5"]
df["rating_range"] = pd.cut(df["review_scores_rating"], bins=bins, labels=labels, right=False)
mean_prices_by_rating_range = df.groupby("rating_range")["price"].mean().round().reset_index()
fig = px.bar(mean_prices_by_rating_range, x="rating_range", y="price", text_auto=True,
             title="Average Price per Rating Range", color="rating_range",
             labels={"rating_range": "Rating Range", "price": "Average Price"})

st.plotly_chart(fig)

st.markdown("The average price of accommodations is close to \$300 for review ratings between 2 and 5. The average price of accommodations with review ratings between 1 and 2 is higher ($538) than that of accommodations with review ratings between 2 and 5.")









