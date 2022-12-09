def mappingsss():
  import pandas as pd
  import warnings
  warnings.filterwarnings('ignore')

  data=pd.read_csv('Ganpati competition - Sheet1.csv')
  data.head()
  model=data.copy()

  data=data[['District','latitude']]

  data.dropna(inplace=True)

  data['Longitute']=data['latitude']

  def long(num):
    a=num.split(",")
    return a[1]

  def lati(num):
    a=num.split(",")
    return a[0]

  data['latitude']=data['latitude'].apply(lati)
  data['latitude']=data['latitude'].astype(float)
  data['Longitute']=data['Longitute'].apply(long)
  data['Longitute']=data['Longitute'].astype(float)

  from sklearn.preprocessing import LabelEncoder
  le=LabelEncoder()
  data['District']=le.fit_transform(data['District'])

  from sklearn.model_selection import train_test_split
  x=data.drop('District',axis=1)
  y=data['District']
  x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=2)

  from sklearn.metrics import classification_report
  from sklearn.neighbors import KNeighborsClassifier
  knn=KNeighborsClassifier(n_neighbors=5)
  knn.fit(x_train,y_train)
  y_pred=knn.predict(x_test)

  def nearbyy (a):
    b=knn.predict(a)
    d=le.inverse_transform(b)
    return d[0]

  url='http://ipinfo.io/json'
  import json
  import urllib.request as ur
  html = ur.urlopen(url).read()
  print(type(html))
  data = json.loads(html.decode('utf-8'))
  co=data['loc'].split(",")
  latitude=float(co[0])
  longitude=float(co[1])

  a=[[latitude, longitude]]
  location=nearbyy(a)
  z=model[model['District']==location]
  b=(z[["District","Locality",'Pandal Name']])
  a=b.values.tolist()
  return a