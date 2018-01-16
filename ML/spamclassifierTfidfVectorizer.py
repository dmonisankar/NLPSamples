import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer

df=pd.read_csv('smsspamcollection\SMSSpamCollection',sep='\t',names=['Status','Message'])

df.loc[df["Status"]=='ham',"Status",]=1
df.loc[df["Status"]=='spam',"Status",]=0

df_x=df["Message"]
df_y=df["Status"]

cv1 = TfidfVectorizer(min_df=1,stop_words='english')

x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.2, random_state=4)

x_traincv=cv1.fit_transform(x_train)
x_testcv=cv1.transform(x_test)

mnb = MultinomialNB()

y_train=y_train.astype('int')


mnb.fit(x_traincv,y_train)


predictions=mnb.predict(x_testcv)
a=np.array(y_test)

count=0
for i in range (len(predictions)):
    if predictions[i]==a[i]:
        count=count+1
		
accuracy = count/(len(predictions))

print(accuracy)




