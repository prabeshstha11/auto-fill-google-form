from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

CHROME_DRIVER_PATH = '/usr/local/bin/chromedriver'

FORM_URL = 'https://docs.google.com/forms/xxx/viewform'

JAVASCRIPT_CODE = """
// Function to generate a random Nepali name
function generateRandomNepaliName() {
  const firstNames = ["Jimin", "Sumin", "Jiwoo", "Minjun", "Hyunwoo", "Suhyun", "Jaemin", "Youngmin", "Eunwoo", "Sangmin", "Jihyun", "Haneul", "Minji", "Jisoo", "Seungmin", "Hajin", "Dayun", "Yujin", "Seojun", "Doyun"];
  const lastNames = ["Shrestha", "Adhikari", "Rai", "Gurung", "Magar", "Thapa", "Poudel", "Bista", "Malla", "Lama", "Chhetri", "Tamang", "Khadka", "Karki", "Neupane"];
  const firstName = firstNames[Math.floor(Math.random() * firstNames.length)];
  const lastName = lastNames[Math.floor(Math.random() * lastNames.length)];
  return `${firstName} ${lastName}`;
}

// Function to generate a random email address
function generateRandomEmail(name) {
  const domains = ["gmail.com", "yahoo.com", "hotmail.com"];
  const domain = domains[Math.floor(Math.random() * domains.length)];
  const emailName = name.toLowerCase().replace(/\\s+/g, "");
  return `${emailName}${Math.floor(Math.random() * 1000)}@${domain}`;
}

// Randomly select one checkbox from each group
const groups = document.querySelectorAll('[role="radiogroup"]');
groups.forEach((group, groupIndex) => {
  const checkboxes = group.querySelectorAll('[role="radio"]');
  if (checkboxes.length > 0) {
    const randomIndex = Math.floor(Math.random() * checkboxes.length);
    checkboxes[randomIndex].click();
    console.log(`Group ${groupIndex + 1}: Selected checkbox at index ${randomIndex}`);
  } else {
    console.log(`Group ${groupIndex + 1}: No checkboxes found`);
  }
});

// Fill input fields for name and email
// Dynamically identify the first text input field for Name and the next one for Email
const inputFields = document.querySelectorAll('input[type="text"].whsOnd.zHQkBf');

if (inputFields.length >= 2) {
  // Fill the first field (Name)
  const randomName = generateRandomNepaliName();
  inputFields[0].value = randomName;
  const nameInputEvent = new Event('input', { bubbles: true });
  inputFields[0].dispatchEvent(nameInputEvent);
  console.log(`Name input filled: ${randomName}`);

  // Fill the second field (Email)
  const randomEmail = generateRandomEmail(randomName);
  inputFields[1].value = randomEmail;
  const emailInputEvent = new Event('input', { bubbles: true });
  inputFields[1].dispatchEvent(emailInputEvent);
  console.log(`Email input filled: ${randomEmail}`);
} else {
  console.log("Insufficient input fields found for Name and Email!");
}
"""

service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)

driver.get(FORM_URL)

time.sleep(3)

for i in range(100):
    print(f"Submitting form attempt {i + 1}...")

    driver.execute_script(JAVASCRIPT_CODE)
    time.sleep(2)

    submit_button = driver.find_element(By.XPATH, '//div[@role="button" and @aria-label="Submit"]')
    submit_button.click()
    print(f"Form submitted successfully! Attempt {i + 1}")

    time.sleep(2)
    driver.get(FORM_URL) 
    time.sleep(3)

print("Completed all submissions!")

driver.quit()
