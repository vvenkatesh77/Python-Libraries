'''
import pandas as pd

#a=["kumar","sam","ravi","ramu"]#series list without columns
#a={"name":["ravi","ramu","sameer","teja"]}
a={"name":["ravi","ramu","sai","teja"],
   "age":[12,23,34,45]}
data=pd.DataFrame(a)
print(type(data))
print(data)
'''
#reading csv fil
'''
import pandas as pd

#df = pd.read_csv('data/crops.csv')
#df = pd.read_csv('data/student-mat.csv',delimiter=":")
#df = pd.read_csv('data/iris.data')
df = pd.read_csv('https://raw.githubusercontent.com/srinathkr07/IPL-Data-Analysis/master/matches.csv')
print(df)
'''
# reading xl files
'''
import pandas as pd
df = pd.read_excel('data/sampleexcel.xlsx')
print(df)


'''
'''
import pandas as pd
#df = pd.read_csv('data/crops.csv')
#print(df)
#pd.set_option('display.max_rows',None)
#pd.set_option('display.max_columns',None)
#print(df)



#print(df.head())
#print(df.head(11))
#print(df.head(7))
#print(df.tail(9))
#print(df['crop'])
#print(df['crop','area','msp'].head())#gives three coulmns

    #pandas attributes
#print(df.dtypes)
#print(df['area'].dtypes)
#print(df.columns)
#print(df.axes)
#print(df.ndim)  #num of dimensions
#print(df.size)  #total tuples in the files i.e 100*5=500
#print(df.shape)
#print(df.values)


# pandas methods

#print(df.describe()) #gives the description of the crop data
#print(df.max())
#print(df['area'].max())
#print(df.mean())
#print(df['area'].mean())
#print(df.std())


#print(df['area'].unique())
#print(df['crop'].unique())

#print(df['crop'].value_counts())
#print(df['area'].value_counts())

#print(df.sample(n=25))
#print(df.loc[5:15])
#print(df.loc[5:15,['crop','year','area']])
#print(df.loc[72:,['crop','year','area']])


#print(df.iloc[10:20,[1,3]])
#print(df.iloc[10:20,1:3])

#print(df.iloc[10:20])
#print(df.iloc[ :20])

'''
'''
#find mean departure dealays for everyy origin
import pandas as pd
df = pd.read_csv('data/flightdata.csv')
print(df.head())
#pd.set_option('display.max_rows',None)
#pd.set_option('display.max_columns',None)
#print(df.head())

#print(df.groupby(['ORIGIN'])['DEP_DELAY'].max())
#print(df.groupby(['ORIGIN'],sort=False)['DEP_DELAY'].max())
#to fetch the one origin details
dt = df.groupby(['ORIGIN'])['DEP_DELAY'].mean()
print("dep_delay from ATL:",dt['ATL'])
'''
#### 1-06-2022

#import pandas as pd
#df=pd.read_csv('data/movie_metadata.csv')
#print(df)

#data filtering
#dt=df[df['duratuion']>170]  #row filtering
#print(dt)
#print(dt[['director_name','movie_title','duration']])

#print([(df.duration>160)&(df.num_critic_for_reviews<100)*(dfd.country=="USA")])
#dt=df[(df.duration>=160)&(df.duration<200)]
#print(dt[['director_name','movie_title','duaration']])

########
#print(df.isnull())
#print(df.isnull().sum())
#print(df.notnull())


#country
'''
#print(df['country'].head())
#print("NAN values before FillNA :",df['country'].isnull().sum())
#df['country'].fillna(df['country'].mode()[0],inplace=True)
#df.country=df.country.fillna(df.country.mode()[0])
#df.country=df.country.fillna('INDIA')
#print(df['country'].head())
#print("NAN values After FillNA :",df['country'].isnull().sum())

#duration

#print("NAN values before FillNA :",df['duration'].isnull().sum())
#print("Mean of duration :",round(df.duration.mean()))
#df['duration'].fillna(round(df['duration'].mean()),inplace=True)
#df.duration=df.duration.fillna(round(df.duration.mean()))
#print("NAN values After FillNA :",df['duration'].isnull().sum())
#print(df['duration'].head(15))
'''
#02-06-2022
'''
import pandas as pd
df=pd.read_excel('data/stddata.xlsx')

#print(df)
 
'''
'''
print("Before using Fillna:",df.isnull().sum())

df.m1.fillna(df.m1.mean(),inplace=True)
df.m2.fillna(df.m2.mean(),inplace=True)
df.m3.fillna(df.m3.mean(),inplace=True)      
df.m4.fillna(df.m4.mean(),inplace=True)

print("After using Fillna:",df.isnull().sum())
print(df)
'''
'''
 
'''
'''
#print("Before Dropna() function :\n",df.head(14))#actual data
#dt=df.dropna()
#print("After Dropna() function :\n",dt.head(14))

#print(df.head(14))
#print("Dropna() function with How=all:\n",df.dropna(how='all'))

#prin(df.head())
#print(df.dropna(thresh=6))

#print(df.dropna(subset=['m3']))
#print(df.dropna(subset=['m3','m4']))
      
#print(df.head(14))
#print(df.dropna(axis=1,how='all'))
#print(df.dropna(axis=1))
#print(df.dropna(axis=1,thresh=8))
 '''
