# Bot_lib Public v1.0.1 Release 1-April 2023

This is python module aims to provide user-friendly interface to the web-automation and desktop automation tools available like Selenium. It offers driver management, proxies, proxy testing, shorter source code and faster development with cross browser script compatibility. The aim is to streamline the automation procedure, minimize the detection and reduce the time of development needed. The scripts generated with bot_lib could be very complex yet still very readable and less error-prone, and they are easier to maintain.

## Installation 

Watch video tutorial here https://www.youtube.com/watch?v=rFLyj9u0MbE

You have to make a virtual environment or not and put this command on your terminal and the latest public release will install.

```
pip install bot-lib-public
```

Now you can use it like this

```
from bot_lib import Bot, Chrome_Driver

class YourBot(Bot):
    def __init__(self):
        super().__init__(browser="Chrome", driver_exe=Chrome_Driver())
        # Do Stuff Here
        self.get_url("https://www.duckduckgo.com")
        self.timeout()

if __name__ == "__main__":
    YourBot()
```

Keep in mind that automatic driver installation (Chrome_Driver and others) may not work for platforms other than windows so you have to point it to the driver executable by entering a path to it like this.

```
from bot_lib import Bot

class YourBot(Bot):
    def __init__(self):
        super().__init__(browser="Chrome", driver_exe="chromedriver.exe")
        # Do Stuff Here
        self.get_url("https://www.duckduckgo.com")
        self.timeout()

if __name__ == "__main__":
    YourBot()
```

### How I started with bot-lib?

I started to make bot lib which contained classes to automatically setup everything everytime I wanted to use selenium automation. 

I had a very basic version in the end of 2021 in December then added new methods in the April of 2022, and then continued to improve it and add new things to the it. 

In August of 2022, I made it into a private repo on github and now I feel confident enough to release a public version of it.
