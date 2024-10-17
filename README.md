# 🎯 AI-Powered Marketing System

This project demonstrates an AI-based Marketing System that analyzes customer behavior to provide insights and personalized recommendations. It uses Streamlit for the web interface, pandas for data manipulation, and Plotly for visualizations. The project is designed to help companies like Amazon and Flipkart optimize their marketing strategies.

## ⚡ Features

### 📊 Customer Dashboard:
- Displays key metrics like total items sold, total revenue, and average ratings.
- Visualizations of customer data, including gender distribution and spending habits by age and gender.

### 🤖 AI-Powered Marketing Insights:
- Customer segmentation based on age group to predict future purchasing behaviors.
- Bar charts and scatter plots showcasing average spend, satisfaction levels, and total spend vs. age by gender.

### 💡 Personalized Product Recommendations:
- Uses Collaborative Filtering or Content-Based Filtering to predict product recommendations.
- Visualizes the frequency of recommended products based on similar customer profiles.

### 📈 Predictive Marketing Analysis:
- Predicts customer behavior using algorithms like Logistic Regression and Support Vector Machines (SVM) for targeted advertising and customer engagement.

## 🛠️ Tech Stack
- 🖥️ **Python**: Core programming language used for the project.
- 🌐 **Streamlit**: Framework for building the interactive web interface.
- 📊 **Pandas**: Library for data analysis and manipulation.
- 📉 **Plotly**: Data visualization library for charts and graphs.
- 🤖 **Machine Learning Algorithms**: Collaborative Filtering, Logistic Regression, Support Vector Machines (SVM).

## 🚀 Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/ai-marketing-system.git
    ```
2. Navigate to the project directory:
    ```bash
    cd ai-marketing-system
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the Streamlit app:
    ```bash
    streamlit run new.py
    ```

## 📂 Project Files

- **new.py**: Main Python script for running the Streamlit app.
- **data.csv**: CSV file containing customer behavior data (ensure columns like Product, Recommendations are included).
- **README.md**: Documentation for the project.
- **requirements.txt**: File listing the necessary libraries for the project.

## 💻 How It Works

1. **Customer Dashboard**: Displays an overview of customer behavior with metrics and visualizations.
2. **AI-Powered Insights**: Analyzes customer data for marketing insights, such as age-based segmentation and satisfaction levels.
3. **Personalized Recommendations**: Suggests products using recommendation algorithms.
4. **Predictive Marketing**: Uses machine learning to predict customer behavior for targeted advertising.

## 📈 Usage

Prepare your dataset in CSV format (`data.csv`) with the following structure:

| Column Name                | Description                                      |
| -------------------------- | ------------------------------------------------ |
| Customer ID                | Unique customer identifier                       |
| Age                        | Customer's age                                   |
| Gender                     | Customer's gender                                |
| Total Spend                | Total amount spent by the customer               |
| Average Rating             | Customer's average product rating                |
| Items Purchased            | Total number of items purchased                  |
| Days Since Last Purchase  | Days since the customer last purchased           |
| Satisfaction Level         | Customer's satisfaction level (1-5)              |
| Product                    | Product name                                     |
| Recommendations            | Number of recommendations for the product        |

Run the app and navigate between **Customer Dashboard** and **AI Marketing Insights** via the sidebar to view different analytics and predictions.

## 🔮 Future Enhancements

- **AI Models for Personalized Offers**: Real-time personalized product suggestions using more advanced machine learning models.
- **Enhanced Product Recommendations**: Improve the recommendation engine with AI algorithms like Collaborative Filtering.
- **Targeted Advertising**: Use AI models to segment high-potential customers for marketing campaigns.

## 💡 Contributing

We welcome contributions! Feel free to fork the project, submit a pull request, or open an issue to discuss your ideas.
