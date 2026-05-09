import pandas as pd


def load_data(cgm_path, insulin_path):
    cgm_df = pd.read_csv(cgm_path)
    insulin_df = pd.read_csv(insulin_path)

    return cgm_df, insulin_df


def clean_cgm_data(cgm_df):
    cgm_df = cgm_df[['Date', 'Time', 'Sensor Glucose (mg/dL)']].dropna()

    cgm_df["DateTime"] = pd.to_datetime(
        cgm_df["Date"] + " " + cgm_df["Time"],
        format='%m/%d/%Y %H:%M:%S'
    )

    cgm_df.sort_values("DateTime", inplace=True)

    return cgm_df


def extract_auto_mode(insulin_df):
    auto_mode = insulin_df[
        insulin_df['Alarm'] == "AUTO MODE ACTIVE PLGM OFF"
    ][['Date', 'Time']]

    auto_mode["DateTime"] = pd.to_datetime(
        auto_mode["Date"] + " " + auto_mode["Time"],
        format='%m/%d/%Y %H:%M:%S'
    )

    return auto_mode


def split_auto_manual_modes(cgm_df, auto_mode_df):
    auto_start = auto_mode_df['DateTime'].iloc[0]

    auto_df = cgm_df[cgm_df['DateTime'] >= auto_start]
    manual_df = cgm_df[cgm_df['DateTime'] < auto_start]

    return auto_df, manual_df
