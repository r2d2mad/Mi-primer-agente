import json
import anthropic

client = anthropic.Anthropic()


def calcular_prioridad(empleados):
    if empleados >= 100:
        return "ALTA"
    elif empleados >= 20:
        return "MEDIA"
    return "BAJA"


def guardar_mensaje(empresa, mensaje):
    with open("mensajes.txt", "a", encoding="utf-8") as f:
        f.write(empresa + ": " + mensaje + "\n\n")
    return "Mensaje guardado para " + empresa


herramientas = [
    {
        "name": "calcular_prioridad",
        "description": "Calcula la prioridad comercial (ALTA, MEDIA o BAJA) de una empresa según su número de empleados.",
        "input_schema": {
            "type": "object",
            "properties": {"empleados": {"type": "integer"}},
            "required": ["empleados"],
        },
    },
    {
        "name": "guardar_mensaje",
        "description": "Guarda en un archivo el mensaje comercial redactado para una empresa.",
        "input_schema": {
            "type": "object",
            "properties": {
                "empresa": {"type": "string"},
                "mensaje": {"type": "string"},
            },
            "required": ["empresa", "mensaje"],
        },
    },
]

funciones = {
    "calcular_prioridad": calcular_prioridad,
    "guardar_mensaje": guardar_mensaje,
}

tarea = (
    "Soy Arturo Cerro, comercial B2B de suministro industrial en Toledo y Madrid. "
    "Firma cada mensaje con mi nombre y no uses corchetes ni huecos como [Nombre] o [Empresa]. "
    "Para cada empresa de esta lista, "
    "calcula su prioridad, redacta un primer mensaje breve (máx. 50 palabras) adaptado "
    "a esa prioridad y guárdalo. Empresas: Talleres Garcia (8 empleados), "
    "Logistica Toledo (45), Industrias del Centro (320)."
)

mensajes = [{"role": "user", "content": tarea}]

while True:
    respuesta = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1500,
        tools=herramientas,
        messages=mensajes,
    )
    mensajes.append({"role": "assistant", "content": respuesta.content})

    if respuesta.stop_reason != "tool_use":
        break

    resultados = []
    for bloque in respuesta.content:
        if bloque.type == "tool_use":
            print("Usando herramienta:", bloque.name, bloque.input)
            salida = funciones[bloque.name](**bloque.input)
            resultados.append({
                "type": "tool_result",
                "tool_use_id": bloque.id,
                "content": str(salida),
            })
    mensajes.append({"role": "user", "content": resultados})

for bloque in respuesta.content:
    if bloque.type == "text":
        print("\nRespuesta final:", bloque.text)
