import anthropic

client = anthropic.Anthropic()


def redactar_mensaje_ia(nombre, empleados):
    respuesta = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=300,
        messages=[{
            "role": "user",
            "content": f"Soy comercial B2B de suministro industrial. Redacta un primer mensaje breve y profesional (máximo 60 palabras) para la empresa '{nombre}', que tiene {empleados} empleados. Tono cercano, termina proponiendo una llamada corta."
        }],
    )
    return respuesta.content[0].text


empresas = [
    ("Talleres Garcia", 8),
    ("Logistica Toledo", 45),
    ("Industrias del Centro", 320),
]

for nombre, empleados in empresas:
    print(nombre)
    print(redactar_mensaje_ia(nombre, empleados))
    print()
