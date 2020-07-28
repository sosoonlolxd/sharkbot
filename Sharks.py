import discord
from discord.ext import commands 
client = commands.Bot( command_prefix = '+' )
embed_title_dict = {1:""}

@client.event
async def on_ready():
	print('Ready')
	await client.change_presence( status = discord.Status.do_not_disturb, activity = discord.Game("|Sharks|"))

#Kick
@client.command()
@commands.has_permissions ( administrator = True)
async def kick(ctx, member: discord.Member, *, reason=None):
	await ctx.channel.purge(limit = 1 )
	await member.kick(reason=reason)
	emb = discord.Embed(title='Информация о кике участника', description=f'{ member.name }',color=0xc25151)
	emb.set_author(name=member.name, icon_url=member.avatar_url)
	emb.add_field(name=f'ID: { member.id }',value=f'Кикнутый участник : { member }. **Причина кика:** ' + reason)
	emb.set_footer(text='Был кикнут администратором {}'.format(ctx.author.name), icon_url=ctx.author.avatar_url)
	await ctx.send(embed = emb)

#clear
@client.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount: int):
	await ctx.channel.purge(limit=1)
	amount = amount
	deleted = await ctx.channel.purge(limit=amount)
	await ctx.send(embed=discord.Embed(description=f':white_check_mark: Удалено  {len(deleted)} сообщений', color=0x0c0c0c), delete_after=3)


#mute
@client.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("Please specify a member")
        return
    role = discord.utils.get(ctx.guild.roles, name="muted")
    await member.add_roles(role)



#Ban
@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None):
	await ctx.channel.purge(limit=1)
	await member.ban(reason=reason)
	emb = discord.Embed(title='Информация о блокировке участника',color=0xc25151)
	emb.set_author(name=member.name, icon_url=member.avatar_url)
	emb.add_field(name=f'ID: { member.id }',value=f'Заблокированный участник : { member }')
	emb.set_footer(text='Забанил администратор {}'.format(ctx.author.name), icon_url=ctx.author.avatar_url)

	await ctx.send(embed=emb)

goose = ('''░░░░░░░░░░░░░░░░░░░░\n░░░░░ЗАПУСКАЕМ░░░░░░░\n░ГУСЯ░▄▀▀▀▄░РАБОТЯГИ░░
▄███▀░◐░░░▌░░░░░░░░░
░░░░▌░░░░░▐░░░░░░░░░
░░░░▐░░░░░▐░░░░░░░░░
░░░░▌░░░░░▐▄▄░░░░░░░
░░░░▌░░░░▄▀▒▒▀▀▀▀▄
░░░▐░░░░▐▒▒▒▒▒▒▒▒▀▀▄
░░░▐░░░░▐▄▒▒▒▒▒▒▒▒▒▒▀▄
░░░░▀▄░░░░▀▄▒▒▒▒▒▒▒▒▒▒▀▄
░░░░░░▀▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▀▄
░░░░░░░░░░░▌▌░▌▌░░░░░
░░░░░░░░░░░▌▌░▌▌░░░░░
░░░░░░░░░▄▄▌▌▄▌▌░░░░░''')

#auto-role
@client.event

async def on_member_join( member):
	channel = client.get_channel( 735393296884695150 )

	role = discord.utils.get( member.guild.roles, id = 735394962006605886 )
	await member.add_roles( role )
	emb = discord.Embed(description = f"**Пользователь** ``{ member.name }``, **присоединился к серверу! Не забудь прочитать правила)**",color = 0xB1BFF9)
	emb.set_image(url="https://media1.tenor.com/images/f3befb211d89eab9e07db4ca407cb76d/tenor.gif?itemid=13347764")
	await channel.send(embed = emb)
#тебя не любят
@client.event

async def on_member_remove( member):
	channel = client.get_channel( 735393296884695150 )
	emb = discord.Embed(description = f"**Пользователь** ``{ member.name }``, **ливнул с сервера!**",color = 0xB1BFF9)
	emb.set_image(url="https://media1.tenor.com/images/ce52606293142a2bd11cda1d3f0dc12c/tenor.gif?ite")
	await channel.send(embed = emb)

