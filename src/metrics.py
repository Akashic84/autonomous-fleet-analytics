import pandas as pd

def fleet_summary(df):

    total_distance = df["distance_km"].sum()

    total_trips = len(df)

    disengagements = df["disengagements"].sum()

    disengagement_rate = (
        disengagements / total_distance * 1000
    )

    return {
        "total_distance": round(total_distance, 2),
        "total_trips": total_trips,
        "disengagements": disengagements,
        "disengagement_rate": round(
            disengagement_rate,
            2
        )
    }