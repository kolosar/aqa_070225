reporting

docker run --rm -v %cd%/allure-results:/app/allure-results -v %cd%/allure-report:/app/allure-report frankescobar/allure-docker-service:latest allure generate


Кроки для генерації HTML-звіту з pytest-html:
1. Встановити плагін

pip install pytest-html

2. Запустити тести з параметром --html

pytest --html=report.html

    Це створить файл report.html у поточній директорії.

3. Опціонально: додаткові параметри

    Звіт у папці reports/:

pytest --html=reports/my_test_report.html

Додати назву звіту:

pytest --html=report.html --self-contained-html --title="My Test Report"

Використати --self-contained-html, щоб уникнути зовнішніх ресурсів (CSS/JS у тому ж файлі):

    pytest --html=report.html --self-contained-html

🔍 Приклад структури команди

pytest tests/ --html=reports/test_results.html --self-contained-html

