import sys
from os.path import isfile, join, dirname, realpath
import pandas as pd

# path to the data directory "../data"
current_dir = dirname(realpath(__file__))
data_directory = join(dirname(current_dir), 'data')

# data file
fname = join(data_directory, 'fearonlaitin.tab')

# does file exist?
if not isfile(fname):
    print 'file not found: %s' % fname
    sys.exit(0)
    
# read file into data frame
df = pd.read_csv(fname, sep='\t')
print df['year']

# show columns
print df.columns
print df.values

# show types
print df.types

# show head/tail
print df.head(10)
print df.tail(10)

# drop missing vals
df.dropna()

# fill missing vals
df.fillna(-1)

df.loc[df['country'] == 'USA']

us_pop = df.loc[df['country'] == 'USA'][[1,2]]
us_pop['year'].tolist()
us_pop['pop'].tolist()

df.loc[df['country'].isin(['USA', 'FIJI'])][[0,1,2]]