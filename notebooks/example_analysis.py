#!/usr/bin/env python
"""
Exemplo de análise do dataset Docker TOR/VPN
"""

import pandas as pd
import matplotlib.pyplot as plt
from src.data_preprocessing import load_data, preprocess_data

def main():
    print("Exemplo de Análise - Docker TOR/VPN Traffic")
    print("=" * 50)
    
    # Carregar dados
    df = load_data('data/raw/dockertorvpn.csv')
    df_processed = preprocess_data(df)
    
    # Análise básica
    print(f"Total de pacotes: {len(df_processed):,}")
    print(f"IPs únicos: {df_processed['Source'].nunique()}")
    print(f"Protocolos: {df_processed['Protocol'].unique()}")
    
    # Salvar resultados
    df_processed.to_csv('reports/results/processed_data_sample.csv', index=False)
    print("✅ Análise concluída!")

if __name__ == "__main__":
    main()
