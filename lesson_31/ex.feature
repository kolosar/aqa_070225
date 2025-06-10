Тест один
    КОЛИ Відкрити УРЛ (лінк)
    ТОДІ Заповни поле (назва поля)
    І  Заповни поле (назва поля)
    ОЧІКЄТСЬЯ Кнопка (назва кнопки) клікабельна

Scenario: Successful login with valid credentials
    Given the user is on the login page
    When the user enters valid credentials
    And clicks the login button
    Then the user should be redirected to the dashboard