import data
import os

if __name__ == "__main__":
    _data_path = "../data/"
    csv_path = _data_path + "collegeinsight_data_nolabel_ICs_by_year.csv"

    if not os.path.exists(csv_path):
        print("Data not found, downloading...")
        data.download_data(path = _data_path)

    try:
        tuition_db, supplies_db, room_db = data.load_data(path = _data_path)
        print("Loaded Data Successfully!")
    except:
        db, colleges = data.get_data(path = csv_path)
        tuition_db, supplies_db, room_db = data.reformat_data(db, colleges)
        data.save_data(tuition_db, "tuition", path = _data_path)
        data.save_data(supplies_db, "supplies", path = _data_path)
        data.save_data(room_db, "room", path = _data_path)
