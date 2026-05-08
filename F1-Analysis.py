import warnings
warnings.simplefilter('ignore', FutureWarning)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px

df=pd.read_csv("winners_f1_1950_2025_v2.csv")
team_counts = df['team'].value_counts()
year_grp=df.groupby(['year'])

team_grp=df.groupby(['team'])
ferrari=team_grp.get_group('Ferrari')
ferrari_grp_=ferrari.groupby(['year'])
ferrari_standing= ferrari_grp_['team'].count()

circiut = df['circuit'].value_counts()

monaco_circiut = df.groupby(['circuit'])
monaco= monaco_circiut.get_group('Circuit de Monaco')
bar= monaco['winner_name'].value_counts()
monaco_states = bar.head()
monaco_states = monaco_states.sort_values(ascending = True)

st.set_page_config(page_title="F1 Analysis",
                    page_icon="wp8757596.png",
                    layout="wide",
                    initial_sidebar_state = "expanded")




st.sidebar.image("wp8757596.png", use_container_width=True)
st.sidebar.title("F1 Analysis")
st.sidebar.markdown("This dashboard provides insights into the history of Formula 1, showcasing team performances, circuit popularity, and key statistics. Explore the data to discover trends and highlights from the world of F1 racing.")
page = st.sidebar.selectbox("Select a Page", ["Home", "Team Analysis", "Circuit Analysis", "Driver Analysis"])
if page == "Home":
    st.write("F1 Main Data Explorer", df)
elif page == "Team Analysis":
        st.title("Ferrari Performance Analysis")
        with st.expander("See Team Counts"):
                   best_year=year_grp.get_group(2004)
                   st.write("Team Counts:", team_counts)
        
        team_grp=best_year.groupby(['team'])
        ferrari=team_grp.get_group('Ferrari')
        st.write("Ferrari's performance in 2004:", ferrari)
        

        st.header("Ferrari's Wins Over Time")
        fig_ferrari = px.line(
              x =ferrari_standing.index,
              y=ferrari_standing.values,
             title='The Wins Of Ferrari of Hestori in F1',
             labels={'x': 'Years', 'y': 'Number of Wins'},
              #markers=True,
             color_discrete_sequence=['red']
              )
        st.plotly_chart(fig_ferrari)
        st.write("Ferrari's dominance in Formula 1 is evident from the graph, showcasing their consistent performance and numerous victories over the years.")
elif page == "Circuit Analysis":
        st.title("Circuit Analysis")
        st.write("Circuit Counts:", circiut.head())

elif page == "Driver Analysis":
                st.title("Driver Analysis")
                st.header("Top 5 Winners at Circuit de Monaco")
                fig_monaco = px.bar(monaco_states.head(5),
            x=monaco_states.head(5).index, 
            y=monaco_states.head(5).values,
            color=monaco_states.head(5).index,
            title=('Top 5 Winners at "Circuit de Monaco"'),
            labels={'x': 'Winner Names',
                    'y': 'Number of Wins'})
                st.plotly_chart(fig_monaco)
                st.write("The bar chart highlights the top 5 drivers who have achieved the most victories at the prestigious Circuit de Monaco, showcasing their dominance and success at this iconic venue in Formula 1 history.")
        








#plt.barh(monaco_states.index , monaco_states.values , color = 'firebrick')
#plt.title('The 5 kings of "Circuit de Monaco"')
#plt.xlabel('Numeber of win')
#plt.ylabel('Winners_Names')
#plt.grid(True)
#plt.style.use('seaborn-v0_8-darkgrid')
#st.pyplot(plt)






#ferrari_standing= ferrari_grp_.count()






col1, col2, col3 = st.columns(3)
with col1:
        st.metric("All-Time Ferrari Wins", ferrari_standing.sum())
with col2:
        st.metric("King of Monaco Wins", "Ayrton Senna")
with col3:
        st.metric("Most Successful Circuit", "Circuit de Monza", circiut.head(1).values[0])


#tab1 , tab2 = st.tabs(["Ferrari's Wins Over Time", "Top 5 Winners at Circuit de Monaco"])
#with tab1:
        #st.header("Ferrari's Wins Over Time")
        #fig_ferrari = px.line(
        #      x =ferrari_standing.index,
        #      y=ferrari_standing.values,
        #      title='The Wins Of Ferrari of Hestori in F1',
        #      labels={'x': 'Years', 'y': 'Number of Wins'},
        #      #markers=True,
        #      color_discrete_sequence=['red']
        #      )
        #st.plotly_chart(fig_ferrari)
        #st.write("Ferrari's dominance in Formula 1 is evident from the graph, showcasing their consistent performance and numerous victories over the years.")
#with tab2:
        #st.header("Top 5 Winners at Circuit de Monaco")
        #fig_monaco = px.bar(monaco_states.head(5),
        #    x=monaco_states.head(5).index, 
        #    y=monaco_states.head(5).values,
        #    color=monaco_states.head(5).index,
        #    title=('Top 5 Winners at "Circuit de Monaco"'),
        #    labels={'x': 'Winner Names',
        #            'y': 'Number of Wins'})
        #st.plotly_chart(fig_monaco)
        #st.write("The bar chart highlights the top 5 drivers who have achieved the most victories at the prestigious Circuit de Monaco, showcasing their dominance and success at this iconic venue in Formula 1 history.")



