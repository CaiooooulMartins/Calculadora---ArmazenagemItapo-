import tkinter as tk
from tkinter import messagebox
import datetime as dt

def calcular_armazenagem():
    try:
        # Substitui a vírgula por ponto antes de converter para float
        valor = float(entry_valor.get().replace(",", "."))
        dataEntrada = entry_data_entrada.get()
        dataSaida = entry_data_saida.get()
        posicionamentoQtd = int(entry_posicionamentoQtd.get())
        gerenciamentoqtd = int(entry_gerenciamentoqtd.get())
        inspecaoQt = int(entry_inspecaoQt.get())
        agendamentoqtd = int(entry_agendamentoqtd.get())

        # Convertendo para datetime
        dataEntrada = dt.datetime.strptime(dataEntrada, '%d/%m/%Y')
        dataSaida = dt.datetime.strptime(dataSaida, '%d/%m/%Y')

        DiasArmazenados = dataSaida - dataEntrada
        DiasArmazenados = DiasArmazenados.days
        # Transformando os dias armazenados em int
        Armazenagem = int(DiasArmazenados) + 1

        periodo1 = list(range(1, 9))
        periodo2 = list(range(9, 21))
        periodo3 = list(range(22, 1000))
        periodo1pct = 0.0022
        periodo2pct = 0.002
        periodo3pct = 0.0035
        retirada = 335
        posicionamento = 767 * posicionamentoQtd
        gerenciamento = 1926 * gerenciamentoqtd
        inspecao = 420 * inspecaoQt
        agendamentoEspecial = 570 * agendamentoqtd

        if Armazenagem in periodo1:
            resultado = (periodo1pct * valor) + retirada + posicionamento + gerenciamento + inspecao + agendamentoEspecial
            if resultado <= 575:
                messagebox.showinfo("Resultado", f"O valor da Armazenagem é de R$575,00 e o processo se encontra no primeiro período.")
            else:
                messagebox.showinfo("Resultado", f"O valor total da armazenagem é de R${resultado:.2f}, de posicionamento tivemos R${posicionamento:.2f}, de Gerenciamento DTC tivemos R${gerenciamento:.2f}, de inspeção tivemos R${inspecao:.2f} e de agendamento especial tivemos R${agendamentoEspecial:.2f}. O processo se encontra no primeiro período.")
        elif Armazenagem in periodo2:
            resultado = (periodo1pct * valor) + (valor * periodo2pct * (Armazenagem - 8)) + retirada + posicionamento + gerenciamento + inspecao + agendamentoEspecial
            messagebox.showinfo("Resultado", f"O valor total da armazenagem é de R${resultado:.2f}, de posicionamento tivemos R${posicionamento:.2f}, de Gerenciamento DTC tivemos R${gerenciamento:.2f}, de inspeção tivemos R${inspecao:.2f} e de agendamento especial tivemos R${agendamentoEspecial:.2f}. O processo se encontra no segundo período. Tome cuidado com a Demurrage.")
        elif Armazenagem in periodo3:
            resultado = (periodo1pct * valor) + (periodo2pct * valor * 12) + (periodo3pct * valor * (Armazenagem - 20)) + retirada + posicionamento + gerenciamento + inspecao + agendamentoEspecial
            messagebox.showinfo("Resultado", f"O valor total da armazenagem é de R${resultado:.2f}, de posicionamento tivemos R${posicionamento:.2f}, de Gerenciamento DTC tivemos R${gerenciamento:.2f}, de inspeção tivemos R${inspecao:.2f} e de agendamento especial tivemos R${agendamentoEspecial:.2f}. O processo se encontra no terceiro período. Tome cuidado com a Demurrage.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Configurando a janela principal
app = tk.Tk()
app.title("Armazenagem Itapoá")

# Criando os widgets
label_valor = tk.Label(app, text="Valor do Processo:")
label_valor.pack(pady=5)

entry_valor = tk.Entry(app)
entry_valor.pack(pady=5)

label_data_entrada = tk.Label(app, text="Data de Entrada (dd/mm/yyyy):")
label_data_entrada.pack(pady=5)

entry_data_entrada = tk.Entry(app)
entry_data_entrada.pack(pady=5)

label_data_saida = tk.Label(app, text="Data de Saída (dd/mm/yyyy):")
label_data_saida.pack(pady=5)

entry_data_saida = tk.Entry(app)
entry_data_saida.pack(pady=5)

label_posicionamentoQtd = tk.Label(app, text="Quantidade de posicionamentos:")
label_posicionamentoQtd.pack(pady=5)

entry_posicionamentoQtd = tk.Entry(app)
entry_posicionamentoQtd.pack(pady=5)

label_gerenciamentoqtd = tk.Label(app, text="Gerenciamento de DTC (1 para sim, 0 para não):")
label_gerenciamentoqtd.pack(pady=5)

entry_gerenciamentoqtd = tk.Entry(app)
entry_gerenciamentoqtd.pack(pady=5)

label_inspecaoQt = tk.Label(app, text="Inspeção por scanner (1 para sim, 0 para não):")
label_inspecaoQt.pack(pady=5)

entry_inspecaoQt = tk.Entry(app)
entry_inspecaoQt.pack(pady=5)

label_agendamentoqtd = tk.Label(app, text="Agendamento especial (1 para sim, 0 para não):")
label_agendamentoqtd.pack(pady=5)

entry_agendamentoqtd = tk.Entry(app)
entry_agendamentoqtd.pack(pady=5)

button_calcular = tk.Button(app, text="Calcular", command=calcular_armazenagem)
button_calcular.pack(pady=20)

# Iniciando o loop principal
app.mainloop()