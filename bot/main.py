import os
from typing import Optional
import serial
import asyncio
import discord
from discord.ui import View, Button
from discord.ext import commands

TOKEN = "TOKEN"

bot = commands.Bot(command_prefix="-", intents=discord.Intents.all(), description="prueba arduino")
bot.remove_command("help")

serialArduino = serial.Serial("COM3", 115200)

class MyView(discord.ui.View):

    def __init__(self):
        super().__init__()

        self.servo_uno = 90
        self.servo_dos = 80

    #ROW 0

    @discord.ui.button(emoji= "❌",style=discord.ButtonStyle.gray, disabled=True, row=0)
    async def button_1_1(self, interaction: discord.Interaction, Button: discord.ui.Button):
        await interaction.response.send_message("click")

    @discord.ui.button(style=discord.ButtonStyle.primary, emoji="🔼", row=0)
    async def  button_1_2(self, interaction: discord.Interaction, Button: discord.ui.Button):
        if self.servo_dos < 120:
            self.servo_dos = self.servo_dos + 20
            serialArduino.write(str("3").encode("ascii"))
            print(f"arriba, {self.servo_dos}")
            await interaction.response.send_message("enviando movimiento al arduino...", delete_after=1)
        else:
            await interaction.response.send_message("el motor se encuentra en el limite", delete_after=1)

    @discord.ui.button(emoji= "❌",style=discord.ButtonStyle.gray, disabled=True, row=0)
    async def button_1_3(self, interaction: discord.Interaction, Button: discord.ui.Button):
        await interaction.response.send_message("click")

    #ROW 1

    @discord.ui.button(style=discord.ButtonStyle.primary, emoji="◀", row=1)
    async def  button_2_1(self, interaction: discord.Interaction, Button: discord.ui.Button):
        if self.servo_uno > 0:
            self.servo_uno = self.servo_uno - 10
            print(f"izquierda, {self.servo_uno}")
            serialArduino.write(str("2").encode("ascii"))
            await interaction.response.send_message("enviando movimiento al arduino...", delete_after=1)
        else:
            await interaction.response.send_message("el motor se encuentra en el limite", delete_after=1)
    
    @discord.ui.button(emoji= "⏺",style=discord.ButtonStyle.gray, row=1)
    async def button_2_2(self, interaction: discord.Interaction, Button: discord.ui.Button):
        self.servo_uno = 90
        self.servo_dos = 80
        print(f"servo uno, {self.servo_uno}")
        print(f"servo dos, {self.servo_uno}")
        serialArduino.write(str("5").encode("ascii"))
        await interaction.response.send_message("los motores han vuelto a su posicion inicial", delete_after=1)

    @discord.ui.button(style=discord.ButtonStyle.primary, emoji="▶", row=1)
    async def  button_2_3(self, interaction: discord.Interaction, Button: discord.ui.Button):
        if self.servo_uno < 180:
            self.servo_uno = self.servo_uno + 10
            print(f"derecha, {self.servo_uno}")
            serialArduino.write(str("1").encode("ascii"))
            await interaction.response.send_message("enviando movimiento al arduino...", delete_after=1)
        else:
            await interaction.response.send_message("el motor se encuentra en el limite", delete_after=1)

    #ROW 2   

    @discord.ui.button(emoji= "❌",style=discord.ButtonStyle.gray, disabled=True, row=2)
    async def button_3_1(self, interaction: discord.Interaction, Button: discord.ui.Button):
        await interaction.response.send_message("click")

    @discord.ui.button(style=discord.ButtonStyle.primary,emoji="🔽", row=2) 
    async def  button_3_2(self, interaction: discord.Interaction, Button: discord.ui.Button):
        if self.servo_dos > 0:
            self.servo_dos = self.servo_dos - 20
            print(f"abajo, {self.servo_dos}")
            serialArduino.write(str("4").encode("ascii"))
            await interaction.response.send_message("enviando movimiento al arduino...", delete_after=1)
        else:
            await interaction.response.send_message("el motor se encuentra en el limite", delete_after=1)

    @discord.ui.button(emoji= "❌",style=discord.ButtonStyle.gray, disabled=True, row=2)
    async def button_3_3(self, interaction: discord.Interaction, Button: discord.ui.Button):
        await interaction.response.send_message("click")

@bot.command()
async def movimiento(ctx):
    servo_embed = discord.Embed(title="Movimiento de la plataforma",
                                description="presiona los botones para poder mover la plataforma con los servomotores",
                                color= discord.Color.green())
    await ctx.send(embed= servo_embed,view = MyView(), delete_after= 60)

bot.run(TOKEN)