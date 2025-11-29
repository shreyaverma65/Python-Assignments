🌦️ Weather Data Visualizer – Mini Project
Course: Programming for Problem Solving using Python
Assignment: Data Analysis & Visualization using Real-World Weather Data

📌 Project Overview
This project analyzes real-world weather data and visualizes key insights such as temperature trends, monthly averages, and humidity–temperature relationships. The goal is to learn data cleaning, processing, analysis, and storytelling using Python, Pandas, NumPy, and Matplotlib.
Dataset used: Daily Delhi Climate Dataset (2013–2017)

🛠️ Technologies Used
Python 3
Pandas
NumPy
Matplotlib
VS Code

📂 Project Structure
weather-data-visualizer/
│
├── weather_analysis.py
├── cleaned_weather_data.csv
├── DailyDelhiClimateTrain.csv
│
├── daily_temperature_trend.png
├── monthly_avg_temperature.png
├── humidity_vs_temperature.png
├── combined_plot.png
│
├── report.txt
└── README.md

📊 Tasks Completed
✔ 1. Data Acquisition
Downloaded real-world CSV from Kaggle
Loaded dataset using Pandas

✔ 2. Data Cleaning
Converted date column to datetime
Checked and removed missing values
Filtered relevant columns

✔ 3. Statistical Analysis (with NumPy & Pandas)
Daily statistics → mean, min, max, std
Monthly grouped statistics
Yearly grouped statistics

✔ 4. Visualizations (Matplotlib)
📈 Daily temperature line chart
📊 Monthly average temperature bar chart
🔵 Humidity vs temperature scatter plot
🪟 Combined subplot figure
All plots are saved as .png files.

✔ 5. Exporting Clean Data
Cleaned dataset saved as cleaned_weather_data.csv

📝 Summary of Insights
Temperatures rise sharply from Jan to June (peak summer in May–June)
Cooling begins from July due to monsoon season
Winter months (Dec–Jan) show the lowest temperatures
Humidity decreases as temperature increases (negative correlation)
Seasonal patterns repeat consistently every year

📌 How to Run the Project
Install required libraries:
pip install pandas numpy matplotlib
Run the main analysis file:
python weather_analysis.py
View generated PNG graphs inside the project folder.

📧 Submitted By

Your Name: Shreya Verma
Course: B.Tech CSE (AI & ML)
Assignment: Mini Project – Weather Data Visualizer