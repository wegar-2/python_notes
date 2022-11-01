from utils.package_data_loaders import df_load_strokes_medical_data
from sklearn.preprocessing import LabelEncoder

# load the data set
df = df_load_strokes_medical_data()

# have a look at the types
# print(df.dtypes)

# consider variable: work_type
df["work_type"].unique()

# encode the variable work_type
lenc = LabelEncoder()
lenc.fit(df["work_type"])
df["work_type"] = lenc.transform(df["work_type"])
# inverse tranformation: lenc.inverse_transform(df["work_type"])
print(df.dtypes)
