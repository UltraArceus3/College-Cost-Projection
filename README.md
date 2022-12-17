# College-Cost-Projection

A simple polynomial regression model to predict the cost of tuition, room/boarding, and supplies of colleges over time.

Run ```src/main.py``` to show the projection of a randomly-selected college.

After cleaning and filtering of the dataset using pandas, there are 1,453 college entries that are available. Cleaning is based on the availability of certain data, such as tuition, at all available time points (2000, 2003 - 2018).

The ML model is trained on the spot with the data of the selected college. The model utilizes the scikit-learn library's polynomial regression capabilities to fit a 4th degree polynomial on the college's data points. 

The data is visualized using the matplotlib library. The college's actual data is shown as a solid line, while the projected data is shown as a dashed line. College data is available for 2000 and 2003 - 2018, while the data is projected from 2019 - 2025.


The dataset used is from https://college-insight.org, which has the following license:
```
 The Institute for College Access & Success. College Insight, https://college-insight.org. 
 Student debt and undergraduate financial aid data are licensed from Peterson's Undergraduate Financial Aid and Undergraduate Databases, ©️ 2020 Peterson's LLC, all rights reserved. 
 All data may be reproduced, with attribution, subject to restrictions under this Creative Commons license: https://creativecommons.org/licenses/by-nc-nd/3.0/.
```
