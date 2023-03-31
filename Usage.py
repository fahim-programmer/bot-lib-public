from Bot_lib import Selenium_bot, Chrome_Driver

class YourBot(Selenium_bot):
    def __init__(self):
        super().__init__(browser="Chrome", driver_exe=Chrome_Driver())
        # Do Stuff Here
        self.get_url("https://www.duckduckgo.com")
        self.timeout()

if __name__ == "__main__":
    YourBot()