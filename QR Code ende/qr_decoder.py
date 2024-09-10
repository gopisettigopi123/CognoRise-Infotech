import cv2

def decode_qr(image_path):
    img = cv2.imread(image_path)
    detector = cv2.QRCodeDetector()
    data, vertices_array, _ = detector.detectAndDecode(img)
    if vertices_array is not None:
        print(f"Decoded data: {data}")
    else:
        print("No QR code found")

# Example usage
image_path = "qrcode.png"
decode_qr(image_path)
