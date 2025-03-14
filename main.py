import discord
from discord.ext import commands
import random
from model import get_class
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'Hola!, has iniciado sesión como {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('$hola'):
        await message.channel.send("hola, como has estado hoy?")
    if message.content.startswith("$hola amigo"):
        await message.channel.send("https://th.bing.com/th/id/OIP.1Won_QcQaiprPgZEPy52uwHaHH?rs=1&pid=ImgDetMain")
        await message.channel.send(f"Hola, bienvenid@, soy {bot.user}")
    elif message.content.startswith('$bien'):
        await message.channel.send("me alegro, que tengas un lindo día")
    elif message.content.startswith('$adiós'):
        await message.channel.send("adiós, cúidate, no olvides regresar :)")
    elif message.content.startswith('$¿Cómo estás?'):
        await message.channel.send("bien, y tú?")
    elif message.content.startswith('$cuál es tu aplicación favorita'):
        await message.channel.send("discord, me gusta que nostros los bots podamos ayudarlos aquí")
    elif message.content.startswith('🤣'):
        await message.channel.send("😂")
    elif message.content.startswith('😎'):
        await message.channel.send("😎")
    elif message.content.startswith('$Tengo mucho sueño 🥱'):
        await message.channel.send("Hola, que puedo hacer para ayudarte 😴?")
    elif message.content.startswith('😑'):
        await message.channel.send("😐")
    elif message.content.startswith('😄'):
        await message.channel.send("😆")
    elif message.content.startswith('😨'):
        await message.channel.send("🤯")
@bot.event
async def IA(ctx):
    if ctx.message.attachments:
        for archivo in ctx.message.attachments:
            nombre_archivo = archivo.filename
            await archivo.save(f"Img/{nombre_archivo}")
        await ctx.send("IMAGEN GUARDADA")
        # Obtener el resultado y forzar a cadena
        resultado = str(get_class(model_path="keras_model.h5", 
                                  labels_path='labels.txt', 
                                  image_path=f"Img/{nombre_archivo}"))
        
        
        # Verificar y enviar el mensaje
        if resultado and resultado.strip():
            await ctx.send("TU IMAGEN PERTENECE AL GRUPO:")
            await ctx.send(resultado)
        else:
            await ctx.send("No se pudo clasificar la imagen. Intenta nuevamente.")
    else:
        await ctx.send("EL MENSAJE NO TIENE ARCHIVOS, ADJUNTA EL O LOS ARCHIVOS NECESARIOS")
if __name__ == "__main__":
    model_path = "keras_Model.h5"
    labels_path = "labels.txt"
    image_path = "img\prueba_paloma.jpg"
    result = get_class(model_path, labels_path, image_path)
    print(result)

bot.run("tokensecreto")
