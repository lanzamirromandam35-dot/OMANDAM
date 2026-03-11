import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

## I want to make the PAge more wider
st.set_page_config(layout="wide")

## This is the sidebar navigation
st.sidebar.title("Categories")

## i chose a raddio button for the section
page = st.sidebar.radio(
    "choose a category",
    ["pictures", "audio", "VIDEOS", "about"],
    captions = ["the gallery", "some audio", "random videos", "about"]
)


## TITLE OR SOMETHING
st.title ("SIMPLE GALLERY")
st.write ("IMAGES, MUSIC, VIDEOS and about")

## Section for pictures ONLY!
if page == "pictures":
    st.header ("retro style images")
    st.subheader ("some IMAGES may be small but it all comes down to their native resolution")
    images = [ 
        "retro1.jpg",
        "retro2.jpg",
        "retro3.jpg",
        "retro4.jpg",
        "retro5.jpg",
        "https://frutigeraeroarchive.org/images/wallpapers/asadal_stock/asadal_stock_16.jpg",
        "https://frutigeraeroarchive.org/images/wallpapers/asadal_stock/asadal_stock_17.jpg",
        "https://frutigeraeroarchive.org/images/wallpapers/asadal_stock/asadal_stock_30.jpg",
    ]
    for i in range(0, len(images), 3):
        cols = st.columns(3)
        for col, img in zip(cols, images[i:i+3]):
            with col:
                st.image(img, width=300)
##Upload ppictures if you want
    uploaded_img = st.file_uploader("UPload your photo", type = ["jpg", "png", "jpeg"])
    if uploaded_img:
        st.image(uploaded_img, use_column_width=True)

## AUDIO
elif page == "audio":
    col1, col2, = st.columns(2)
    with col1: 
        components.iframe (
       "https://open.spotify.com/embed/track/70LcF31zb1H0PyJoS1Sx1r?si=ef57f8dbbe274d67",
       width ="100%", 
       height= 152
   )
    with col2:
        components.iframe (
        "https://open.spotify.com/embed/track/0GgN4MhR5GKn5IcKN0e0rG?si=97f7f34b6f0d42ee",
        width ="100%",
        height = 152
    )
    col3, col4 = st.columns(2)
    with col3:
        components.iframe (
       "https://open.spotify.com/embed/track/2luxd3WEcEACrORUnXvITr?si=73d3ea721b164202",
       width = "100%",
       height = 152
    )
    with col4:
        components.iframe (
        "https://open.spotify.com/embed/track/7lRlq939cDG4SzWOF4VAnd?si=e7b6f28385fb40e8",
        width = "100%",
        height = 152
    )
    col5, col6 = st.columns(2)
    with col5:
        components.iframe (
            "https://open.spotify.com/embed/track/5dTHtzHFPyi8TlTtzoz1J9?si=013796d2cbb54229",
            width = "100%",
            height = 152
        )
    with col6:
        components.iframe (
            "https://open.spotify.com/embed/track/4RAOI1etsgbh5NP3T5R8rN?si=69d890f25c484b4a",
            width = "100%",
            height = 152
        )

##VIDEOS
elif page == "VIDEOS":
    youtube_links = [
    "https://youtu.be/17Sv2FAZnkw?si=f0ux75OV0vJF8IXc",
    "https://youtu.be/5sMpHfX5bPY?si=xpsCuixL1dL_sYcT",
    "https://youtu.be/FtutLA63Cp8?si=dBApxHxsJ5SYDGJI",
    "https://youtu.be/gq7VDRGMwhI?si=bTkTzuhPySkFbyPt",
    "https://youtu.be/tMQ28t6t9_w?si=7F_ewMwh_l8iSVkn",
    ]
    for link in youtube_links:
        st.video(link)

elif page == "about":
    st.header ("ABOUT")
    st.subheader("What the app does:")
    st.write("""This is a \\multimedia gallery app\\ built with Streamlit. 
    Users can view images, listen to music (Spotify or YouTube), and watch videos. 
    It organizes content in **clean, responsive grids** for easy browsing. ALSO YOU CAN UPLOAD YOUR IMAGE
    """)

    st.subheader("Target users:")
    st.write("""
    - Students, artists, or hobbyists who want to showcase or browse media.
    - Anyone looking for a **simple gallery** to explore images, music, and videos in one place.
    """)

    st.subheader("Inputs and Outputs:")
    st.write("""**Inputs:**
    - Users can upload images (JPG, PNG, JPEG) to the gallery.  
    - Music and videos can be provided via URLs (Spotify, YouTube, or MP3 links).  

    **Outputs:**
    - Images are displayed in a **3-column gallery grid**.  
    - Music is embedded in a **responsive grid with built-in players**.  
    - Videos appear in a **grid layout** with play/pause and volume controls.  
    - Uploaded images appear instantly in the gallery.
    """)

