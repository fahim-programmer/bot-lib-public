from bot_lib import Edge_Driver, Chrome_Driver, FireFox_Driver, Bot


cd = Chrome_Driver()
bot = Bot(browser="Chrome", driver_exe=cd.install(), force_spawn_browser=False)
bot.get_url("https://www.google.com")
bot.timeout(2000)
bot.driver.quit()