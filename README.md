# Telco Customer Churn Prediction

Projeto de grupo da cadeira **Big Data Bootcamp** — Pós-Graduação em Enterprise Data Science & Analytics.
Grupo **EDSB25_20**
Membros: 
-     Diana Gomes nº mec: 20240829
-     Sara Góis nº mec: 20242129
-     Sérgio Patinha nº mec: 20241149
-     Tiago Franco nº mec: 20242038


## Objetivo
Prever o churn (cancelamento) de clientes de uma empresa de telecomunicações, identificando os principais fatores que influenciam a saída e propondo estratégias de retenção.

## Estrutura
- `data/` — dados brutos e processados  
- `notebooks/` — notebooks de análise e modelagem  

      - 00_data_loading.ipynb | Raw data access
      Import libraries, define paths, load raw files, quick data sanity check (shapes, missing files).

      - 01_data_cleaning.ipynb | Data preparation
      Merge datasets, normalize IDs, handle missing values, fix datatypes, rename columns, remove duplicates.

      - 02_EDA.ipynb | Insights
      Summaries, distributions, correlations, churn patterns, first insights.

      - 03_modeling.ipynb | Model training
      Feature engineering, encoding, train-test split, modeling, evaluation.

- `src/` — código modularizado (ETL, modelagem, explicabilidade)  
- `app/` — aplicação interativa para deployment (Gradio/Streamlit)  <-- hugging face
- `presentation/` — slides e material de apresentação  

## Principais tecnologias
Python (Pandas, Scikit-learn) --XGBoost, SHAP, LIME, Streamlit/Gradio-- talvevz

## Execução: Instalação do ambiente
1. Criar ambiente:
   ```bash
   pip install -r requirements.txt

 
1. Clonar o repositório a partir do GIT:

   ```bash

   git clone <URL_DO_REPOSITORIO>

   cd EnterpriseDataScienceBootcamp_workgroup

   # ou 

   ````Clonar a partir do VS Code
   
   Source Control (Ctrl + Shift + G) >> Clone Repository

2. Criar e ativar o ambiente virtual:
 
    ```bash

    Copiar código:

    python -m venv venv

    .\venv\Scripts\activate    # Windows

    ou

    .\.venv\Scripts\Activate.ps1

    # ou

    source venv/bin/activate   # Mac/Linux

    Instalar dependências:
    
    bash

    Copiar código

    pip install -r requirements.txt
 
 3. Atualizar local main e branch

 --garantir em que branch estamos, devemos estar no nosso main local
git branch

--o que tiver o asterisco é o branch onde estamos

-- atualizar o nosso main local
git pull origin main

-- alterar para o nosso branch e confirmar novamente
git branch

--o que tiver o asterisco é o branch onde estamos

-- fazer o merge do nosso branch com o main atualizado
git merge main

##########################################
##########################################
--Outra forma by sergio patinha
git checkout main
git pull origin main

git checkout sergio
git merge main

git push origin sergio
##########################################
##########################################