#fun
@client.command()
async def hug(ctx, member: discord.Member):
	if(hash(member)==hash(ctx.author)):
		await ctx.send('**Не надо так)**')
		return
	emb = discord.Embed(description = f'{ctx.author.name}, обнял(а) {member.mention}',color=0xc25151)
	emb.set_image(url="https://media1.tenor.com/images/7e30687977c5db417e8424979c0dfa99/tenor.gif?itemid=10522729")
	await ctx.send(embed = emb)  
############################################################
@client.command( pass_context = True )
async def say( ctx, *, arg):
	author = ctx.message.author
	await ctx.send(f'{ author.mention } **сказал(а) - **' + arg)

############################################################
@client.command()
async def kiss(ctx, member: discord.Member):
	if(hash(member)==hash(ctx.author)):
		await ctx.send('**Не надо так)**')
		return
	emb = discord.Embed(description = f'{ctx.author.name}, поцеловал(a) {member.mention}',color=0xc25155)
	emb.set_image(url="https://media1.tenor.com/images/f5167c56b1cca2814f9eca99c4f4fab8/tenor.gif?itemid=6155657")
	await ctx.send(embed = emb) 
############################################################
@client.command()
async def nom(ctx, member: discord.Member):
	if(hash(member)==hash(ctx.author)):
		await ctx.send('**Не надо так)**')
		return
	emb = discord.Embed(description = f'{ctx.author.name}, дал(а) вкусняшку {member.mention}',color=0xc25159)
	emb.set_image(url="https://media1.tenor.com/images/de3c538d45c1a0a615352f1ddc66ef02/tenor.gif?itemid=12075787")
	await ctx.send(embed = emb) 
############################################################
@client.command()
async def crycause(ctx, member: discord.Member):
	if(hash(member)==hash(ctx.author)):
		await ctx.send('**Не надо так)**')
		return
	emb = discord.Embed(description = f'{ctx.author.name}, расплакался(ась) из за {member.mention}',color=0xc25152)
	emb.set_image(url="https://media1.tenor.com/images/6e47929917ceb22efc613c381bfcd928/tenor.gif?itemid=16460949")
	await ctx.send(embed = emb) 
############################################################
@client.command()
async def cry(ctx):
	emb = discord.Embed(description = f'{ctx.author.name}, расплакался(ась)',color=0xc25153)
	emb.set_image(url="https://media1.tenor.com/images/4bb996f5c99d48faf8590d8c66396065/tenor.gif?itemid=7552065")
	await ctx.send(embed = emb) 
############################################################
@client.command()
async def bite(ctx, member: discord.Member):
	if(hash(member)==hash(ctx.author)):
		await ctx.send('**Не надо так)**')
		return
	emb = discord.Embed(description = f'{ctx.author.name}, укусил(а) {member.mention}',color=0xc25152)
	emb.set_image(url="https://media1.tenor.com/images/2a11c95dc96bb7ff64297f66b8a1b019/tenor.gif?itemid=12388163")
	await ctx.send(embed = emb)
############################################################
@client.command()
async def suicide(ctx):
	emb = discord.Embed(description = f'{ctx.author.name}, упал(а) с крыши.',color=0xc25152)
	emb.set_image(url="https://media1.tenor.com/images/bd67f01a9865f798a70a0ec0ac9c3d3c/tenor.gif?itemid=13980130")
	await ctx.send(embed = emb)
############################################################+
@client.command( pass_context = True )
async def slapbot( ctx ):
	
	author = ctx.message.author
	
	await ctx.send(goose)
#embed
@client.command()
@commands.has_permissions(administrator=True)
async def embed(ctx, *,rea=None):
    tmp ="** **"
    if(embed_title_dict.get(ctx.message.author.id)!=None):
        tmp=embed_title_dict.get(ctx.message.author.id)
    emb = discord.Embed(title="")
    emb.add_field(name=tmp, value=rea)
    await ctx.send(embed=emb)
    embed_title_dict[ctx.message.author.id]=None;
    
@client.command()
@commands.has_permissions(administrator=True)
async def embed_title(ctx, *,rea=None):

    embed_title_dict[ctx.message.author.id]=rea;
    print(embed_title_dict[ctx.message.author.id])
    await ctx.send('embed title set')

#хуйня
client.run('NzM2MTYwNjUyODkyMzA3NTE4.XxqxCA.t0M7t2MLuB5HaRizzx9LjJ-iTzw')