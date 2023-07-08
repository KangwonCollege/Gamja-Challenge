import configparser

config = configparser.ConfigParser()
print(config.read(r"C:\Users\Mule129\Documents\GitHub\Gamja-Challenge\config\token.ini"))
print(config.sections())
print(config["TOKEN"]["git_token"])