import pandas as pd


def create_features(cgm_df):
    df = cgm_df.copy()

    df["hour"] = df["DateTime"].dt.hour
    df["day_of_week"] = df["DateTime"].dt.dayofweek
    df["is_overnight"] = df["hour"].apply(lambda x: 1 if 0 <= x < 6 else 0)

    df["glucose"] = df["Sensor Glucose (mg/dL)"]

    df["high_glucose_risk"] = df["glucose"].apply(
        lambda x: 1 if x > 180 else 0
    )

    feature_df = df[
        [
            "glucose",
            "hour",
            "day_of_week",
            "is_overnight",
            "high_glucose_risk",
        ]
    ].dropna()

    return feature_df
