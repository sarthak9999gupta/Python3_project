# Encode and Decode QR Code Python Script

This script allows you to generate and decode QR codes using Python. It uses the `qrcode` and `cv2` (OpenCV) libraries to perform these operations.

## Prerequisites

- Python 3.x
- Required packages: `qrcode`, `opencv-python` (install using `pip install qrcode opencv-python`)

## Usage

1. Clone or download the repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory containing the script.

3. Run the script using the following command:
   
   ```sh
   python script.py
   ```

4. The script will present you with two options:
   - Enter `1` to encode a QR code.
   - Enter `2` to decode a QR code.

### Encode QR Code

If you choose to encode a QR code:
1. Enter a valid URL or data that you want to encode.
2. You will be asked if you want to customize the QR code colors.
   - Enter `1` to customize the colors.
   - Enter anything else to use the default colors.
3. If you chose to customize the colors:
   - Enter the background color (e.g., `"white"`, `"red"`, `"blue"`).
   - Enter the foreground (QR code pattern) color (e.g., `"black"`, `"green"`, `"purple"`).
4. The script will generate the QR code and save it as `Qrcode.png`.

### Decode QR Code

If you choose to decode a QR code:
1. Enter the name of the image file containing the QR code (e.g., `"Qrcode.png"`).
2. The script will use OpenCV to read the image and decode the QR code.
3. The decoded data will be displayed on the console.

## Author

This script was created by sarthakgupta. You can find the original source code and contact the author on GitHub [here](https://github.com/sarthakgupta9891/qr-code-generator-decoder).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
Make sure to replace `"script.py"` with the actual name of your Python script. Also, modify the GitHub repository link, author name, and other details as needed.
