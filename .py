# Import necessary packages
import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

tech_skills = [
    "Python",
    "JavaScript",
    "Java",
    "C++",
    "SQL",
    "HTML/CSS",
    "React",
    "Node.js",
    "Angular",
    "Django",
    "Ruby on Rails",
    "Swift",
    "PHP",
    "Go",
    "Rust",
    "TensorFlow",
    "PyTorch",
    "AWS",
    "Docker",
    "Kubernetes",
]

dummy_companies = [
    "Microsoft",
    "Amazon",
    "Google",
    "Facebook",
    "Apple",
    "Tesla",
    "IBM",
    "Oracle",
    "Netflix",
    "Salesforce",
    "Intel",
    "Cisco",
    "Adobe",
    "NVIDIA",
    "Shopify",
    "VMware",
    "Slack",
    "Zoom",
    "GitHub",
    "Reddit",
]
data = {
    'marks': [90, 34, 88, 45, 75, 60, 40, 70, 30, 82, 38, 66, 57, 79, 41, 55, 84, 36, 62, 72],
    'grades': ['A', 'C', 'A', 'C', 'B', 'B', 'C', 'B', 'D', 'A', 'C', 'B', 'C', 'B', 'C', 'C', 'A', 'C', 'B', 'B']
}

df = pd.DataFrame(data)

grade_mapping = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0}
df['grades'] = df['grades'].map(grade_mapping)

X = df[['marks']]
y = df['grades']

model = LinearRegression()
model.fit(X, y)

def predict_placement(grade):
    if grade >= 3.0:
        return "Placed"
    else:
        return "Not Placed"

st.markdown(
    """
    <style>
    body {
        background-image: url('https://media.istockphoto.com/id/1475870499/photo/education-high-five-and-teacher-with-children-in-classroom-for-learning-support-and.jpg?s=2048x2048&w=is&k=20&c=wS7LezckoSaKJ8zZJJVaHv_eD4YuLih6Ncd4W4jAvcE=');
        background-size: cover;
        background-attachment: fixed;
        background-color: #f3f3f3;  /* Background color behind content */
        font-family: Arial, sans-serif;
    }
    .stApp {
        max-width: 700px;
        margin: 0 auto;
        padding: 2em;
        background-color: rgba(255, 255, 255, 0.9);  /* Content background color with transparency */
        border-radius: 15px;  /* Rounded corners for content */
        box-shadow: 0 4px 6px 0 rgba(0, 0, 0, 0.1);  /* Box shadow for content */
    }
    .stNumberInput input {
        width: 80%;
    }
    .st-title {
        font-size: 28px;  /* Increase title font size */
        color: #333;  /* Title text color */
    }
    .st-write {
        font-size: 16px;  /* Adjust text size in write elements */
        color: #444;  /* Text color for write elements */
    }
    .st-button {
        background-color: #007BFF;  /* Button background color */
        color: white;  /* Button text color */
        font-weight: bold;  /* Make button text bold */
    }
    .st-button:hover {
        background-color: #0056b3;  /* Hover color for button */
    }
    .st-success {
        background-color: #4CAF50;  /* Success message background color */
        color: white;  /* Success message text color */
    }
    .st-info {
        background-color: #007BFF;  /* Info message background color */
        color: white;  /* Info message text color */
    }
    .st-warning {
        background-color: #FFC107;  /* Warning message background color */
        color: white;  /* Warning message text color */
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.sidebar.title("Predict Your Future Here")
selected_page = st.sidebar.radio("Go to", ("Home", "Prediction", "Skills"))

if selected_page == "Home":
    st.title("Welcome to the Student Performance Prediction App")
    st.image("https://niagaraindependent.ca/wp-content/uploads/2019/05/predicting-the-future-1024x640.jpg", use_column_width=True)
    st.write("This app allows you to predict a student's grade based on their marks and provides information about their placement status.")
    st.write("Please use the navigation bar on the left to make predictions.")
    
elif selected_page == "Prediction":
    st.title("Grade Prediction and Placement")
    st.write("Enter the student's marks to predict their grade and placement:")

    marks = st.number_input("Marks (0-100):", min_value=0, max_value=100)
    
    if st.button("Predict"):
        
        grade_mapping = {4.0: 'A', 3.0: 'B', 2.0: 'C', 1.0: 'D'}

        
        predicted_grade = model.predict([[marks]])

        
        predicted_grade_char = grade_mapping.get(round(predicted_grade[0]), 'Unknown Grade')

        
        if predicted_grade is not None:
            
            placement = predict_placement(predicted_grade[0])
            st.success(f"Predicted Grade: {predicted_grade_char}")
            st.success(f"Placement Status: {placement}")

            if placement == "Placed" and predicted_grade_char in ['A', 'B']:
                st.success("🎉 Well done! You are placed! 🎉")
            else:
                st.info("Keep working hard! You'll get there!")

elif selected_page == "Skills":
    st.title("Skills and Company Placement")
    st.write("Enter your skills to predict your company placement:")

    selected_skills = st.multiselect("Select your tech skills:", tech_skills)

    if st.button("Predict Company"):
        
        skill_company_mapping = {
            "Python": ["Microsoft", "Amazon", "Google"],
            "JavaScript": ["Google", "Facebook", "Apple"],
            "Java": ["Amazon", "Google", "Oracle"],
            "C++": ["Microsoft", "IBM", "Intel"],
            "SQL": ["Microsoft", "Oracle", "IBM"],
            "HTML/CSS": ["Google", "Facebook", "Apple"],
            "React": ["Facebook", "Netflix", "Salesforce"],
            "Node.js": ["Amazon", "Netflix", "Salesforce"],
            "Angular": ["Google", "Microsoft", "Intel"],
            "Django": ["Microsoft", "Amazon", "IBM"],
            "Ruby on Rails": ["GitHub", "Reddit", "Shopify"],
            "Swift": ["Apple", "Tesla", "IBM"],
            "PHP": ["Oracle", "Adobe", "GitHub"],
            "Go": ["Google", "Intel", "GitHub"],
            "Rust": ["Intel", "GitHub", "NVIDIA"],
            "TensorFlow": ["Google", "Amazon", "Facebook"],
            "PyTorch": ["Facebook", "Microsoft", "NVIDIA"],
            "AWS": ["Amazon", "Netflix", "Salesforce"],
            "Docker": ["Amazon", "Microsoft", "IBM"],
            "Kubernetes": ["Google", "Microsoft", "Cisco"],
        }
        selected_companies = []
        for skill in selected_skills:
            if skill in skill_company_mapping:
                selected_companies.extend(skill_company_mapping[skill])

        if selected_companies:
            st.success(f"Predicted Company Placement: {', '.join(selected_companies)}")
        else:
            st.warning("No available companies for your selected skills.")
