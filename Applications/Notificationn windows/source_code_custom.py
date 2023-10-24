from plyer import notification

# Configura los detalles de la notificación
title = "Mi Aplicación"
message = "¡Hola desde mi aplicación de Python!"
app_icon = "./Applications/Notificationn windows/python_icon.ico"
app_icon2 = "path/to/your/icon.ico"  # Ruta a un archivo .ico para el icono de la notificación (opcional)
timeout = 10  # Duración de la notificación en segundos

# Muestra la notificación
notification.notify(
    title=title,
    message=message,
    app_icon=app_icon,
    timeout=timeout
)