'''
#03-06-2022

#import pandas as pd
#df=pd.read_csv('data/movie_metadata.csv')

#dt=df['director_name'].str.upper()#converts letters into upper case
#print(df.head(10))
#print(df['movie_title'].str.strip()) #remove white spaces
#print(df.head())
#dfnew=df.rename(columns={'director_name':'director','movie_facebook_likes':'facebook_likes'})
#print(dfnew.head())
#dfnew.to_csv('newfileapr2.csv') #saving edited file in apr2
'''
'''
import pandas as pd

b=[ [1,2,3,4,5,6,7,8,9],
    [2,3,4,5,7,6,8,9,1],
    [4,5,6,7,8,9,3,2,1],
    [9,8,7,6,5,4,3,2,1] ]
data1=pd.DataFrame(b)
#print(data1)
#print(data1.iloc[0:3,3:7])
#print(data1.iloc[2:4,5:8])
#print(data1.iloc[2:4,4:9])
'''
###data sorting###
'''
import pandas as pd
df=pd.read_csv('data/movie_metadata.csv')

#print(df['duration'].head(10))
#dt=df.sort_values(by='duration')
#print(dt)
#print(dt.duration.head(10))


DA=df.sort_values(by='duration',ascending=False)
print(DA.duration.head(10))

'''

#cleaning data
#COLLEGE ADMISSION
'''
import pandas as pd
df=pd.read_csv('undata/Admission_Prediction.csv')
#print(df.head())

print(df.isna().sum())
#there are some missing values
#df['GRE Score'].fillna(round(df['GRE Score'].mean()),inplace=True)
#df['TOEFL Score'].fillna(round(df['TOEFL Score'].mean()),inplace=True)
#df['University Rating'].fillna(df['University Rating'].mode()[0],inplace=True)                              
#print(df.isna().sum())

#df.to_csv("admin_cleandataapr2.csv")
'''
#BOSTON
'''
import pandas as pd
df=pd.read_excel('undata/boston.xlsx')
#print(df)

#print(df.isnull().sum())
df['crim'].fillna((df['crim'].mean()),inplace=True)
df['zn'].fillna(df['zn'].mode()[0],inplace=True)
df['chas'].fillna(df['chas'].mode()[0],inplace=True)
df['nox'].fillna(round(df['nox'].mean()),inplace=True)
df['rm'].fillna(round(df['rm'].mean()),inplace=True)
df['age'].fillna(round(df['age'].mean()),inplace=True)
df['dis'].fillna(round(df['dis'].mean()),inplace=True)
df['rad'].fillna(df['rad'].mode()[0],inplace=True)
df['tax'].fillna(round(df['tax'].mean()),inplace=True)
df['ptratio'].fillna(round(df['ptratio'].mean()),inplace=True)
df['black'].fillna(round(df['black'].mean()),inplace=True)
df['lstat'].fillna(round(df['lstat'].mean()),inplace=True)
df['medv'].fillna(round(df['medv'].mean()),inplace=True)
print(df.isnull().sum())

df.to_csv("admin_cleanedbostondata.csv")
'''
''' 
import pandas as pd
df=pd.read_csv('undata/petfinder-mini.csv')
#print(df)
#print(df.isnull().sum())
df['Age'].fillna(round(df['Age'].mean()),inplace=True)
df['Fee'].fillna(df['Fee'].mode()[0],inplace=True)
df['PhotoAmt'].fillna(round(df['PhotoAmt'].mean()),inplace=True)
df['AdoptionSpeed'].fillna(df['AdoptionSpeed'].mode()[0],inplace=True)
#print(df.dropna(subset=['Type']))
print(df.dropna(axis=1)) 
#df.to_csv("admin_cleanedpetfinderdata.csv")
print(df.isnull().sum())
''' 
 



























