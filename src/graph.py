import matplotlib.pyplot as plt
from model import PolyRegModel



_GRAPH_COLORS = {
    "TUITION": "red",
    "ROOM": "blue",
    "SUPPLIES": "green"
}

def plot_data(college, db, years, **kwargs):

    plt.plot([str(x) for x in years], list(db[db["name"] == college].iloc[0, 1:])[1:], marker = "o", **kwargs)


def plot_prediction(db, predict, college, years, predict_years, **kwargs):

    predict.train(years, list(db[db["name"] == college].iloc[0, 1:])[1:])
    plt.plot([str(x) for x in years + predict_years], predict.predict(years + predict_years), marker = "o", linestyle = "--", **kwargs)



def plot_college_data(college, tuition_db, supplies_db, room_db, years, **kwargs):

    predict_years = [2019, 2020, 2021, 2022, 2023, 2024, 2025]
    predict = PolyRegModel(4)

    plt.figure(figsize=(10, 5))


    plot_prediction(tuition_db, predict, college, years, predict_years, label = "Tuition Prediction", color = "orange", **kwargs)
    plot_data(college, tuition_db, years, label = "Tuition", color = "red", **kwargs)

    plot_prediction(room_db, predict, college, years, predict_years, label = "Room & Board Prediction", color = "cyan",  **kwargs)
    plot_data(college, room_db, years, label = "Room & Board", color = "blue", **kwargs)

    plot_prediction(supplies_db, predict, college, years, predict_years, label = "Supplies Prediction", color = "lime", **kwargs)
    plot_data(college, supplies_db, years, label = "Supplies", color = "green", **kwargs)

    plt.axvline(str(years[-1]), color = "black", linestyle = "--", label = "Last Year of Data")

    plt.title(college)
    plt.legend()
    plt.grid()
    plt.show()


