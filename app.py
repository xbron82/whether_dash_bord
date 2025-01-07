import streamlit as st
import pandas as pd
import requests as resp

st.set_page_config(layout='wide', initial_sidebar_state='expanded')


st.markdown(
 """
 <style>
 .stApp {
background-image: url("https://www.metoffice.gov.uk/binaries/content/gallery/metofficegovuk/hero-images/advice/mountains/view-of-the-peak-district.jpg");
 background-size: cover;
 background-position: center;
 background-repeat: no-repeat;
}
.stTitle {
<p style="color: red";
font-size: 50px;
font-weight: bold;
text-align: center;
margin-bottom: 30px;
}
</style>
""",
unsafe_allow_html=True
)
st.markdown("""
    <div>
    <h2 class="stTitle"> Weather Dashboard </h2>
    </div>
    """, unsafe_allow_html=True)

requests= (resp)
response = resp.get('https://api.open-meteo.com/v1/forecast?latitude=51.5085&longitude=-0.1257&current=temperature_2m,relative_humidity_2m,is_day,rain,snowfall,weather_code,surface_pressure,wind_speed_10m&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,daylight_duration,wind_speed_10m_max&timezone=Europe%2FLondon&past_days=7&models=ukmo_seamless')
selectbox_option = st.sidebar.selectbox('Select the data need to predict',('Temperature', 'Temperature_min','wind speed'))

x = response.json()
response
lat = x['latitude']
lon = x['longitude']
temp = x['current']['temperature_2m']
wind =x['current']['wind_speed_10m']
sp=x['current']['surface_pressure']
rel_hu=x['current']['relative_humidity_2m']
ti=x['current']['time']
sf=x['current']['snowfall']
D_y=x['current']['is_day']

#st.title("Weather Dashboard")
st.sidebar.title("Input Location")
latitude=st.sidebar.number_input("Latitude", value=52.52, step=0.01, format="%.2f")
longitude=st.sidebar.number_input("Logtitude",value=0.91, step=0.01,format="%.2f")


def Day_or_Night():
   if D_y == 1:
       st.metric('Day or Night', "Day")
   else:
        st.metric('Day or Night', "Night")

#3 Columns to display current temperature, wind speed and Day/Night

col1, col2= st.columns(2)
with col1:
    st.metric('Temperature (°C)', temp)

with col2:
    Day_or_Night()

st.subheader("Location Details")
st.write(f"**snowfall**:{sf}")
st.write(f"**time**:{ti}")
st.write(f"**relative_humidity_2m**:{sf}")

# st.subheader("Current Temperature")
# st.write(f"{temp} °C")
st.subheader("currnt wind speed")
st.write(f"{wind} m/s")
st.subheader("currnt surface presuer")
st.write(f"{sp} n/m3")

st.subheader('TODAYS WETHER')
st.title('hello,wellcome to afternoon whether')
st.video('https://www.youtube.com/watch?v=y6QIMQW-dOc')



daily_max_temp_df = pd.DataFrame(x["daily"]["temperature_2m_max"],
                                 x["daily"]["time"])
daily_max_sp_df = pd.DataFrame(x["daily"]["temperature_2m_min"],
                               x["daily"]["time"])
daily_ws_df = pd.DataFrame(x["daily"]["wind_speed_10m_max"],
                               x["daily"]["time"])


# Display line charts based on selection
if selectbox_option == 'Temperature':
    st.line_chart(daily_max_temp_df)
elif selectbox_option == 'Temperature_min':
    st.line_chart(daily_max_sp_df)
else:
    st.line_chart(daily_ws_df)

st.map(pd.DataFrame({'lat': [latitude], 'lon': [longitude]}))

