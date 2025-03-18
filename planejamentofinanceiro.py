import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Exemplo de dados históricos de 2024 (substitua pelo seu próprio dataset)
data = {
    'mes': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'vendas': [100000, 120000, 130000, 125000, 140000, 150000, 155000, 160000, 170000, 180000, 190000, 200000],
    'custos': [50000, 55000, 60000, 58000, 62000, 64000, 65000, 66000, 67000, 69000, 70000, 71000],
    'investimentos': [10000, 12000, 13000, 12500, 14000, 15000, 15500, 16000, 17000, 18000, 19000, 20000],
}

# Criando o DataFrame
df = pd.DataFrame(data)

# Definindo variáveis de entrada (features) e saída (target)
# Agora, estamos prevendo os custos para o ano seguinte (2025)
X = df[['vendas', 'investimentos']]  # Variáveis independentes
y = df['custos']  # Variável dependente

# Dividindo os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializando o modelo RandomForestRegressor
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Treinando o modelo
model.fit(X_train, y_train)

# Fazendo previsões com o conjunto de teste
y_pred = model.predict(X_test)

# Calculando o erro absoluto médio (MAE)
mae = mean_absolute_error(y_test, y_pred)
print(f"Erro absoluto médio (MAE): {mae:.2f}")

# Agora, podemos usar o modelo treinado para prever os custos de 2025
# Suponha que as vendas e investimentos para 2025 sejam conhecidos
vendas_2025 = 210000
investimentos_2025 = 22000

# Prevendo os custos de 2025
custos_2025 = model.predict([[vendas_2025, investimentos_2025]])
print(f"Projeção de custos para 2025: {custos_2025[0]:.2f}")
