# Armazenagem Itapoá

📚 **Descrição**  
O Armazenagem Itapoá é uma aplicação desenvolvida em Python com interface gráfica utilizando `tkinter`. Ele calcula os custos de armazenagem de processos logísticos com base em diversos parâmetros fornecidos pelo usuário, como valor do processo, datas de entrada e saída, e serviços adicionais.

---

## 💡 **Funcionalidades**  
- Cálculo de custos de armazenagem com base em períodos específicos.  
- Inclusão de custos adicionais:  
  - Posicionamento  
  - Gerenciamento de DTC  
  - Inspeção por scanner  
  - Agendamento especial  
- Exibição detalhada dos resultados (valores parciais e totais).  
- Tratamento de erros para entradas inválidas.  

---

## 🗂️ **Estrutura do Projeto**  
Principais arquivos:  
- `Amz.Itapoa.py`: Lógica principal do cálculo + interface gráfica.  
- `calculadoraforte2.py`: Calculadora adaptada para parâmetros diferentes.  

---

## 🚀 **Como Usar**  
1. Execute o arquivo principal:  
   ```bash
   python Amz.Itapoa.py
2. Preencha os campos obrigatórios:

- Valor do Processo: Valor monetário do processo.

- Data de Entrada e Data de Saída: Datas no formato dd/mm/yyyy.

- Quantidade de Posicionamentos: Número de movimentações.

- Gerenciamento de DTC: Insira 1 para sim ou 0 para não.

- Inspeção por Scanner: Insira 1 para sim ou 0 para não.

- Agendamento Especial: Insira 1 para sim ou 0 para não.

3.Clique no botão Calcular para visualizar os resultados.

## ⚙️  **REequisitos**   

- Python 3.8 ou superior.

- Bibliotecas:

- tkinter (inclusa no Python padrão).

- datetime.

## 📝  **Estrutura de Cálculo**   
 Os cálculos são baseados em três períodos:

1. Período 1: Dias 1 a 8.

2. Período 2: Dias 9 a 20.

3. Período 3: Dias 21 em diante.

Cada período possui uma taxa percentual aplicada ao valor do processo. Custos adicionais são somados ao resultado final.

## 🚧 **Tratamento de Erros**  

1. Entradas inválidas, como valores não numéricos ou datas em formato incorreto, exibem mensagens de erro amigáveis ao usuário.

## ✍️  **Autor**

Desenvolvido por Caio Martins.
