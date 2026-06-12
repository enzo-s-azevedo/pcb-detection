import os
from PIL import Image


def rotate_images(input_folder, output_folder, num_augmentations):
    os.makedirs(output_folder, exist_ok=True)

    angle_step = 360 / num_augmentations

    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tif', '.tiff')

    for filename in os.listdir(input_folder):
        if not filename.lower().endswith(valid_extensions):
            continue

        image_path = os.path.join(input_folder, filename)

        try:
            image = Image.open(image_path)

            name, ext = os.path.splitext(filename)

            for i in range(1, num_augmentations + 1):
                angle = round(i * angle_step)

                rotated = image.rotate(
                    -angle,          # sentido horário
                    expand=True,
                    fillcolor=(0, 0, 0)
                )

                output_name = f"{name}_{angle}{ext}"
                output_path = os.path.join(output_folder, output_name)

                rotated.save(output_path)

            print(f"Processada: {filename}")

        except Exception as e:
            print(f"Erro em {filename}: {e}")


if __name__ == "__main__":
    input_folder = r".\entrada"
    output_folder = r".\Soldagem+DA"

    num_augmentations = 2

    rotate_images(
        input_folder=input_folder,
        output_folder=output_folder,
        num_augmentations=num_augmentations
    )

    print("Concluído!")