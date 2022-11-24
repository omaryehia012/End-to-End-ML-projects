import streamlit as st
import joblib 
import pandas as pd

Inputs = joblib.load(open("Loan_Classification\inputs.h5",'rb'))
Model = joblib.load(open("Loan_Classification\model.h5",'rb))
                         
@st.cache()                         

def predict(Gender,Married,Dependents, Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,
        Loan_Amount_Term,Credit_History,Property_Area):
    test_df = pd.DataFrame(columns = Inputs)
    test_df.at[0,"Gender"] = Gender
    test_df.at[0,"Married"] = Married
    test_df.at[0,"Dependents"] = Dependents
    test_df.at[0,"Education"] = Education
    test_df.at[0,"Self_Employed"] = Self_Employed
    test_df.at[0,"ApplicantIncome"] = ApplicantIncome
    test_df.at[0,"CoapplicantIncome"] = CoapplicantIncome
    test_df.at[0,"LoanAmount"] = LoanAmount
    test_df.at[0,"Loan_Amount_Term"] = Loan_Amount_Term
    test_df.at[0,"Credit_History"] = Credit_History
    test_df.at[0,"Property_Area"] = Property_Area
    result = Model.predict(test_df)[0]
    return result
    

def header(url):
     st.markdown(f'<p style="background-color:#0066cc;color:#33ff33;font-size:24px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)    

# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit Loan Status ML classification App</h1> 
    </div> 
    """
     
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True)
    # following lines create boxes in which user can enter data required to make prediction
    st.sidebar.title("Choose your Features") 
    ApplicantIncome = st.sidebar.slider("Total Applicant Income", min_value=0, max_value=100000, value=0, step=1)
    CoapplicantIncome = st.sidebar.slider("Total Co_Applicant Income", min_value=0, max_value=50000, value=0, step=1)
    LoanAmount = st.sidebar.number_input("Total Loan Amount")
    Loan_Amount_Term = st.sidebar.slider("Total Loan Amount Term", min_value=12, max_value=1000, value=0, step=12)
    Credit_History = st.sidebar.selectbox('Credit_History',(0,1))
    Gender = st.sidebar.selectbox('Select Gender',("Male","Female"))
    Married = st.sidebar.selectbox('Married Status',("Yes","No"))
    Dependents = st.sidebar.selectbox('No of Dependents',('0','1','2','+3'))
    Education = st.sidebar.selectbox('Select Education',("Graduate","Not Graduate"))
    Self_Employed = st.sidebar.selectbox('Are you Self_Employed ?',("Yes","No"))
    Property_Area = st.sidebar.selectbox('Property_Area',("Semiurban","Urban","Rural"))
    result =""
          
    # when 'Predict' is clicked, make the prediction and store it 
    if st.sidebar.button("Predict"): 
        result = predict(Gender,Married,Dependents, Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area)
        label = ["Unfortunately ! Your Loan Rejected","Congratulations ! Accepted Loan"]
        
        ## Print final Prediction 
        st.markdown(f'<h1 style="color:#33ff33;font-size:40px;text-align:center;border-style: solid;border-width:5px;border-color:#fbff00;">{label[result]}</h1>', unsafe_allow_html=True)
   
   ## show resturant image
    st.image('Loan_Classification/images/Loan.jpg')    
     
if __name__=='__main__': 
    main()
