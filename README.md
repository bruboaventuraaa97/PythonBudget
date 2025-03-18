# PythonBudget
# Planejamento de Custos com Machine Learning

Este repositório contém um exemplo de como usar aprendizado de máquina para planejar os custos de 2025 com base nos dados históricos de 2024. Utilizamos bibliotecas poderosas como **Pandas**, **Numpy** e **Scikit-learn** para construir um modelo de previsão de custos usando **RandomForestRegressor**.

##Execute o script Python planejamento_custos.py:

## Como Executar o Código

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/bruboaventuraaa97/PythonBudget/
2. Navegue até a pasta do projeto:

cd PythonBudget

Instale as dependências: Para instalar as bibliotecas necessárias, execute o seguinte comando:

pip install pandas numpy scikit-learn

4. Execute o script Python: Após instalar as dependências, execute o script Python planejamento_custos.py:

   python planejamento_custos.py
   
5. Substitua os dados de exemplo: No arquivo planejamento_custos.py, substitua os dados de exemplo pelos seus próprios dados financeiros históricos.

6. Certifique-se de que os dados contenham informações de vendas, custos e investimentos para cada mês.
Execute novamente o script para treinar o modelo e prever os custos de 2025 com os dados atualizados.



## Explicação

### 1. Leitura e Preparação de Dados
O código começa criando um DataFrame com os dados históricos de **vendas**, **custos** e **investimentos** para o ano de 2024. Você pode substituir esses dados por seu próprio conjunto de dados. Os dados devem conter colunas de **vendas**, **custos** e **investimentos** para cada mês.

### 2. Definição de Variáveis
As **variáveis independentes** (features) usadas para prever a **variável dependente** (custos) são **vendas** e **investimentos**. Essas variáveis ajudam o modelo a aprender como os **custos** estão relacionados com as **vendas** e **investimentos**.

### 3. Divisão de Dados
A divisão entre dados de **treinamento** e **teste** é feita com a função `train_test_split`, permitindo que o modelo seja treinado em um subconjunto dos dados e testado em outro subconjunto de forma independente. Isso ajuda a garantir que o modelo não esteja **overfitting** (ajustando-se demais aos dados de treinamento).

### 4. Modelo RandomForestRegressor
Usamos o modelo **RandomForestRegressor** para prever os **custos**. O modelo é treinado com o conjunto de dados de **treinamento** e depois testado com o conjunto de **teste**. O modelo utiliza múltiplas árvores de decisão para prever os custos com base nas variáveis **vendas** e **investimentos**.

### 5. Avaliação do Modelo
O erro do modelo é avaliado utilizando a métrica **Erro Absoluto Médio (MAE)**. O MAE nos dá uma ideia de quão precisas são as previsões de custos feitas pelo modelo, calculando a média da diferença entre as previsões e os valores reais dos custos.

### 6. Previsão para 2025
Depois de treinar o modelo, você pode usá-lo para prever os **custos de 2025** com base nos **custos anteriores** e nos **investimentos e vendas estimados** para o próximo ano.

## Benefícios

- **Projeções de custos mais precisas**: Usando aprendizado de máquina, você pode prever os **custos** de 2025 com base nos dados históricos de 2024, criando um planejamento financeiro mais robusto.
- **Planejamento financeiro mais assertivo**: Com previsões mais realistas de custos, o processo de **budgeting** e **forecasting** para o próximo ano se torna mais preciso e fundamentado, minimizando erros e otimizando a alocação de recursos financeiros.




### Como usar:

1. **Leitura e Preparação de Dados**: Inicialmente, você carrega os dados históricos de vendas, custos e investimentos em um DataFrame com o Pandas.
2. **Definição de Variáveis**: Em seguida, define-se as variáveis independentes (vendas e investimentos) para prever a variável dependente (custos).
3. **Divisão de Dados**: Usa-se a função `train_test_split` para separar os dados em conjuntos de treino e teste.
4. **Modelo de Regressão**: O modelo **RandomForestRegressor** é treinado e testado com esses dados.
5. **Avaliação do Modelo**: O erro de previsão é calculado com a métrica **MAE**, e você pode usar o modelo para prever os custos para 2025.

Isso fornece uma visão clara e organizada para o uso do código e como ele pode beneficiar o planejamento financeiro.
