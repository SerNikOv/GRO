# Autotrader
Регистрация бота в телеге

Заходим на сайт телеграма: https://my.telegram.org
Вводим телефон и ждем код подтверждения на родном клиенте телеграма. Он довольно длинный (12 символов) и неудобный для ввода.


Заходим в пункт "API". Ищем "Telegram API" и заходим в "Creating an application" (https://my.telegram.org/apps).


Заполняем поля App title и Short name, нажимаем «Create application» и запоминаем две переменные: api_id и api_hash

# Создание чат-бота в Телеграме
Перейдите в диалог с инструментом для разработки чатов — https://telegram.me/BotFather.
Нажмите кнопку «Start» или введите в диалоге команду /start.
Далее введите команду /newbot, чтобы сделать новый бот.
Укажите название — как будет отображаться чат в списке контактов.
Последнее — системное имя: это то, что будет ником после знака @.
Название может быть любым: нестрашно, если оно будет дублировать уже существующие. Но системное имя обязательно должно быть уникальным. Если имя уже занято, вы увидите подсказку: «Sorry, this username is already taken. Please try something different».

После успешного создания вы получите токен. Сохраните его, он понадобится для дальнейшей интеграции. Если вы закрыли окно и нужно снова найти токен, напишите в диалоге команду /token