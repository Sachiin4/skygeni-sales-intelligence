import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Load data
df = pd.read_csv("data/skygeni_sales_data.csv")

# Target
df["target"] = (df["outcome"] == "Won").astype(int)

# Features
features = [
    "industry",
    "region",
    "product_type",
    "lead_source",
    "deal_stage",
    "deal_amount",
    "sales_cycle_days"
]

X = df[features]
y = df["target"]

cat_cols = ["industry","region","product_type","lead_source","deal_stage"]
num_cols = ["deal_amount","sales_cycle_days"]

# Preprocess
preprocess = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols)
], remainder="passthrough")

# Model
model = Pipeline([
    ("prep", preprocess),
    ("clf", LogisticRegression(max_iter=1000))
])

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train
model.fit(X_train, y_train)

# Evaluate
preds = model.predict(X_test)

print("\n=== MODEL PERFORMANCE ===")
print("Accuracy:", model.score(X_test, y_test))
print("\nClassification Report:\n")
print(classification_report(y_test, preds))

# Get feature names after encoding
ohe = model.named_steps["prep"].named_transformers_["cat"]
encoded_features = list(ohe.get_feature_names_out(cat_cols))

all_features = encoded_features + num_cols

# Get coefficients
coefficients = model.named_steps["clf"].coef_[0]

feature_importance = pd.DataFrame({
    "feature": all_features,
    "coefficient": coefficients
})

feature_importance = feature_importance.sort_values("coefficient", ascending=False)

print("\n=== TOP WIN DRIVERS ===")
print(feature_importance.head(10))

print("\n=== TOP LOSS DRIVERS ===")
print(feature_importance.tail(10))

# Predict win probability for all deals

probs = model.predict_proba(X)[:,1]

df_results = df.copy()
df_results["win_probability"] = probs

df_results.to_csv("outputs/deal_win_probabilities.csv", index=False)

print("\nSaved: outputs/deal_win_probabilities.csv")
print("\nScored deals saved for sales intelligence usage.")