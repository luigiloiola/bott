import discord
from discord.ext import commands
from discord.ext.commands import Bot
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



client: Bot = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('sua mae na cama'))
    print('bot online')

#comando para checar o ms do servidor
@client.command(aliases=['ms','ms do servidor','server ms', 'ms servidor'])
async def oie(ctx):
    await ctx.send(f'{int(client.latency * 1000)}ms')
#comando do op do bot
@client.command(aliases=['status',])
async def op(ctx,*, member):
    path = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get("https://br.op.gg/")
    search = driver.find_element_by_name('userName')
    search.send_keys(member)
    search.send_keys(Keys.RETURN)

    #esperar que o elemento exista na pagina, antes dele ser selecionado
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="left_champion"]/a'))
        )
        vitoria = driver.find_element_by_xpath('//*[@id="SummonerLayoutContent"]/div[2]/div[1]/div[1]/div/div[2]/div[3]/span[2]/span[1]').text
        derrota = driver.find_element_by_xpath('//*[@id="SummonerLayoutContent"]/div[2]/div[1]/div[1]/div/div[2]/div[3]/span[2]/span[2]').text
        vitorias = int(vitoria.replace('V',''))
        derrotas=int(derrota.replace('L',''))
        partidas = vitorias + derrotas
        pdl = driver.find_element_by_class_name('LeaguePoints').text
        rank = driver.find_element_by_class_name('TierRank').text
        wr = driver.find_element_by_class_name('winratio').text
        element.click()
        await ctx.send(f'''{member}
{rank} ({pdl}) ({wr})  ({partidas} partidas)
---------------------------------------------------------------------------
''')

    except:
        driver.close()
    try:
        elementt = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="SummonerLayoutContent"]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[1]/td[3]'))
        )
        main1 = elementt.text
        wr1= driver.find_element_by_xpath('//*[@id="SummonerLayoutContent"]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[1]/td[4]/div/span').text
        wr2 = driver.find_element_by_xpath('//*[@id="SummonerLayoutContent"]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[2]/td[4]/div/span').text
        wr3 = driver.find_element_by_xpath('//*[@id="SummonerLayoutContent"]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[3]/td[4]/div/span').text
        main2= driver.find_element_by_xpath('//*[@id="SummonerLayoutContent"]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[2]/td[3]/a').text
        main3 = driver.find_element_by_xpath('//*[@id="SummonerLayoutContent"]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[3]/td[3]/a').text
        await ctx.send(f'main 1: {main1} ({wr1})')
        await ctx.send(f'main 2: {main2}({wr2})')
        await ctx.send(f'main 3: {main3}({wr3})')
    finally:
        driver.quit()
@client.command(aliases=['stats'])
async def fun(ctx, *, member):
    path = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get(f"https://br.op.gg/summoner/userName={member}")
    click = driver.find_element_by_xpath('//*[@id="left_champion"]/a')
    vitoria = driver.find_element_by_xpath(
        '//*[@id="SummonerLayoutContent"]/div[2]/div[1]/div[1]/div/div[2]/div[3]/span[2]/span[1]').text
    derrota = driver.find_element_by_xpath(
        '//*[@id="SummonerLayoutContent"]/div[2]/div[1]/div[1]/div/div[2]/div[3]/span[2]/span[2]').text
    vitorias = int(vitoria.replace('V', ''))
    derrotas = int(derrota.replace('L', ''))
    partidas = vitorias + derrotas
    pdl = driver.find_element_by_class_name('LeaguePoints').text
    rank = driver.find_element_by_class_name('TierRank').text
    wr = driver.find_element_by_class_name('winratio').text
    await ctx.send(f'''{member}
    {rank} ({pdl}) ({wr})  ({partidas} partidas)
    ---------------------------------------------------------------------------
    ''')
    click.click()
    try:
        elementt = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="SummonerLayoutContent"]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[1]/td[3]'))
        )
        main1 = elementt.text
        wr1= driver.find_element_by_xpath('//*[@id="SummonerLayoutContent"]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[1]/td[4]/div/span').text
        wr2 = driver.find_element_by_xpath('//*[@id="SummonerLayoutContent"]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[2]/td[4]/div/span').text
        wr3 = driver.find_element_by_xpath('//*[@id="SummonerLayoutContent"]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[3]/td[4]/div/span').text
        main2= driver.find_element_by_xpath('//*[@id="SummonerLayoutContent"]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[2]/td[3]/a').text
        main3 = driver.find_element_by_xpath('//*[@id="SummonerLayoutContent"]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[3]/td[3]/a').text
        await ctx.send(f'main 1: {main1} ({wr1})')
        await ctx.send(f'main 2: {main2}({wr2})')
        await ctx.send(f'main 3: {main3}({wr3})')
    finally:
        driver.quit()



@client.command(aliases=['lastgame'])
async def historico(ctx,*,member):
    path = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get('https://br.op.gg/l=pt')
    search = driver.find_element_by_name('userName')
    search.send_keys(member)
    search.send_keys(Keys.RETURN)
    try:
        atualizar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'SummonerRefreshButton'))
        )
        atualizar.click()
    except:
        try:
            campeao = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH,
                     '//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div/div[1]/div[2]/div[4]/a'))
            )
            champ = campeao.text
            winloose = driver.find_element_by_xpath(
                '//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div/div[1]/div[1]/div[4]').text
            k = driver.find_element_by_xpath(
                '//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div/div[1]/div[3]/div[1]/span[1]').text
            d = driver.find_element_by_xpath(
                '//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div/div[1]/div[3]/div[1]/span[2]').text
            a = driver.find_element_by_xpath(
                '//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div/div[1]/div[3]/div[1]/span[3]').text
            await ctx.send(f'''{winloose} 
{champ} ({k}/{d}/{a}) ''')
        finally:
            driver.quit()
    finally:
        try:
            campeao = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH,
                     '//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div/div[1]/div[2]/div[4]/a'))
            )
            champ = campeao.text
            winloose = driver.find_element_by_xpath(
                '//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div/div[1]/div[1]/div[4]').text
            k = driver.find_element_by_xpath(
                '//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div/div[1]/div[3]/div[1]/span[1]').text
            d = driver.find_element_by_xpath(
                '//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div/div[1]/div[3]/div[1]/span[2]').text
            a = driver.find_element_by_xpath(
                '//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div/div[1]/div[3]/div[1]/span[3]').text
            await ctx.send(f'''{winloose} 
{champ} ({k}/{d}/{a}) ''')
        finally:
            driver.quit()
    #(f'https://br.op.gg/summoner/userName={member}')
@client.command(aliases= ['barril'])
async def gp(ctx,*,member : discord.Member):
    channel = discord.utils.get(ctx.guild.channels, name='barril')
    await member.move_to(channel)




                                                                     #await channel.send(f'{msg.content}')

client.run('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
#id=   834293526132162580        834127252693188649, 'guild_id'
