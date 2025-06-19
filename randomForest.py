import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
import pickle

# Load data
df = pd.read_csv('aktivitas_lms.csv')

# Pisahkan fitur dan label
X = df[['Akses_Kinestetik', 'Akses_Visual', 'Akses_Auditori',
        'Avg_Skor_Kinestetik', 'Avg_Skor_Visual', 'Avg_Skor_Auditori']]
y = df['Gaya_Belajar']

print(df['Gaya_Belajar'].value_counts())

# Bagi dataset (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Buat model Random Forest dan latih
model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
model.fit(X_train, y_train)

# Evaluasi
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Simpan model
with open('model_rf.pkl', 'wb') as f:
    pickle.dump(model, f)

# Contoh data siswa baru untuk prediksi
data_baru = {
    'Akses_Kinestetik': [10],
    'Akses_Visual': [8],
    'Akses_Auditori': [10],
    'Avg_Skor_Kinestetik': [85],
    'Avg_Skor_Visual': [85],
    'Avg_Skor_Auditori': [90]
}
df_baru = pd.DataFrame(data_baru)

# Prediksi gaya belajar siswa baru
prediksi = model.predict(df_baru)
print("Prediksi gaya belajar siswa baru:", prediksi[0])
ConfusionMatrixDisplay.from_estimator(model, X_test, y_test)
plt.title("Confusion Matrix Random Forest")
plt.show()
plt.figure(figsize=(20,10))
plot_tree(model.estimators_[0], 
          feature_names=X.columns, 
          class_names=model.classes_, 
          filled=True, 
          rounded=True)
plt.title("Visualisasi Salah Satu Pohon dari Random Forest")
plt.show()