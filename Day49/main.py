from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

driver_path = "D:\chromedriver.exe"
driver = webdriver.Chrome(driver_path)

driver.get("https://www.linkedin.com/login?emailAddress=&fromSignIn=&fromSignIn=true&session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fjobs%2Fsearch%2F%3Ff_LF%3Df_AL%26geoId%3D102257491%26keywords%3Dpython%2520developer%26location%3DLondon%252C%2520England%252C%2520United%2520Kingdom%26redirect%3Dfalse%26position%3D1%26pageNum%3D0&trk=public_jobs_nav-header-signin")
username = driver.find_element_by_id("username")
password = driver.find_element_by_name("session_password")

username.send_keys("YOUR EMAIL")
password.send_keys("YOUR PASSWORD")

submit = driver.find_element_by_xpath(
    '//*[@id="organic-div"]/form/div[3]/button')
submit.click()

time.sleep(3)

all_listings = driver.find_elements_by_css_selector(
    ".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    # Try to locate the apply button, if can't locate then skip the job.
    try:
        apply_button = driver.find_element_by_css_selector(
            ".jobs-s-apply button")
        apply_button.click()
        time.sleep(3)

        # If phone field is empty, then fill your phone number.
        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys("9876543210")

        submit_button = driver.find_element_by_css_selector("footer button")

        # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name(
                "artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements_by_class_name(
                "artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        # Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element_by_class_name(
            "artdeco-modal__dismiss")
        close_button.click()

    # If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(3)
