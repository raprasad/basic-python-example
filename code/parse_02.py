import sys
import pprint
from os.path import isfile, join, dirname, realpath
import pandas as pd

# path to the data directory "../data"
current_dir = dirname(realpath(__file__))
data_directory = join(dirname(current_dir), 'data')


def get_country_info(selected_country):
    
    if selected_country is None:
        return (False, 'Please select a country')
        
    # --------------------------
    # data file
    # --------------------------
    fname = join(data_directory, 'fearonlaitin.tab')

    # --------------------------
    # does file exist?
    # --------------------------
    if not isfile(fname):
        return (False, 'File not found: %s' % fname)
                
    # --------------------------
    # read file into data frame
    # --------------------------
    df = pd.read_csv(fname, sep='\t')

    # --------------------------
    # check for country
    # --------------------------
    country_names = pd.unique(df['country'])
    if not selected_country in country_names:
        return (False, 'Country not found: %s' % selected_country)
    
    # --------------------------
    # Filter out country stats, dropping out missing values
    # --------------------------
    df_country = df.loc[df['country'] == selected_country].dropna() 

    # --------------------------
    # Make lists of years and populations
    # --------------------------
    year_list = df_country['year'].tolist()
    pop_list = df_country['pop'].apply(int).tolist()
    
    # pairing information (example)
    year_pop_pairs = zip(year_list, pop_list)

    # --------------------------
    # Store values as a dict / hash
    # --------------------------
    data_dict = { 'selected_country' : selected_country,
        'year_list' : year_list, 
        'pop_list' : pop_list,
        'year_pop_pairs' : year_pop_pairs,
        'country_names' : country_names,
        }

    return (True, data_dict)
    
if __name__=='__main__':
    country_info_dict = get_country_info('USA')
    pprint.pprint(country_info_dict, indent=4)
    #print 
    