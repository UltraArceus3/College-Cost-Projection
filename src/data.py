# suppresses warnings
import warnings
warnings.simplefilter(action = 'ignore')

import pandas as pd

# Downloads data from college-insight.org
def download_data(page = "https://college-insight.org/wp-content/uploads/2020/10/CIS-Data-and-Codebook-20-10-06.zip", path = "../data/"):
    import requests
    import zipfile
    import io

    r = requests.get(page)

    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(path)

# Imports and cleans database, returns dataframe and a list of colleges
def get_data(path = "../data/collegeinsight_data_nolabel_ICs_by_year.csv"):
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


# Reformats data into three dataframes organized by college and year, one for tuition, one for books & supplies, and one for room & board
def reformat_data(db: pd.DataFrame, colleges: list):
    yrs = sorted(list(set(db['data_yr_string'])))
    years = [int(x.split("-")[0]) for x in yrs]

    columns = ["name"] + years
    print(columns)

    tuition_db = pd.DataFrame(columns = columns)
    tuition_db['name'] = colleges

    supplies_db = tuition_db.copy()

    room_db = tuition_db.copy()


    for i in range(len(colleges)):
        c_db = db[db['name'] == colleges[i]]
        
        tuition = [c_db[c_db['data_yr_string'] == x]['coa_tuit_fees_d'].values[0] for x in yrs]
        supplies = [c_db[c_db['data_yr_string'] == x]['coa_books_supp_d'].values[0] for x in yrs]
        room = [c_db[c_db['data_yr_string'] == x]['coa_on_room_board_d'].values[0] for x in yrs]
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
    return pd.read_csv(path + name + ".csv", **kwargs)
