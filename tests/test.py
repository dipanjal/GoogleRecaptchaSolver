import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from google_captcha_solver import RecaptchaSolver

def main():
    driver = webdriver.Chrome()
    recaptcha_solver = RecaptchaSolver(driver)
    driver.get("https://www.google.com/recaptcha/api2/demo")
    t_start = time.time()
    recaptcha_solver.solve()
    print(f"Time taken to solve the captcha: {time.time()-t_start:.2f} seconds")

    # Submit the form after captcha is solved
    # Ensure you switch back to the default content when needed
    driver.switch_to.default_content()  # Go back to the main document
    submit = driver.find_element(By.ID, "recaptcha-demo-submit")
    submit.click()

    sleep(2)
    driver.quit()

if __name__ == "__main__":
    main()