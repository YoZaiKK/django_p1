class Carro:
    # detectar la request
    # construir la session
    # construir el carro 
    def __init__(self, request):
        self.request = request #aqui almacenamos la peticion
        self.session = request.session #tenemos iniciada la session
        carro = self.session.get('carro') #aqui identifica el string con el carro
        if not carro:   # Lo creamos, vea
            carro = self.session['carro'] = {} # inicializamos el carro
        else:   # Ps no lo creamos, vea
            self.carro = carro
    def agregar(self, producto): #funcion que agregue los productos al carro
        if(str(producto.id) not in self.carro.key()):
            self.carro[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url,
                
            }