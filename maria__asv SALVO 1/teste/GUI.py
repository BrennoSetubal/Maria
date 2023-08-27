import tkinter as tk
import pyaudio
import numpy as np
import threading
import queue
import time

CHUNK = 1024  # Tamanho do buffer de áudio
FORMAT = pyaudio.paInt16  # Formato do áudio
CHANNELS = 1  # Número de canais de áudio (1 para mono, 2 para estéreo)
RATE = 44100  # Taxa de amostragem do áudio (Hz)

def animate_microphone():
    global microphone_id
    canvas.delete("microphone")  # Limpar a tela antes de redesenhar
    x = canvas_width / 2
    y = canvas_height / 2 + (20 * np.sin(time.time() * 3))  # Movimento senoidal
    microphone_id = canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="red", tags="microphone")
    root.after(50, animate_microphone)  # Redesenhar após 50 milissegundos

def read_microphone(q):
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    while True:
        data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
        q.put(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

def process_microphone(q):
    while True:
        data = q.get()
        # Faça o processamento necessário aqui, se desejar
        # Neste exemplo, não faremos nada com os dados, apenas animaremos o microfone

data_queue = queue.Queue()

root = tk.Tk()
root.title("Microfone Interativo")

canvas_width = 400
canvas_height = 300
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

microphone_thread = threading.Thread(target=read_microphone, args=(data_queue,))
microphone_thread.daemon = True
microphone_thread.start()

process_thread = threading.Thread(target=process_microphone, args=(data_queue,))
process_thread.daemon = True
process_thread.start()

animate_microphone()

root.protocol("WM_DELETE_WINDOW", root.quit)
root.mainloop()
