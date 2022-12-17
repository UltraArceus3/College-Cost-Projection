import data
import os
import graph

if __name__ == "__main__":
    _data_path = "../data/"
    csv_path = _data_path + "collegeinsight_data_nolabel_ICs_by_year.csv"

    if not os.path.exists(csv_path):
        print("Data not found, downloading...")
        data.download_data(path = _data_path)

    try:
        tuition_db = data.load_data("tuition_db", path = _data_path)
        supplies_db = data.load_data("supplies_db", path = _data_path)
        room_db = data.load_data("room_db", path = _data_path)
        print("Loaded Data Successfully!")
    except:
        print("Data not found, processing...")
        db, colleges = data.get_data(path = csv_path)
        tuition_db, supplies_db, room_db = data.reformat_data(db, colleges)
        data.save_data(tuition_db, "tuition", path = _data_path)
        data.save_data(supplies_db, "supplies", path = _data_path)
        data.save_data(room_db, "room", path = _data_path)

    
    graph.plot_college_data("UNIVERSITY OF CONNECTICUT", tuition_db, supplies_db, room_db, [2000, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018])
