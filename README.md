# 🕒 OrangeClock

**OrangeClock** es un reloj digital minimalista que se muestra en la terminal. Representa la hora actual en un formato de caracteres visualmente atractivo, utilizando `#` para formar números. Este proyecto está desarrollado en Python y utiliza programación asincrónica para actualizar la hora en tiempo real.

---

## 🚀 Características

- ✅ **Reloj en tiempo real**: Muestra la hora actual y se actualiza automáticamente cada segundo.
- ✅ **Interfaz visual simple**: Los números son representados con el carácter `#` para formar un diseño digital.
- ✅ **Color personalizado**: El reloj se muestra en color naranja utilizando códigos ANSI.
- ✅ **Salida limpia**: Pulsa ENTER para salir del programa en cualquier momento.

---

## 🖥️ Captura de pantalla
![image](https://github.com/user-attachments/assets/471120d9-9c0d-44e7-987e-ae25542c7c08)



---

## 🛠️ Instalación

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/victor522m/orangeclock.git
   cd orangeclock
   ```

2. **Instala Python**:
   Asegúrate de tener Python 3.7 o superior instalado en tu sistema. Puedes verificarlo con:
   ```bash
   python --version
   ```

3. **Ejecuta el programa**:
   No se necesitan dependencias adicionales. Simplemente ejecuta:
   ```bash
   python main.py
   ```

---

## 📄 Uso

1. Ejecuta el programa desde la terminal:
   ```bash
   python main.py
   ```

2. Observa cómo el reloj digital muestra la hora actual en tiempo real.

3. Pulsa **ENTER** para detener el programa.

---

## 🧩 Estructura del proyecto

```
orangeclock/
│
├── orange_clock.py   # Código principal de la clase OrangeClock
├── main.py           # Archivo para iniciar el programa
└── README.md         # Este archivo
```

---

## ✨ Personalización

Puedes personalizar el proyecto modificando los siguientes aspectos:

- **Color del reloj**:
  Cambia el código ANSI `\033[38;5;208m` en el método `actualizar_reloj` para usar otros colores.

- **Formato de los números**:
  Edita el diccionario `diccionario_numeros` en la clase `OrangeClock` para cambiar la representación de los números.

---

## 🛡️ Licencia

Este proyecto está bajo la GNU General Public License v3.0. Puedes usarlo, modificarlo y distribuirlo libremente, siempre y cuando incluyas la licencia original.

---

## 🧑‍💻 Contribuciones

¡Las contribuciones son bienvenidas! Si encuentras un error o tienes ideas para mejorar el proyecto:

1. Haz un fork del repositorio.
2. Crea una nueva rama:
   ```bash
   git checkout -b mi-mejora
   ```
3. Realiza tus cambios y haz un commit:
   ```bash
   git commit -m "Mejora: Añadido soporte para ..."
   ```
4. Envía un pull request.

---

## 📧 Contacto

Si tienes preguntas o sugerencias, no dudes en abrir un issue en el repositorio o contactarme en [tu-email@example.com](mailto:tu-email@example.com).

---

¡Gracias por usar **OrangeClock**! 😊
