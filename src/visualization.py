"""
Módulo para visualização de dados de tráfego de rede.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from typing import Optional

def plot_traffic_over_time(df: pd.DataFrame, 
                          time_col: str = 'Time', 
                          length_col: str = 'Length',
                          window: int = 100,
                          title: str = 'Volume de Tráfego ao Longo do Tempo') -> plt.Figure:
    """
    Plota volume de tráfego ao longo do tempo.
    
    Args:
        df: DataFrame com dados de tráfego
        time_col: Nome da coluna de tempo
        length_col: Nome da coluna de tamanho
        window: Tamanho da janela para média móvel
        title: Título do gráfico
        
    Returns:
        Figura matplotlib
    """
    # Calcular tempo acumulado e média móvel
    df_plot = df.copy()
    df_plot['Time_cumulative'] = df_plot[time_col].cumsum()
    df_plot['Rolling_Mean'] = df_plot[length_col].rolling(window, min_periods=1).mean()
    
    # Criar figura
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(df_plot['Time_cumulative'], df_plot['Rolling_Mean'], linewidth=1)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlabel('Tempo (segundos)', fontsize=12)
    ax.set_ylabel('Tamanho Médio dos Pacotes', fontsize=12)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    
    return fig

def plot_protocol_distribution(df: pd.DataFrame, 
                              protocol_col: str = 'Protocol',
                              top_n: int = 10) -> plt.Figure:
    """
    Plota distribuição de protocolos de rede.
    
    Args:
        df: DataFrame com dados de tráfego
        protocol_col: Nome da coluna de protocolo
        top_n: Número de protocolos principais para mostrar
        
    Returns:
        Figura matplotlib
    """
    # Contar protocolos
    protocol_counts = df[protocol_col].value_counts().head(top_n)
    
    # Criar figura
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(range(len(protocol_counts)), protocol_counts.values)
    ax.set_title(f'Top {top_n} Protocolos de Rede', fontsize=14, fontweight='bold')
    ax.set_xlabel('Protocolo', fontsize=12)
    ax.set_ylabel('Número de Pacotes', fontsize=12)
    ax.set_xticks(range(len(protocol_counts)))
    ax.set_xticklabels(protocol_counts.index, rotation=45, ha='right')
    
    # Adicionar valores nas barras
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                f'{int(height):,}', ha='center', va='bottom', fontsize=10)
    
    plt.tight_layout()
    return fig

def plot_packet_size_distribution(df: pd.DataFrame, 
                                 length_col: str = 'Length',
                                 bins: int = 50) -> plt.Figure:
    """
    Plota distribuição de tamanhos de pacotes.
    
    Args:
        df: DataFrame com dados de tráfego
        length_col: Nome da coluna de tamanho
        bins: Número de bins para o histograma
        
    Returns:
        Figura matplotlib
    """
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    
    # Histograma
    axes[0].hist(df[length_col], bins=bins, edgecolor='black', alpha=0.7)
    axes[0].set_title('Distribuição de Tamanhos de Pacotes', fontsize=12)
    axes[0].set_xlabel('Tamanho (bytes)')
    axes[0].set_ylabel('Frequência')
    axes[0].grid(True, alpha=0.3)
    
    # Box plot
    axes[1].boxplot(df[length_col], vert=True, patch_artist=True)
    axes[1].set_title('Box Plot - Tamanhos de Pacotes', fontsize=12)
    axes[1].set_ylabel('Tamanho (bytes)')
    axes[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    return fig

if __name__ == "__main__":
    print("Módulo de visualização carregado.")
    print("Funções disponíveis:")
    print("- plot_traffic_over_time(df)")
    print("- plot_protocol_distribution(df)")
    print("- plot_packet_size_distribution(df)")
