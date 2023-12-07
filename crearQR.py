import qrcode

def generar_qr_desde_url(url, nombre_archivo):
    # Crea un objeto QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Agrega la URL al objeto QRCode
    qr.add_data(url)
    qr.make(fit=True)

    # Crea una imagen QR
    imagen_qr = qr.make_image(fill_color="black", back_color="white")

    # Guarda la imagen en un archivo
    imagen_qr.save(nombre_archivo)

if __name__ == "__main__":
    # Ingresa la URL de tu proyecto y el nombre del archivo QR
    url_proyecto = "http://127.0.0.1:8000/gmapsapi/mostrar-mapa/"  # Reemplaza con la URL deseada
    nombre_archivo_qr = "proyecto.png"  # Nombre del archivo QR

    generar_qr_desde_url(url_proyecto, nombre_archivo_qr)
    print(f"Se ha generado el código QR en el archivo: {nombre_archivo_qr}")
