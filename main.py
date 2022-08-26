import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

data = pd.read_csv("https://raw.githubusercontent.com/anastang/BillionaireAnalysis/main/Billionaire.csv?token=GHSAT0AAAAAABYAGLZXAP4Z5HN26BOVDM7MYYIHZBA")
#print(data.head())

# check for missing values
#print(data.isnull().sum())

# remove expendable data
data = data.dropna()

#print(data.isnull().sum())
data['NetWorth'] = data['NetWorth'].str.strip('$')
data['NetWorth'] = data['NetWorth'].str.strip('B')
data['NetWorth'] = data['NetWorth'].astype(float)


# --------- FIGURE 1 --------- #

filteredData = data.sort_values(by = ["NetWorth"], ascending=False).head(10)
plt.figure(figsize = (20,10))
sb.histplot(x = "Name", hue = "NetWorth", data = filteredData)
plt.rc('font', size=12)
plt.title("Top 10 Billionaires by Net Worth")



# --------- FIGURE 2 --------- #

filteredData2 = data["Source"].value_counts().head(10)
index = filteredData2.index
sources = filteredData2.values
colors2 = ["red", "blue", 'green', "orchid", "maroon", "orange", "yellow", "brown", "black", "cyan"]
plt.figure(figsize = (15,15))
plt.pie(sources, labels = index, colors = colors2)
centreCircle = plt.Circle((0,0), 0.5, color = 'white')
figure2 = plt.gcf()
figure2.gca().add_artist(centreCircle)
plt.rc('font', size=12)
plt.title("Top 10 Domains Among Billionaires", fontsize = 18)



# --------- FIGURE 3 --------- #

filteredData3 = data["Industry"].value_counts().head(10)
index = filteredData3.index
sources = filteredData3.values
colors3 = ["orangered", "skyblue", 'palegreen', "firebrick", "teal", "royalblue", "mediumpurple", "violet", "deeppink", "mediumseagreen"]
plt.figure(figsize = (15,15))
plt.pie(sources, labels = index, colors = colors3)
centreCircle = plt.Circle((0,0), 0.5, color = 'white')
figure2 = plt.gcf()
figure2.gca().add_artist(centreCircle)
plt.rc('font', size=12)
plt.title("Top 10 Industries Among Billionaires", fontsize = 18)



# --------- FIGURE 4 --------- #

filteredData4 = data["Country"].value_counts().head()
index = filteredData4.index
sources = filteredData4.values
colors4 = ["red", "forestgreen", 'dodgerblue', "blueviolet", "magenta"]
plt.figure(figsize = (15,15))
plt.pie(sources, labels = index, colors = colors4)
centreCircle = plt.Circle((0,0), 0.5, color = 'white')
figure2 = plt.gcf()
figure2.gca().add_artist(centreCircle)
plt.rc('font', size=12)
plt.title("Top 5 Countries with Most Billionaires", fontsize = 18)



plt.show()