import pandas as pd
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Загрузка данных
data = pd.read_csv('data.csv')

# Разделение данных на обучающую и тестовую выборки
X = data[['brand', 'model', 'screen_size', 'color', 'hard_disk', 'CPU', 'RAM', 'operating_system', 'special_features', 'graphics_card', 'graphics_coprocessor', 'CPU_rating', 'rating']]
y = data['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создание модели кластера
model = KMeans(n_clusters=10)

# Обучение модели на обучающей выборке
model.fit(X_train, y_train)

# Предсказание цены ноутбука на тестовой выборке
predictions = model.predict(X_test)
mean_squared_error = mean_squared_error(y_test, predictions)
print("Mean Squared Error:", mean_squared_error)
