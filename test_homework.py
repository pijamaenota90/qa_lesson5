from selene import browser, have, be
import os

def test_form():
    browser.open('/automation-practice-form')

    # Заполнение формы
    browser.element('#firstName').should(be.blank).type('Alex')
    browser.element('#lastName').should(be.blank).type('Alexov')
    browser.element('#userEmail').should(be.blank).type('alex.alexov@mail.ru')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').should(be.blank).type('1234567890')

    # Выбор даты рождения
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select option[value="11"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select option[value="1990"]').click()
    browser.element('.react-datepicker__day--026').click()
    # Выбор
    browser.element('#subjectsInput').type('History').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').type(os.path.abspath('files/test.jpg'))
    browser.element('#currentAddress').should(be.blank).type('address')

    # Выбор штата и города
    browser.element('#state').click()
    browser.element('//div[@id="state"]//div[text()="NCR"]').click()
    browser.element('#city').click()
    browser.element('//div[@id="city"]//div[text()="Delhi"]').click()

    # Подтверждение формы
    browser.element('#submit').click()

    # Проверка вывода
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    # Проверка заполненных данных
    browser.all('tbody tr td:last-child').should(have.texts(
        'Alex Alexov',
        'alex.alexov@mail.ru',
        'Male',
        '1234567890',
        '26 November,1990',
        'History',
        'Reading',
        'test.jpg',
        'address',
        'NCR Delhi'
    ))