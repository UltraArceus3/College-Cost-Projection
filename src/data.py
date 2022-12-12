import pandas as pd

# Imports and cleans database, returns dataframe and a list of colleges
def get_data(path = "../data/collegeinsight_data_nolabel_ICs_by_year.csv") -> tuple(pd.DataFrame, list):
    db = pd.read_csv(path, encoding = 'unicode_escape')


    pred_data = ['coa_tuit_fees_d', 'coa_books_supp_d', 'coa_on_room_board_d']

    db['name'] = db['name'].str.upper() # make all names uppercase

    db = db[['name', 'data_yr_string'] + pred_data] # select only the columns we need

    for dat in pred_data:
        db = db[db[dat].notnull()] # remove rows with null values


    yrs = sorted(list(set(db['data_yr_string'])))

    colleges = list(db[db['data_yr_string'] == yrs[0]]['name'])

    for yr in yrs[1:]:
        col = list(db[db['data_yr_string'] == yr]['name'])

        colleges = [x for x in colleges if x in col]

    print(len(colleges))

    db = db[[x in colleges for x in db['name']]]

    return db, colleges

