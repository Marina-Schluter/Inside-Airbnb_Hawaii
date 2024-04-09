# --------------------LIBRARIES----------------------------#

import streamlit as st
import base64

# -----------------SITE CONFIGURATION----------------#

st.title("Uselful information about Hawaii")

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


# --------------------SIDEBAR-----------------------------#

logo="Multipage_app/pages/pages/hawaii t-shirt design_6170575.png"             
st.sidebar.image(logo, width=120)

#----------------------CONTENT----------------------------#

#Selectable 1

choice = st.radio("Seasons:",["Kau","Hoolio"])

if choice == "Kau":
    st.write("Summer, from May to October.")
    
if choice == "Hoolio":
    st.write("Winter, from November to April.")

#Selectable 2

choice= st.radio("Average temperature",["Kau","Hoolio"])

if choice == "Kau":
    st.write("In summer, the average daytime temperature is 29.4 °C (85 °F) at sea level.")
    
if choice == "Hoolio":
    st.write("In winter, the average daytime temperature is 25.6 °C (78 °F).")

#Selectable 3

choice = st.radio("Overview:", ["Island of Hawai'i","Kauai", "O'ahu","Moloka'i","Läna'i","Maui","Island of Hawai'i"])

if choice == "Island of Hawai'i":
    st.write("From active volcanoes to coffee farms and beautiful beaches to rich history. Known as the Big Island, it is the southeasternmost and largest of the Hawaiian Islands.")
    
elif choice == "Kauai":
    st.write("The **Garden Isle** is home to some of the most dramatic scenery in the South Pacific.")

elif choice == "O'ahu":
    st.write("The **Heart of Hawai'i** is home to the capital city of Honolulu and legendary surf towns like Hale''iwa.")
    
elif choice == "Moloka'i":
    st.write("True to its island roots, Moloka'i is filled with rustic charm and epic beauty.")
    
elif choice == "Läna'i":
    st.write("Lāna'i is an island of contradictions and balances restful luxury with rugged terrain.")
    
elif choice == "Maui":
    st.write("From its famous beaches to the peak of Haleakalā, Maui offers a wealth of unforgettable experiences.")
    
    
    
#Selectable 4

choice = st.radio("Places to visit:", ["Hawaii Volcanoes National Park","Kawaihae", "Hilo","Mauna Loa","Waipio Valley","Kilauea","Mauna Kea","Subaru Telescope","Waimea"])

if choice == "Hawaii Volcanoes National Park":
    st.write("Active volcanic area along the southeastern shore of the island of Hawaii, Hawaii state, U.S., located southwest of Hilo. Established in 1961 and formerly a part of Hawaii National Park (established 1916), it occupies an area of 505 square miles (1,308 square km) and includes two active volcanoes—Mauna Loa and Kilauea—25 miles (40 km) apart. The park was designated a UNESCO World Heritage site in 1987.")

elif choice == "Kawaihae":
    st.write("Deepwater port lying along Kawaihae Bay, on the northwestern coast of Hawaii island, Hawaii, U.S. It marks the northernmost point of a 40-mile (65-km) stretch known as the “Gold Coast,” a resort-beach development area that follows the Queen Kaahumanu Highway around Anaehoomalu and Kiholo bays.")
    
elif choice == "Hilo":
    st.write("City seat of Hawaii county, northeastern Hawaii island, Hawaii, U.S. It lies along Hilo Bay and is the island's business center.")
    
elif choice == "Mauna Loa":
    st.write("The world's largest volcano, located on the south-central part of the island of Hawaii, Hawaii state, U.S., and a part of Hawaii Volcanoes National Park. One of the largest single mountain masses in the world, Mauna Loa (meaning “Long Mountain” in Hawaiian) rises to 13,677 feet (4,169 metres) above sea level and constitutes half of the island's area.")
    
elif choice == "Waipio Valley":
    st.write("Valley in the Kohala Mountains, northern Hawaii island, Hawaii, U.S. Enveloped on three sides by 2,500-foot- (750-metre-) high cliffs ribboned with spectacular waterfalls (including Hiilawe Falls, which drops more than 1,000 feet [300 metres]), the picturesque valley faces a heavy Pacific surf along the Hamakua coast, where it is fringed by an impassable reef. The valley, whose name means “Curving Water,” was once the home of a large native community and is the birthplace of many island legends. King Kamehameha I was raised in the area, but it has been virtually uninhabited since 1946, when a tsunami devastated the valley. Its flat alluvial floor is covered with lush vegetation and drained by Waipio Stream, which enters the ocean at a black-sand beach. Swift headwaters and landslides have caused Kawainui Stream to be diverted westward into the valley. The fertile floor is now used for taro farming, and the sheer cliffs are a popular challenge for island rock climbers.")
    
elif choice == "Kilauea":
    st.write("The world's most active volcanic mass, located on the southeastern part of the island of Hawaii, Hawaii state, U.S. The central feature of Hawaii Volcanoes National Park, Kilauea (“Much Spreading” in Hawaiian), is an elongated dome built of lava eruptions from a central crater and from lines of craters extending along east and southwest rifts, or fissures.")
    
elif choice == "Mauna Kea":
    st.write("Dormant volcano, north-central Hawaii island, Hawaii, U.S. The focus of a state forest preserve, it is the highest point in the state (13,796 feet [4,205 metres] above sea level). Mauna Kea (Hawaiian: “White Mountain”), which last erupted about 4,500 years ago, is often snowcapped. Its dome is 30 miles (50 km) across, with numerous cinder cones, and is the site of a major astronomical observatory.")

elif choice == ("Subaru Telescope"):
    st.write("A Japanese 8.2-metre (27-foot) optical-infrared telescope located on the dormant volcano Mauna Kea (4,163 metres [13,658 feet]) on the island of Hawaii.")

elif choice == ("Waimea"):
    st.write("Village, Hawaii county, north-central Hawaii island, Hawaii, U.S. It is situated on the Mauna Kea–Kohala Saddle (2,669 feet [814 metres]), northeast of Kailua-Kona. In the 1790s the English navigator George Vancouver presented a gift of five cattle to King Kamehameha I. The king placed a kapu (royal taboo) on the killing of the cattle, and within two decades thousands of wild cattle roamed vast swaths of the area, destroying much of the local agriculture.")
    

    
st.markdown("**Useful links:**")
st.markdown("https://www.gohawaii.com/")
st.markdown("https://portal.ehawaii.gov/")
st.markdown("https://www.britannica.com/place/Hawaii-island-Hawaii")

