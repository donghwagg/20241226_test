import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 타이틀 적용 예시
st.title('오늘은 스트림릿이라는걸 배워봤습니다.')

# 특수 이모티콘 삽입 예시
# emoji: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
st.title('안녕하세요 저는 :green[강빵빵이] 입니다. :sunglasses:')

# Header 적용
st.header('저는 조주O씨를 좋아합니다 :woman-heart-man:')

# Subheader 적용
st.subheader('너무너무 신기하네요!! 열심히 공부해 볼게요!')


st.title('데이터프레임도 넣을수 있고')

# DataFrame 생성
dataframe = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
})

st.dataframe(dataframe, use_container_width=False)


st.title('차트도넣을수 있네요~')


labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 35, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]
men_std = [2, 3, 4, 1, 2]
women_std = [3, 5, 2, 3, 3]
width = 0.35       # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()

ax.bar(labels, men_means, width, yerr=men_std, label='Men')
ax.bar(labels, women_means, width, yerr=women_std, bottom=men_means,
       label='Women')

ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.legend()

st.pyplot(fig)