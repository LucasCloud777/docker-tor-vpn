"""
Módulo para pré-processamento de dados de tráfego de rede.
"""

import pandas as pd
import numpy as np
import re
from typing import Tuple, Optional

def load_data(filepath: str) -> pd.DataFrame:
    """
    Carrega dados de tráfego de rede de um arquivo CSV.
    
    Args:
        filepath: Caminho para o arquivo CSV
        
    Returns:
        DataFrame com os dados carregados
    """
    return pd.read_csv(filepath)

def extract_ports(info: str) -> Tuple[Optional[int], Optional[int]]:
    """
    Extrai portas de origem e destino do campo Info.
    
    Args:
        info: String com informações do pacote
        
    Returns:
        Tupla (porta_origem, porta_destino)
    """
    ports = re.findall(r'(\d+) > (\d+)', str(info))
    if ports:
        return int(ports[0][0]), int(ports[0][1])
    return None, None

def extract_tcp_flags(info: str) -> str:
    """
    Extrai flags TCP do campo Info.
    
    Args:
        info: String com informações do pacote
        
    Returns:
        String com flags separadas por vírgula
    """
    flags = []
    if 'SYN' in str(info): flags.append('SYN')
    if 'ACK' in str(info): flags.append('ACK')
    if 'FIN' in str(info): flags.append('FIN')
    if 'PSH' in str(info): flags.append('PSH')
    if 'RST' in str(info): flags.append('RST')
    return ','.join(flags) if flags else 'NONE'

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Pipeline completo de pré-processamento.
    
    Args:
        df: DataFrame com dados brutos
        
    Returns:
        DataFrame pré-processado
    """
    df_processed = df.copy()
    
    # Extrair portas
    df_processed[['Source_Port', 'Dest_Port']] = df_processed['Info'].apply(
        lambda x: pd.Series(extract_ports(x))
    )
    
    # Converter portas para numérico
    df_processed['Source_Port'] = pd.to_numeric(df_processed['Source_Port'], errors='coerce')
    df_processed['Dest_Port'] = pd.to_numeric(df_processed['Dest_Port'], errors='coerce')
    
    # Extrair flags TCP
    df_processed['TCP_Flags'] = df_processed['Info'].apply(extract_tcp_flags)
    
    # Criar features adicionais
    df_processed['Time_Diff'] = df_processed['Time'].diff().fillna(0)
    df_processed['Time_cumulative'] = df_processed['Time'].cumsum()
    df_processed['Flow_ID'] = df_processed['Source'] + '_' + df_processed['Destination']
    
    return df_processed

if __name__ == "__main__":
    print("Módulo de pré-processamento carregado.")
    print("Funções disponíveis:")
    print("- load_data(filepath)")
    print("- extract_ports(info)")
    print("- extract_tcp_flags(info)")
    print("- preprocess_data(df)")
