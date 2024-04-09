# --------------------LIBRARIES----------------------------#

import streamlit as st
import base64

# -----------------SITE CONFIGURATION----------------#

st.title("Power BI Panel")

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

#-------------------PowerBI Panel-------------------------#

power_bi_url = "https://app.fabric.microsoft.com/reportEmbed?reportId=5d8ec6fb-a47b-42e0-ac55-95fdff5fc28c&autoAuth=true&ctid=8aebddb6-3418-43a1-a255-b964186ecc64"

iframe_width = 1300
iframe_height = 600

# Usa la función 'iframe' de Streamlit para incrustar el panel de Power BI
st.markdown(f'<iframe src="{power_bi_url}" width={iframe_width} height={iframe_height} style="position:absolute; left:-300px;"></iframe>', unsafe_allow_html=True)


