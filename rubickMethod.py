from rubikencryptor.rubikencryptor import RubikCubeCrypto
from PIL import Image
import os


def rubik_encrypt_image(image, block_size, key_number, encoded_key, output_image):
    input_image = Image.open(image)
    encryptor = RubikCubeCrypto(input_image)
    encrypted_image = encryptor.encrypt(alpha=8, iter_max=10, key_filename=f"{encoded_key}/key{key_number}.txt")
    encrypted_image.save(output_image)


def rubik_decrypt_image(image, block_size, key_number, encoded_key, output_image):
    input_image = Image.open(image)
    decryptor = RubikCubeCrypto(input_image)
    decrypted_image = decryptor.decrypt(key_filename=encoded_key)
    decrypted_image.save(output_image)
