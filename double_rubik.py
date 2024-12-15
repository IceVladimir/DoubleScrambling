from rubikencryptor.rubikencryptor import RubikCubeCrypto
from PIL import Image
import os


# Скремблирование с помощью алгоритма рубика
def rubik_encrypt_image(image, encoded_key, output_image):
    input_image = Image.open(image)
    encryptor = RubikCubeCrypto(input_image)
    encrypted_image = encryptor.encrypt(alpha=8, iter_max=10, key_filename=f'key{encoded_key}.txt')
    encrypted_image.save(output_image)


def rubik_decrypt_image(image, encoded_key, output_image):
    input_image = Image.open(image)
    decryptor = RubikCubeCrypto(input_image)
    decrypted_image = decryptor.decrypt(key_filename=f'key{encoded_key}.txt')
    decrypted_image.save(output_image)


def delete_trash():
    if os.path.exists("encrypted_first.png"):
        os.remove("encrypted_first.png")

    if os.path.exists("decrypted_first.png"):
        os.remove("decrypted_first.png")


def main():
    # Шаг 1. Вводим путь до изображения
    image_input = input("Введите путь/название картинки с его расширением: ")

    # Шаг 2. Скремблирование методом рубика дважды
    rubik_encrypt_image(image_input, 1, "encrypted_first.png")
    rubik_encrypt_image("encrypted_first.png", 2, "encrypted_final.png")

    # Шаг 3. Дескремблирование методом рубика дважды
    rubik_decrypt_image("encrypted_final.png", 2, "decrypted_first.png")
    rubik_decrypt_image("decrypted_first.png", 1, "decrypted_final.png")

    # Шаг 4. Удаляем промежуточные файлы
    delete_trash()


if __name__ == "__main__":
    main()