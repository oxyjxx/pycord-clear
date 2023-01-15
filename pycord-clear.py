#By: oKsi#1111 ; Python, PyCord, ClearCommand

# Очистка всего чата
@bot.command()
async def clear(ctx):
  await ctx.channel.purge(limit=None)
  
# Очистка количества сообщений
@bot.command()
async def amount_clear(ctx):
  await ctx.channel.purge(limit=50)
  
# Очистка количества сообщений №2
@bot.command()
async def amount_clear_two(ctx, amount: int=50):
  await ctx.channel.purge(limit=amount)
  
# Очистка сообщений канала
@bot.command()
async def channel_clear(ctx, channel: discord.TextChannel="Канал не указан."):
  await channel.purge(limit=50)
  
# Очистка сообщений пользователя
@bot.command()
async def user_clear(ctx, user: discord.User="Пользователь не указан."):
  msg = []
  async for m in ctx.channel.history():
    if len(msg) == 50:
      break
    if m.author == user:
      msg.append(m)
  await ctx.channel.delete_messages(msg)
