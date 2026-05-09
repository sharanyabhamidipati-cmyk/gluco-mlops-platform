import os
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from preprocess import load_data, clean_cgm_data, extract_auto_mode, split_auto_manual_modes
from features import create_features


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CGM_PATH = os.path.join(BASE_DIR, "data", "CGMData.csv")
INSULIN_PATH = os.path.join(BASE_DIR, "data", "InsulinData.csv")
MODEL_DIR = os.path.join(BASE_DIR, "model")
MODEL_PATH = os.path.join(MODEL_DIR, "glucose_risk_model.pkl")

os.makedirs(MODEL_DIR, exist_ok=True)


def train_model():
    cgm_df, insulin_df = load_data(CGM_PATH, INSULIN_PATH)

    clean_cgm_df = clean_cgm_data(cgm_df)
    auto_mode_df = extract_auto_mode(insulin_df)

    auto_df, manual_df = split_auto_manual_modes(clean_cgm_df, auto_mode_df)

    feature_df = create_features(auto_df)

    X = feature_df[["glucose", "hour", "day_of_week", "is_overnight"]]
    y = feature_df["high_glucose_risk"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    joblib.dump(model, MODEL_PATH)

    print("Model trained successfully")
    print(f"Accuracy: {accuracy}")
    print(f"Training rows: {len(X_train)}")
    print(f"Test rows: {len(X_test)}")
    print(f"Model saved at: {MODEL_PATH}")


if __name__ == "__main__":
    train_model()
