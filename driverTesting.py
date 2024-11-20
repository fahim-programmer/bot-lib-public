from Bot_lib import Edge_Driver, Chrome_Driver, FireFox_Driver, Bot


cd = Chrome_Driver()
bot = Bot(browser="Chrome", driver_exe=cd.install(), force_spawn_browser=True)
while True:
    command = input("Input Syntax <- ")
    if command == "EMITSIG-CLOSE": break
    eval(command)
    print("EMITSIG-FINISHED")
    #bot.get_url("https://www.google.com")
#bot.timeout(2000)
bot.driver.quit()