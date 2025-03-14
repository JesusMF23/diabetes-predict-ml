#  PROYECTO CONSOLIDACION STREAMLIT: FUNCION app.py

# Importaciones
import streamlit as st
import streamlit.components.v1 as stc
from eda_app import run_eda_app
from ml_app import run_ml_app

# Función main()
def main():
	st.sidebar.title("Navigation")
	selection = st.sidebar.selectbox("Go to", ["Home", "EDA", "ML", "Info"])

	if selection == "Home":
		st.title("App for early detection of DM")
		st.write("Dataset that contains signals and symptoms that can indicate diabetes or possibility of diabetes.")
		
		st.title("Data source")
		st.code("- https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset")

		st.title("App content")
		st.code("- EDA section: Exploratory Data Analysis\n- ML section: Diabetes prediction based on ML (Machine Learning) models")
		
	elif selection == "EDA":
		run_eda_app()
		
	elif selection == "ML":
		run_ml_app()
		
	elif selection == "Info":
		st.title("Project Information")
		st.write("This project is part of the Masters Degree in Data Engineering")
		st.subheader("MBIT Website")
		st.markdown("[Navigate to MBIT School](https://mbitschool.com)")
		stc.iframe("https://www.mbitschool.com")

if __name__ == '__main__':
	main()