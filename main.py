import os
from gooey import Gooey, GooeyParser
from PIL import Image


@Gooey
def convert_ico_to_png():
    parser = GooeyParser()
    parser.add_argument("current_dir", action="store", help="Your directory to the images.", widget="DirChooser")
    parser.add_argument("from_format", action="store", help="The initial format you want to convert from. for example: ico")
    parser.add_argument("to_format", action="store", help="The initial format you want to convert to. for example: png")
    # current_dir = input("Enter the path to your folder with .ico files \n Example: M:\Windows 7 Icons \n Your path: ")
    # from_format = input("Enter the ORIGINAL FILES format. Example: ico \n WRITE VALID FORMATS AND ok. ")
    # to_format = input("Enter the format you want your pictures to be converted to. EXAMPLE: png. \n Go ahead: ")
    args = parser.parse_args()
    current_dir = args.current_dir
    from_format = args.from_format
    to_format = args.to_format
    
    from_format = from_format.replace(".", "")
    to_format = to_format.replace(".","")
    # os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(current_dir, f"converted_to_{to_format.lower()}_v1")
    if not os.path.exists(output_dir):
        print("Path doesnt exist! Creating...")
        os.makedirs(output_dir)
        print("Created! Continuing...")
    converted_c = 0

    for file in os.listdir(current_dir):
        if file.lower().endswith(f'.{from_format.lower()}'):
            icop = os.path.join(current_dir, file)

            try:
                with Image.open(icop) as img:
                    sizes = img.info.get('sizes')
                    if sizes:
                        largest_size = max(sizes, key=lambda s: s[0] * s[1])
                        img.size = largest_size
                    base_name = os.path.splitext(file)[0]
                    output_path = os.path.join(output_dir, f"{base_name}.{to_format}")
                    formatte = to_format.upper()
                    if formatte == "JPG" or formatte == "JPEG":
                        formatte = "JPEG"
                        img_rgb = img.convert("RGB")
                        img_rgb.save(output_path, format=f"{formatte}", quality=95)
                    else:
                        if formatte == "ICON" or formatte == "ICONE":
                            formatte = "ICO"
                            output_path = os.path.join(output_dir, f"{base_name}.ico")
                        img.save(output_path, format=f"{formatte}")
                    print(f"Succesful: {file} = {base_name}.{to_format}")
                    converted_c += 1
            except Exception as e:
                print(f"error... {file} is faulty: {e}")
    print(f"\n All done! Conveted files: {converted_c}")
    if formatte == "JPEG":
        print(" \n Warning: jpg doesn't support alpha channel. incase you dont know heh \n")
    print(f"Your files were saved to {output_dir}!")
    print("Have a great day!!!!")

if __name__ == "__main__":
    convert_ico_to_png()