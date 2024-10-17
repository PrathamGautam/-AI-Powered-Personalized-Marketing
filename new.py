import streamlit as st
import pandas as pd
import plotly.express as px

# Function to get metric cards
def get_metric_cards(df):
    """Define all the cards with metrics."""
    cards = [
        {'label': 'Number of customers', 'value': len(df['Customer ID'].unique())},
        {'label': 'Total number of items sold', 'value': df['Items Purchased'].sum()},
        {'label': 'Total Revenue (USD)', 'value': round(df['Total Spend'].sum())},
        {'label': 'Average Rating', 'value': round(df['Average Rating'].mean(), 1)},
        {'label': 'Average Days Since Last Purchase', 'value': round(df['Days Since Last Purchase'].mean(), 1)}
    ]
    return cards

# Pie chart for Gender distribution
def get_gender_pie_chart(df, color_map):
    genders = df['Gender'].unique()
    gender_counts = df['Gender'].value_counts()
    gender_dict = {'Gender': genders, 'Counts': [gender_counts[k] for k in genders]}
    df_gender_counts = pd.DataFrame(gender_dict)
    fig = px.pie(df_gender_counts, values='Counts', names='Gender', color='Gender', color_discrete_map=color_map)
    fig.update_layout(
        legend=dict(orientation='h', yanchor="bottom", y=1),
        legend_title_text='Gender'
    )
    return st.plotly_chart(fig, use_container_width=True)

# Scatter plot: Total Spend vs Average Rating
def get_spend_vs_rating_chart(df, marker_color):
    fig = px.scatter(df, x='Average Rating', y='Total Spend', color_discrete_sequence=[marker_color])
    return st.plotly_chart(fig, use_container_width=True)

# Scatter plot: Average Rating vs Satisfaction Level
def get_rating_vs_satisfaction_chart(df, marker_color):
    fig = px.scatter(df, x='Satisfaction Level', y='Average Rating', color_discrete_sequence=[marker_color])
    return st.plotly_chart(fig, use_container_width=True)

# Bar chart: Total Spend vs Age by Gender
def get_spend_vs_age_chart(df, color_map):
    df = df.groupby(['Gender', 'Age'])['Total Spend'].sum().to_frame().reset_index()
    fig = px.bar(df, x='Age', y='Total Spend', color='Gender', color_discrete_map=color_map)
    fig.update_layout(
        legend=dict(orientation='h', yanchor="bottom", y=1),
        legend_title_text='Gender'
    )
    return st.plotly_chart(fig, use_container_width=True)

# New section: Personalized Product Recommendations
def get_recommendations_chart(df):
    st.subheader("Personalized Product Recommendations (Collaborative Filtering)")
    st.write("""
    **AI Algorithm: Collaborative Filtering or Content-Based Filtering**  
    This chart shows the frequency of product recommendations based on similar customer profiles. 
    It drives engagement and boosts sales by offering personalized suggestions.
    """)

    # Check if 'Product' and 'Recommendations' columns exist
    if 'Product' not in df.columns or 'Recommendations' not in df.columns:
        st.error("The dataset doesn't contain 'Product' or 'Recommendations' columns. Please check your data.")
        return

    # Create bar chart for product recommendations
    recommended_products = df.groupby('Product')['Recommendations'].sum().reset_index()
    fig = px.bar(recommended_products, x='Product', y='Recommendations', title='Product Recommendations based on Similar Users')
    st.plotly_chart(fig, use_container_width=True)


# New section: Targeted Advertising and Customer Engagement
def get_targeted_advertising_chart(df):
    st.subheader("Targeted Advertising and Customer Engagement (Classification)")
    st.write("""
    **AI Algorithm: Logistic Regression or Support Vector Machines (SVM)**  
    This scatter plot classifies customers into high-potential and low-potential buyers. Businesses can focus ad 
    spending on high-potential buyers, optimizing marketing strategies.
    """)
    
    # Sample scatter plot for high-potential vs low-potential buyers
    df['Potential'] = df['Total Spend'].apply(lambda x: 'High Potential' if x > df['Total Spend'].median() else 'Low Potential')
    fig = px.scatter(df, x='Customer ID', y='Total Spend', color='Potential', title='Customer Potential Classification for Targeted Advertising')
    st.plotly_chart(fig, use_container_width=True)

