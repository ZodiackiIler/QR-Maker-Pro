# Генератор QR-кода с изображением

Это скрипт на языке Python, который генерирует QR-код с возможностью добавления изображения в центре. Для работы скрипта используются библиотеки `qrcode` и `Pillow` для манипуляции с изображениями.

## Предварительные требования

Перед запуском скрипта убедитесь, что у вас установлены следующие зависимости:

- Python 3.x
- Библиотека qrcode (`pip install qrcode`)
- Библиотека Pillow (`pip install pillow`)

## Использование

1. Клонируйте данный репозиторий или скопируйте код в свою локальную среду разработки.
2. Откройте терминал и перейдите в директорию с файлом скрипта.
3. Выполните следующую команду для запуска скрипта:

```py
python qr_code_maker.py
```

4. При запросе введите необходимую информацию:
- Введите данные для QR-кода.
- Если вы хотите добавить изображение поверх QR-кода, укажите путь к изображению. Нажмите Enter, если не хотите добавлять изображение.
- Укажите путь и имя файла для сохранения QR-кода.

5. Скрипт сгенерирует QR-код и сохранит его в виде изображения по указанному пути.

## Пример

Вот пример использования:

`python qr_code_maker.py`

Введите данные для QR-кода: https://example.com - указывается в файле</br>
Введите путь к изображению (нажмите Enter, чтобы пропустить): image.png - указывается в терминале</br>
Укажите путь и имя файла для сохранения: qr_code.png - указывается в файле</br>

QR-код сохранен в файле: qr_code.png - вывод в консоли

## Лицензия

Этот проект распространяется под [лицензией MIT](LICENSE).
