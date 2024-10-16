import tkinter as tk
import chessEngine
class App():
    def __init__(self, L_QUADRADO):
        self.gs = chessEngine.GameState()
        self.L_QUADRADO = L_QUADRADO
        self.imagenes = {}

        self.ventana = tk.Tk()
        self.ventana.title("Ajedrez ITC")
        self.ventana.geometry(f"{str(L_QUADRADO * 8)}x{str(L_QUADRADO * 8)}")
        self.ventana.resizable(0, 0)

        self.interfaz = tk.Canvas(self.ventana)
        self.interfaz.pack(fill="both", expand=True)
    def __call__(self):
        self.ventana.mainloop()
    
    def dibujartablero(self):
        for i in range(8):
            for j in range(8):
                if (i+j) % 2 ==0:
                    self.interfaz.create_rectangle(i*self.L_QUADRADO, j*self.L_QUADRADO, (i+1)*self.L_QUADRADO, (j+1)*self.L_QUADRADO, fill="#dfc07f")
                else:
                    self.interfaz.create_rectangle(i*self.L_QUADRADO, j*self.L_QUADRADO, (i+1)*self.L_QUADRADO, (j+1)*self.L_QUADRADO, fill="#7a4f37")

    def cargarimg (self):
        piezas = ["peon_blanco","peon_negro","caballo_blanco","caballo_negro","torre_blanco","torre_negra","afil_blanco","afil_negro","reina_blanca","reina_negra", "rey_blanco","rey_negro"]
        for pieza in piezas:
            self.imagenes[pieza] = tk.PhotoImage(file="./img/" + pieza + ".png")

    def mostrarPiezas(self):
        for indice_i, i in enumerate(self.gs.piezas):
            for indice_j, j in enumerate(i):
                if j != "--":
                    self.interfaz.create_image(indice_j*self.L_QUADRADO, indice_i * self.L_QUADRADO, image=self.imagenes[j], anchor="nw")

MotorDeAjedrez = App(75)
MotorDeAjedrez.dibujartablero()
MotorDeAjedrez.cargarimg()
MotorDeAjedrez.mostrarPiezas()


MotorDeAjedrez()
