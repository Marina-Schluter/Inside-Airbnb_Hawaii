# --------------------LIBRARIES----------------------------#

import streamlit as st
import base64

# -----------------SITE CONFIGURATION----------------#

st.title("Data Analysis Process & Highlights")

#------------------BACKGROUND IMAGE--------------------#

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

# --------------------SIDEBAR-----------------------------#

logo="Multipage_app/pages/pages/hawaii t-shirt design_6170575.png"             
st.sidebar.image(logo, width=120)

#--------------------Preliminary-------------------------#

st.markdown("### **Preliminary study of the information**")
st.image("Multipage_app/pages/pages/preliminary check.png", width=1000)
st.write("")
st.image("Multipage_app/pages/pages/Null Values listingsdf.png", width=1000)
st.write("")

#----------------Cleaning Data----------------------------#

st.markdown("### **Data Cleaning on Listings file**")

st.markdown("#### **Combining Listings files**")
st.image("Multipage_app/pages/pages/Data cleaning, combining files.png", width=1000)
st.write("")

st.markdown("#### **Combining Columns**")
st.image("Multipage_app/pages/pages/Data cleaning, combining columns.png", width=1000)
st.markdown("- Both description and neighbourhood_overview have null spaces and contain a written description of the accommodation. Combining them results in a column with no null values. ")
st.markdown("- The bathrooms column has 9% null values while the bathrooms_text column does not. By extracting the numbers from the bathrooms_text column and combining the columns, we get a new column with all rows filled in and no nulls. ")
st.write("")

# st.markdown("#### **Price study on calendar file**")
# st.markdown("- The price of accommodation is fixed for each listing_id, it does not vary according to the month or time of the year.")
# st.write("")

st.markdown("#### **Null treatment according to the different columns**")
st.image("Multipage_app/pages/pages/Null values changes.png", width=800)
st.image("Multipage_app/pages/pages/deleting columns.jpg",width=800)
st.markdown("- After this changes, only review_scores_rating column has null values, a 23%. Will work with that without changing values")
st.write("")

st.markdown("#### **Correlation**")
st.image("Multipage_app/pages/pages/correlation.png", width=800)
st.markdown("- Price shows no direct correlation with any other numerical variable")
st.markdown("- There is a positive correlation between room capacity and the number of beds.")
st.markdown("- There is a positive correlation between room capacity and the number of bathrooms.")
st.markdown("- There is a positive correlation between the overall number of reviews and the number of reviews in the last 12 months.")
st.write("")

st.markdown("### **Final csv**")
st.markdown("- After studying the background information and transforming it, a new working file has been created that will underpin all the subsequent analyses that appear throughout this app. The new file is: `Hawaii.csv`. ")


