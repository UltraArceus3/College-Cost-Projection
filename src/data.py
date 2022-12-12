# suppresses warnings
import warnings
warnings.simplefilter(action = 'ignore')

# Trys importing multi-processing pandas, if it fails, imports regular pandas
try: 
    import modin.pandas as pd
except ImportError:
    import pandas as pd


# Imports and cleans database, returns dataframe and a list of colleges
def get_data(path = "../data/collegeinsight_data_nolabel_ICs_by_year.csv") -> tuple(pd.DataFrame, list):
    db = read_csv(path, encoding = 'unicode_escape')


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


# Reformats data into three dataframes organized by college and year, one for tuition, one for books & supplies, and one for room & board
def reformat_data(db: pd.DataFrame, colleges: list) -> tuple(pd.DataFrame, pd.DataFrame, pd.DataFrame):
    yrs = sorted(list(set(db['data_yr_string'])))
    years = [int(x.split("-")[0]) for x in yrs]

    columns = ["name"] + years
    print(columns)

    tuition_db = pd.DataFrame(columns = columns)
    tuition_db['name'] = colleges

    supplies_db = tuition_db.copy()

    room_db = tuition_db.copy()


    for i in range(len(colleges)):
        tuition = [db[db['name'] == colleges[i]][db['data_yr_string'] == x]['coa_tuit_fees_d'].values[0] for x in yrs]
        supplies = [db[db['name'] == colleges[i]][db['data_yr_string'] == x]['coa_books_supp_d'].values[0] for x in yrs]
        room = [db[db['name'] == colleges[i]][db['data_yr_string'] == x]['coa_on_room_board_d'].values[0] for x in yrs]
        #print([college] + tuition)
        #row = pd.DataFrame([colleges[i]] + tuition, columns = columns)
        #print(row)
        
        for yr in years:
            tuition_db.loc[i, yr] = tuition[years.index(yr)]
            supplies_db.loc[i, yr] = supplies[years.index(yr)]
            room_db.loc[i, yr] = room[years.index(yr)]

        print(f"{i + 1} / {len(colleges)}", end = "\r")
    
    return (tuition_db, supplies_db, room_db)

# Saves dataframes to csv files
def save_data(df, name, path = "../data/", **kwargs):
    df.to_csv(path + name + ".csv", **kwargs)

# Loads dataframes from csv files
def load_data(name, path = "../data/", **kwargs):
    return read_csv(path + name + ".csv", **kwargs)
