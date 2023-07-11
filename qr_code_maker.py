# Импортируем библиотеки
import qrcode
from PIL import Image
import os

def generate_qr_code_with_image(data, image_path, output_path):
    # Создание объекта QRCode с параметрами QR-кода
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    # Добавление данных в QR-код
    qr.add_data(data)
    # Создание QR-кода
    qr.make(fit=True)

    # Создаем изображение QR-кода
    # fill_color - цвет линий qrcode
    # back_color - задний фон qrcode
    qr_image = qr.make_image(fill_color="black", back_color="white")

    # Добавляем изображение в QR-код, если image_path не пусто
    if image_path:
        # Открываем изображение, которое вы хотите добавить в QR-код
        overlay_image = Image.open(image_path)

        # Расчитываем размер и позиции изображения на QR-коде
        qr_width, qr_height = qr_image.size
        overlay_width, overlay_height = overlay_image.size
        overlay_size = min(qr_width, qr_height) // 4

        overlay_image = overlay_image.resize((overlay_size, overlay_size))

        position = ((qr_width - overlay_size) // 2, (qr_height - overlay_size) // 2)

        # Добавляем изображение в QR-код
        qr_image.paste(overlay_image, position)

    # Генерируем уникальное имя файла, если файл уже существует
    base_path, ext = os.path.splitext(output_path)
    count = 1
    while os.path.exists(output_path):
        output_path = f"{base_path}_{count}{ext}"
        count += 1

    # Сохраняем QR-код с добавленным изображением или без него
    qr_image.save(output_path)

# Пример использования:
data = "Строка1\nСтрока2\nСтрока3"
image_path = input("Введите путь к изображению (если нет, нажмите Enter): ")
output_path = "qr_code.png"

generate_qr_code_with_image(data, image_path, output_path)
print(f"QR-код был сохранен в файл: {output_path}")