# AI-Powered Marketing System with Explanation
def ai_marketing_system_with_explanation(df):
    st.title("AI-Powered Marketing System")

    # Step 1: Customer Segmentation (Clustering)
    st.header("Customer Segmentation")
    st.write("""
    **AI Algorithm: K-Means Clustering or Hierarchical Clustering**  
    Customer segmentation divides the customer base into groups based on behavior and demographics.
    This allows businesses to offer personalized recommendations and marketing strategies for each
    customer group. Companies like Amazon and Flipkart use this to target specific audiences with
    tailored advertisements and offers.
    """)
    
    # Bar chart for Customer Segmentation
    age_segment = df.groupby(pd.cut(df['Age'], bins=[18, 25, 35, 45, 60, 100]))['Total Spend'].sum().reset_index()
    age_segment['Age'] = age_segment['Age'].astype(str)  # Convert intervals to string
    fig = px.bar(age_segment, x='Age', y='Total Spend', title='Total Spend by Age Group')
    st.plotly_chart(fig)

    # Step 2: Predictive Analytics (Regression)
    st.header("Predictive Marketing Insights")
    st.write("""
    **AI Algorithm: Linear Regression or Decision Trees**  
    Predictive analytics help estimate future customer behaviors based on past data. For example,
    businesses can predict customer purchase patterns, expected spend, and product preferences.
    Platforms like Amazon use this to make proactive recommendations and tailor the shopping
    experience to customer behavior.
    """)
    
    # Bar chart for Predictive Insights
    avg_purchase_by_gender = df.groupby('Gender')['Total Spend'].mean().reset_index()
    fig = px.bar(avg_purchase_by_gender, x='Gender', y='Total Spend', title='Average Spend by Gender')
    st.plotly_chart(fig)

    # Step 3: Personalized Recommendations
    get_recommendations_chart(df)

    # Step 4: Targeted Advertising and Customer Engagement
    get_targeted_advertising_chart(df)

# Main function
def main():
    # Load data
    df = pd.read_csv('data.csv')

    # Define color map for genders
    color_map = {'Female': '#000001', 'Male': '#000002'}

    # Multi-page layout
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Customer Dashboard", "AI-Powered Marketing System with Explanation"])

    if page == "Customer Dashboard":
        st.title('E-commerce Customer Behaviour')

        # Metric Cards
        st.markdown("<h2 style='text-align: center;'>Overview</h2>", unsafe_allow_html=True)
        for card in get_metric_cards(df):
            st.metric(**card)

        # Gender pie chart
        st.markdown("<h2 style='text-align: center;'>Gender distribution</h2>", unsafe_allow_html=True)
        get_gender_pie_chart(df, color_map)

        # Spend vs Rating + Rating vs Satisfaction
        gender_list = ['All', 'Female', 'Male']
        selected_genders = st.selectbox('Select gender(s)', gender_list, index=0)

        if selected_genders == 'All':
            df_selected_genders = df
            color_for_selected_gender = '#00CC96'
        else:
            df_selected_genders = df[df['Gender'] == selected_genders]
            color_for_selected_gender = color_map[selected_genders]

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("<h2 style='text-align: center;'>Total spend vs Average rating</h2>", unsafe_allow_html=True)
            get_spend_vs_rating_chart(df_selected_genders, color_for_selected_gender)

        with col2:
            st.markdown("<h2 style='text-align: center;'>Average Rating vs Satisfaction Level</h2>", unsafe_allow_html=True)
            get_rating_vs_satisfaction_chart(df_selected_genders, color_for_selected_gender)

        # Spend vs Age by Gender
        st.markdown("<h2 style='text-align: center;'>Total spend vs Age by Gender</h2>", unsafe_allow_html=True)
        get_spend_vs_age_chart(df, color_map)

    elif page == "AI-Powered Marketing System with Explanation":
        ai_marketing_system_with_explanation(df)

if __name__ == '__main__':
    main()
