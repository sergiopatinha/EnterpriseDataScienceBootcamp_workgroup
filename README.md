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
- `src/` — código modularizado (ETL, modelagem, explicabilidade)  
- `app/` — aplicação interativa para deployment (Gradio/Streamlit)  <-- hugging face
- `presentation/` — slides e material de apresentação  

## Principais tecnologias
Python (Pandas, Scikit-learn) --XGBoost, SHAP, LIME, Streamlit/Gradio-- talvevz

## Execução
1. Criar ambiente:
   ```bash
   pip install -r requirements.txt
