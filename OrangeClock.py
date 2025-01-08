import asyncio
import datetime

class OrangeClock:
    def __init__(self):
        self.diccionario_numeros = {
        '0': [
            [1, 1, 1],
            [1, 0, 1],
            [1, 0, 1],
            [1, 0, 1],
            [1, 1, 1]
        ],
        '1': [
            [0, 1, 0],
            [1, 1, 0],
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0]
        ],
        '2': [
            [1, 1, 1],
            [0, 0, 1],
            [1, 1, 1],
            [1, 0, 0],
            [1, 1, 1]
        ],
        '3': [
            [1, 1, 1],
            [0, 0, 1],
            [1, 1, 1],
            [0, 0, 1],
            [1, 1, 1]
        ],
        '4': [
            [1, 0, 1],
            [1, 0, 1],
            [1, 1, 1],
            [0, 0, 1],
            [0, 0, 1]
        ],
        '5': [
            [1, 1, 1],
            [1, 0, 0],
            [1, 1, 1],
            [0, 0, 1],
            [1, 1, 1]
        ],
        '6': [
            [1, 1, 1],
            [1, 0, 0],
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ],
        '7': [
            [1, 1, 1],
            [0, 0, 1],
            [0, 0, 1],
            [0, 0, 1],
            [0, 0, 1]
        ],
        '8': [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ],
        '9': [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1],
            [0, 0, 1],
            [1, 1, 1],
        ],
        ':': [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        }
    def indexacion_derecha(self, cadena):  #para indexar la fecha
        return " " * (len(self.convert_digital_string(self.obtener_hora() ) ) // 5 - len(cadena) -1 )  

    def convert_digital_string(self, fecha_hora_formateada):
        cadena_completa = ""
        for i in range(5):
            for ch in fecha_hora_formateada:
                cadena_completa += str(self.diccionario_numeros[ch][i]).replace(',', " ").replace('[', ' ').replace(']', ' ').replace('0', ' ').replace('1', '#')  
            cadena_completa += "\n"
        return cadena_completa

    def obtener_hora(self):
        return datetime.datetime.now().strftime("%H:%M:%S")
    def obtener_fecha(self):
        return datetime.datetime.now().strftime("%Y/%m/%d")

    async def actualizar_reloj(self, salir):
        while not salir.is_set():
            print("\033[2J\033[H", end="")
            print(f"\033[38;5;208m{self.convert_digital_string(self.obtener_hora())}\033[0m")
            message = "Press Enter for exit"
            print(f"\033[38;5;208m{self.indexacion_derecha(self.obtener_fecha())}{self.obtener_fecha()}\033[0m")
            print(f"\033[38;5;208m{self.indexacion_derecha(message)}{message}\033[0m")
            await asyncio.sleep(1)

    async def leer_entrada(self, salir):
        await asyncio.get_event_loop().run_in_executor(None, input)
        salir.set()

    async def run_async(self):
        salir = asyncio.Event()
        task1 = asyncio.create_task(self.actualizar_reloj(salir))
        task2 = asyncio.create_task(self.leer_entrada(salir))
        await asyncio.gather(task1, task2)

    def run(self):
        asyncio.run(self.run_async())
if __name__ == '__main__':
        OrangeClock().run()
