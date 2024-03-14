import streamlit as st




# Set the page configuration
st.set_page_config(
    page_title="My Portfolio",
    page_icon="📁",
    layout="centered",
    initial_sidebar_state="expanded"
)



# Define the sections
sections = ["👋About", "💪Skills", "📁Projects"]

# Create a navigation bar
selected_section = st.sidebar.radio("Navigate", sections)

# About Section
if selected_section == "👋About":
    st.header("About Me", divider = 'orange')
    col1, col2 = st.columns(2) # creating columns

    with col1:
        st.image("https://github.com/IssacDavidi/data_project/blob/main/photos/human.jpeg?raw=true", use_column_width = True)

    with col2:
        st.markdown("""
<style>
.big-font {
    font-size:20.3px !important;
}
</style>
""", unsafe_allow_html=True)
        st.markdown('<p class="big-font">Greetings! Im Isaac, an Economics and Business Management graduate driven by a passion for data. With strong analytical abilities and business acumen, I leverage data-driven insights to fuel strategic decision-making. Proficient in data analysis tools, I blend technical expertise with economic principles to translate complex datasets into actionable solutions. Eager to contribute my unique skill set to an organization that values data-driven approaches.</p>', unsafe_allow_html=True)





# Skills Section
elif selected_section == "💪Skills":
    st.header('Skills', divider = 'rainbow')
    col1, col2 = st.columns([1,12])
    with st.container():  # SQL
        with col1:
            st.image('https://github.com/IssacDavidi/data_project/blob/main/photos/sql.webp?raw=true', width = 40)
        with col2:
            st.subheader('SQL')

        # Stars line
        col1, col2 = st.columns([1,8])
        with col1:
            st.write(':orange[Skill Level]')
        with col2:
            st.image('https://github.com/IssacDavidi/data_project/blob/main/photos/4stars.png?raw=true',  width = 150)

        st.write("- Proficient in precise data retrieval and manipulation through SQL queries.")
        st.write("- Adept in leveraging subqueries for intricate data analysis.")
        st.write("- Skilled in seamless data integration using various JOIN operations.")
        st.write("- Proficient in string operations for enhanced data presentation.")
        st.write("- Demonstrated ability to extract insightful information for strategic business decisions.")





    with st.container():  # Python
        col1, col2 = st.columns([1,12])
        with col1:
            st.image('https://github.com/IssacDavidi/data_project/blob/main/photos/python.png?raw=true', width = 50)
        with col2:
            st.subheader('Python')

        # Stars line
        col1, col2 = st.columns([1,8])
        with col1:
            st.write(':orange[Skill Level]')
        with col2:
            st.image('https://github.com/IssacDavidi/data_project/blob/main/photos/3stars.png?raw=true',  width = 150)


        st.write('- Proficient in data manipulation and analysis with Pandas and NumPy')
        st.write('- Creating interactive dashboards and visualizations using Plotly and Matplotlib')
        st.write('- Web scraping and data extraction with Beautiful Soup and Scrapy')
        st.write('- Automating tasks and workflows with Python scripting')


        



    with st.container():  # Excel
        col1, col2 = st.columns([1,12])
        with col1:
            st.image('https://github.com/IssacDavidi/data_project/blob/main/photos/excel.png?raw=true', width = 45)
        with col2:
            st.subheader('Excel')

        # Stars line
        col1, col2 = st.columns([1,8])
        with col1:
            st.write(':orange[Skill Level]')
        with col2:
            st.image('https://github.com/IssacDavidi/data_project/blob/main/photos/5stars.png?raw=true',  width = 150)


        st.write('- Creating pivot tables and charts for data analysis and visualization')
        st.write('- Manipulating and cleaning data using functions (VLOOKUP, IFS) and advanced filtering')
        st.write('- Automating repetitive tasks with macros and VBA scripting')
        st.write('- Applying conditional formatting and other formatting techniques for data presentation')




# Projects Section
elif selected_section == "📁Projects":
    st.header("Projects", divider = 'rainbow')
    with st.expander("Exploring the Bookshelf: An Insightful Analysis of Steimatzky's Book Catalog"):
        st.write("- **Project Description:** This project focuses on exploring and analyzing data from Steimatzky, a prominent book retailer. The analysis delves into various aspects, including book prices across different categories, popular authors, and other insightful metrics. Through data visualization and statistical techniques, the project aims to uncover valuable insights and patterns within Steimatzky's book catalog and sales data.")
        st.write('👉[To the project](https://sql-books-project.streamlit.app)')

    with st.expander("Dynamic Stock Performance Tracking Dashboard"):
        st.write("- **Project Description:** This interactive stock analysis dashboard provides in-depth insights into various financial metrics and indicators.")
        st.write("- It enables comprehensive exploration of stock data, including last traded price, beta value, 52-week range, year-to-date returns, dividend information, and more.")
        st.write("- Users can visualize stock price movements through interactive charting capabilities.")
        st.write("- The dashboard allows for seamless integration of technical indicators onto the charts.")
        st.write("- Additionally, the dashboard provides access to financial statements data in tabular format for further analysis.")
        st.write('👉[To the project](https://stock-analysis-interactive.streamlit.app)')




# Run the Streamlit app
if __name__ == "__main__":
    st.sidebar.subheader("Contact", divider = 'rainbow')
    col1, col2 = st.sidebar.columns([1,10])
    with col1:
        st.image('https://github.com/IssacDavidi/data_project/blob/main/photos/email.png?raw=true', width = 25)
    with col2:
        st.write('Davidi.Itzhak@gmail.com')


    col1, col2 = st.sidebar.columns([1,10])
    with col1:
        st.image('https://github.com/IssacDavidi/data_project/blob/main/photos/linkdin.png?raw=true', width = 25)
    with col2:
        st.write('[LinkedIn](https://www.linkedin.com/in/itzhakdavidi)')


    col1, col2 = st.sidebar.columns([1,10])
    with col1:
        st.image('https://github.com/IssacDavidi/data_project/blob/main/photos/github.png?raw=true', width = 25)
    with col2:
        st.write('[GitHub](https://github.com/IssacDavidi)')
