# PROYECTO DE CONSOLIDACION STREAMLIT: FUNCION eda_app.py

# Importaciones: streamlit, pandas, matplotlib, seaborn
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Función principal que emplearemos en la APP
def run_eda_app():
	st.title("Exploratory Data Analysis")
	analysis_option = st.sidebar.selectbox("Choose analysis type", ["Descriptive", "Graphics"])
		
	if analysis_option == "Descriptive":
		st.header("Descriptive Analysis")
		data_upload = pd.read_csv("data/diabetes_data_upload.csv")

		data_clean = pd.read_csv("data/diabetes_data_upload_clean.csv")

		print("Columns:", data_upload.columns)
		print("Data types:", data_upload.dtypes)
		
		st.subheader("Data Overview")
		st.dataframe(data_upload)
		
		with st.expander("Data Types"):
			st.write(data_upload.dtypes)
		
		with st.expander("Descriptive Statistics"):
			st.write(data_clean.describe())
		
		with st.expander("Data Values (First 5 Rows)"):
			st.write(data_upload.head())
		
	elif analysis_option == "Graphics":
		st.header("Graphical Analysis")
		data_upload = pd.read_csv("data/diabetes_data_upload.csv")
		
		with st.expander("Distribution by Gender"):
			col1,col2 = st.columns(2)
			gender_counts = data_upload['Gender'].value_counts()

			with col1:
				fig = px.pie(names=gender_counts.index, values=gender_counts.values)
				st.plotly_chart(fig)

			with col2:
				st.write(gender_counts)
		
		with st.expander("Distribution by Class"):
			col1,col2 = st.columns(2)
			class_counts = data_upload['class'].value_counts()
			with col1:
				fig = px.pie(names=class_counts.index, values=class_counts.values)
				st.plotly_chart(fig)
			
			with col2:
				st.write(class_counts)
		
		with st.expander("Age Distribution (Bar Plot)"):
			freq_data = pd.read_csv("data/freqdist_of_age_data.csv")
			fig, ax = plt.subplots()
			sns.barplot(x="Age", y="count", data=freq_data, ax=ax)
			st.pyplot(fig)
		
		with st.expander("Boxplot of Ages by Gender"):
			fig, ax = plt.subplots()
			sns.boxplot(x="Gender", y="Age", data=data_upload, ax=ax)
			st.pyplot(fig)
		
		with st.expander("Correlation Heatmap"):
			data_clean = pd.read_csv("data/diabetes_data_upload_clean.csv")
			corr_matrix = data_clean.corr()
			fig, ax = plt.subplots()
			sns.heatmap(corr_matrix, annot=True, ax=ax)
			st.pyplot(fig)

# Fin de la FUNCION







