from modules.excel import Excel
from modules.browser import Browser
from modules.linkedin import LinkedIn
from time import sleep
from settings import linkedin_email, linkedin_password


# tarayıcıyı çalıştır ve LinkedIn'e giriş yap
driver = Browser().get()

linkedin = LinkedIn(driver)
linkedin.login(linkedin_email, linkedin_password)

sleep(5)