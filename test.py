import os
import hashlib
import json

# 1. Vulnerabilidad de Seguridad Crítica: Inyección de Comandos (CWE-78)
# SonarQube detectará esto como una falla de "Comando del sistema usado con datos de entrada no validados".
def ejecutar_comando_inseguro(comando_usuario):
    # ¡NUNCA hagas esto en código real!
    print(f"Ejecutando: ping -c 1 {comando_usuario}")
    os.system(f"sudo ping -c 1 {comando_usuario}") # <-- Riesgo de Inyección

# 2. Vulnerabilidad de Seguridad: Uso de Hash Criptográfico Débil (CWE-327)
# SonarQube detectará el uso de MD5.
def generar_hash_debil(contrasena):
    return hashlib.md5(contrasena.encode()).hexdigest() # <-- MD5 es débil

# 3. Code Smell y Error Potencial: Condición Duplicada e Innecesaria
def verificar_edad(edad):
    if edad < 18:
        print("Menor de edad.")
        return False
    elif edad >= 18:  # <-- La condición 'edad >= 18' es redundante e innecesaria
        print("Mayor de edad.")
        return True

# 4. Code Smell: Lógica de Código Muerto (Dead Code)
def funcion_con_codigo_muerto():
    x = 10
    if False: # <-- Este bloque de código nunca se ejecutará
        print("Este código nunca se ve")
    return x + 5

# 5. Code Smell: Magic Number (Número Mágico)
IVA = 0.21 # <-- Esto está bien.
def calcular_precio_final(precio):
    precio_con_iva = precio + (precio * 0.21) # <-- Usar 0.21 directamente aquí es un "número mágico"
    return precio_con_iva

# 6. Error Lógico: Exposición de Stack Trace
# Esto expone detalles internos del sistema a un usuario.
def cargar_configuracion(archivo):
    try:
        with open(archivo, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error al cargar la configuración: {e}") # <--- Podría ser un error de seguridad/mantenimiento
        # La forma correcta sería: logging.error("...") y retornar un valor por defecto.


# --- Demostración ---
if __name__ == "__main__":
    print("--- 1. Inyección de Comandos ---")
    # Entrada de un atacante. En Linux/macOS, esto ejecutaría 'ls -l'.
    # Comando 'ping' se ejecutará con: 'ping -c 1 ; ls -l'
    comando_malicioso = "127.0.0.1; ls -l"
    ejecutar_comando_inseguro(comando_malicioso)

    print("\n--- 2. Hash Débil ---")
    hash_resultado = generar_hash_debil("MiContrasenaSecreta")
    print(f"Hash MD5 generado: {hash_resultado}")

    print("\n--- 3. Condición Duplicada ---")
    verificar_edad(20)

    print("\n--- 4. Código Muerto ---")
    print(funcion_con_codigo_muerto())

    print("\n--- 5. Número Mágico ---")
    print(f"Precio con IVA: {calcular_precio_final(100)}")

    print("\n--- 6. Manejo de Errores Inseguro ---")
    cargar_configuracion("archivo_que_no_existe.json")