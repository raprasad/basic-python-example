from os.path import isfile
import pandas as pd


# data file
fname = '../data/fearonlaitin.tab'

# does file exist?
if not isfile(fname):
    print 'file not found: %s' % fname
    sys.exit(0)
    
# read file into data frame
df = pd.read_csv(fname, sep='\t')


# show columns
df.columns
df.dtypes
df.values

df.describe()


# show head/tail
df.head(10)
df.tail(10)

# ---------------------
# List of countries
# ---------------------
df['country']   # alternate: df['country']
pd.unique(df.country)   
countries = pd.unique(df.country)
countries.sort()
for c in countries:
    print c


df['year']
df.loc[df['year'] == 1983]

# drop missing vals
df.dropna()

# fill missing vals
df.fillna(-1)

# USA data
df_usa = df.loc[df['country'] == 'USA']

# Year and population
df_usa[['year', 'pop']]

# year to list
df_usa['year'].tolist()

# population to list
df_usa['pop'].tolist()

# list of tuples
zip(df_usa['year'], df_usa['pop'])

df.loc[df['country'].isin(['USA', 'FIJI'])][[0,1,2]]