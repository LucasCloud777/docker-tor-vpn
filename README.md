# 🚀 Análise de Tráfego de Rede: Docker com TOR/VPN

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LucasCloud777/docker-tor-vpn/blob/main/notebooks/dockertorvpntrafficprocess.ipynb)
[![GitHub stars](https://img.shields.io/github/stars/LucasCloud777/docker-tor-vpn?style=social)](https://github.com/LucasCloud777/docker-tor-vpn/stargazers)

**Análise completa de tráfego de rede em ambiente Docker com comunicação TOR/VPN utilizando técnicas avançadas de Data Science e Machine Learning.**

---

## 📋 Índice
- [Visão Geral](#-visão-geral)
- [Conjunto de Dados](#-conjunto-de-dados)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias](#-tecnologias)
- [Instalação e Uso](#-instalação-e-uso)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Análises Realizadas](#-análises-realizadas)
- [Resultados](#-resultados)
- [Como Contribuir](#-como-contribuir)
- [Licença](#-licença)
- [Contato](#-contato)

---

## 🎯 Visão Geral

Este projeto realiza uma análise completa de capturas de tráfego de rede em um ambiente Docker configurado com TOR/VPN. O objetivo é entender padrões de comunicação, detectar anomalias e aplicar modelos de Machine Learning para classificação e previsão.

### Objetivos Principais:
1. **Análise Exploratória**: Compreender a distribuição e características do tráfego
2. **Detecção de Anomalias**: Identificar comportamentos suspeitos ou anômalos
3. **Classificação**: Categorizar tipos de tráfego e serviços
4. **Clusterização**: Agrupar IPs por padrões de comportamento similares

---

## 📊 Conjunto de Dados

### Características:
- **Fonte**: Captura Wireshark/Tshark de ambiente Docker com TOR
- **Tamanho**: 146,434 pacotes de rede
- **Período**: Sessão contínua de captura
- **Formato**: CSV exportado do Wireshark

### Colunas Disponíveis:
| Coluna | Tipo | Descrição |
|--------|------|-----------|
| `No.` | Integer | Número sequencial do pacote |
| `Time` | Float | Timestamp relativo (segundos) |
| `Source` | String | Endereço IP de origem |
| `Destination` | String | Endereço IP de destino |
| `Protocol` | String | Protocolo de rede (TCP, TLS, HTTP, etc.) |
| `Length` | Integer | Tamanho do pacote em bytes |
| `Info` | String | Informações detalhadas do pacote |

---

## ✨ Funcionalidades

### 🔍 Análise Exploratória
- Visualização temporal do tráfego
- Distribuição de protocolos e portas
- Análise de matriz de comunicação
- Estatísticas descritivas avançadas

### 🛠️ Feature Engineering
- Extração automática de portas TCP/UDP
- Identificação de flags TCP (SYN, ACK, FIN, RST)
- Cálculo de métricas de tempo entre pacotes
- Criação de identificadores únicos de fluxo

### 🤖 Modelos de Machine Learning
- **Classificação**: Random Forest, XGBoost, LightGBM
- **Detecção de Anomalias**: Isolation Forest
- **Clusterização**: K-Means com redução dimensional (PCA)
- **Regressão Temporal**: Previsão de volume de tráfego

### 📈 Visualização
- Gráficos interativos com Plotly
- Heatmaps de comunicação
- Análise de séries temporais
- Visualização de clusters

---

## 🛠️ Tecnologias

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge&logo=python&logoColor=white)

**Stack Completa:**
- **Processamento de Dados**: Pandas, NumPy, SciPy
- **Visualização**: Matplotlib, Seaborn, Plotly
- **Machine Learning**: Scikit-learn, XGBoost, LightGBM
- **Ambiente**: Jupyter Notebook, Google Colab
- **Controle de Versão**: Git, GitHub

---

## 🚀 Instalação e Uso

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. **Clonar o repositório:**
```bash
git clone https://github.com/LucasCloud777/docker-tor-vpn.git
cd docker-tor-vpn

## 📈 Status do Projeto
![GitHub last commit](https://img.shields.io/github/last-commit/LucasCloud777/docker-tor-vpn)
![GitHub repo size](https://img.shields.io/github/repo-size/LucasCloud777/docker-tor-vpn)

## 📊 Dados
- **Arquivo**: `data/raw/dockertorvpn.csv`
- **Tamanho**: 20.7 MB
- **Pacotes**: 146,434 registros
