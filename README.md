# Stagewise-Regression-Demo
A demo of forward stagewise regression.

Introduction
---
This is a basic demo of forward stagewise regression. The model is used to predict the call time of two people, who are using HOLLA app to chat with each other.

Dataset
---
The dataset are generated randomly by the [gen_data.py](https://github.com/Suyi32/Stagewise-Regression-Demo/blob/master/Data%20Generation/gen_data.py)

1. raw_data_diff_gender.csv: This dataset is used to predict the call time of a user when he or she is going to chat with a person of different gender.

2. raw_data_same_gender.csv: This dataset is used to predict the call time of a user when he or she is going to chat with a person of same gender.

The first 7 columns in each dataset are features selected to make prediction. These features are selected according to the [a paper](https://github.com/Suyi32/Stagewise-Regression-Demo/blob/master/Reference%20Paper/duration.pdf) and the experience. The last column is the actual call time generate by human.

The selected features are: call_time_same_sex, call_time_diff_sex, quality_internet, time, if_new_friend, Credit, age_diff, language_fluence.

Description:
1. call_time_same_sex: Average time of the call time when a user chats with person of the same sex, described by number of minutes.
2. call_time_diff_sex: Average time of the call time when a user chats with person of the different sex, described by number of minutes.
3. quality_internet  : The quality of the Internet when a user begin chating, described by a score.
4. time: This feature reflects if it is a comfortable time period for the user to chat, described by a score.
5. if_new_friend: This feature reflects if a user begin chatting with a new friend, described by 0 or 1.
6. Credit: This feature reflects the credit condition of a user, decribed by a score.
7. age_diff: This feature reflects the age difference of the two users, decribed by number of years.
8. language_fluence: This feature reflects the languge knowledge of a user, that is, if he or she can communicate well in the current language, decribed by scores.

Running Environment
---
Python 2.7 with numpy 

How to use
---
Download and store the prediction_model.py and datasets in the same directory. And run the prediction_model.py. Then you will get the results.



