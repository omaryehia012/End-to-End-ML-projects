!pip install joblib

import pickle
import joblib
import streamlit as st
from variables import *
 
# loading the trained model
scaler = joblib.load(r'C:\Users\ascom\Epsilon Training work\Classification_2\scaler.h5')
model = joblib.load(r'C:\Users\ascom\Epsilon Training work\Classification_2\Zomato Restaurants')
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(online_order, book_table, votes,rest_type,cuisines,cost_per_two, type,city):   
 
    # Pre-processing user input    
    if online_order.lower() == "yes":
        online_order = 0
    else:
        online_order = 1

    if book_table.lower() == "yes":
        book_table = 0
    else:
        book_table = 1

    rest_type = rest_type_dictionary[rest_type]
    cuisines=cuisines_dictionary[cuisines]
    type=type_dictionary[type]
    city=city_dictionary[city]
 
    # Making predictions 
    prediction = model.predict(scaler.transform([[online_order, book_table, votes,rest_type,cuisines,cost_per_two, type,city]]))
     
    if prediction == 0:
        pred = 'Rating lower than 3.7'
    else:
        pred = 'Rating higher than 3.7'
    return pred


def header(url):
     st.markdown(f'<p style="background-color:#0066cc;color:#33ff33;font-size:24px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit Zomato Resturants ML classification App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
    #st.image('Zomato-1.jpg')

          
    # following lines create boxes in which user can enter data required to make prediction
    st.sidebar.title("Choose your Features") 
    online_order = st.sidebar.selectbox('Online Order',("Yes","No"))
    book_table = st.sidebar.selectbox('Book Table',("Yes","No"))
    votes = st.sidebar.number_input("Total number of votes")
    rest_type = st.sidebar.selectbox('Resturant Type',Rest_type)
    cuisines = st.sidebar.selectbox('Cuisines',Cuisines)
    cost_per_two = st.sidebar.number_input("Total Cost per two persons")
    type = st.sidebar.selectbox('Type',Type)
    city = st.sidebar.selectbox('City',City) 
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.sidebar.button("Predict"): 
        result = prediction(online_order, book_table, votes,rest_type,cuisines,cost_per_two, type,city)

        ## show chosen Features
        col1, col2, col3,col4,col5,col6,col7,col8 = st.columns(8)

        with col1:
            st.markdown("Online Order")
            st.success(f"{online_order}")
        with col2:
            st.markdown("Book Table")
            st.success(f"{book_table}") 
        with col3:
            st.markdown("No of Votes")
            st.success(f"{votes}") 
        with col4:
            st.markdown("Resturant type")
            st.markdown(f"{rest_type}") 
        with col5:
            st.markdown("Cuisines")
            st.markdown(f"{cuisines}") 
        with col6:
            st.markdown("Cost for Two")
            st.success(f"{cost_per_two}") 
        with col7:
            st.markdown("Type")
            st.success(f"{type}") 
        with col8:
            st.markdown("City")
            st.markdown(f"{city}") 


        ## Print final Prediction 
        st.markdown(f'<h1 style="color:#33ff33;font-size:50px;text-align:center;border-style: solid;border-width:5px;border-color:#fbff00;">{result}</h1>', unsafe_allow_html=True)
   
   ## show resturant image
    st.image('Zomato-1.jpg')    
     
if __name__=='__main__': 
    main()
