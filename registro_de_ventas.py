from main import ventas
def registro_de_ventas (nombre, precio, cantidad):
    ventas.append(
        {
           "producto":nombre,
           "precio"  :precio,
           "cantidad":cantidad 
        }
        
    )
    return ventas