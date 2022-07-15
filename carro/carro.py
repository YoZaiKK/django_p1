class Carro:
    # detectar la request
    # construir la session
    # construir el carro
    
    def guardar_carro(self):
        self.session['carro'] = self.carro
        self.session.modified = True
        
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get('carro')
        if not carro:  # Lo creamos, vea
            carro = self.session['carro'] = {}  # inicializamos el carro
        else:  # Ps no lo creamos, vea
            self.carro = carro

    def agregar(self, producto):  #funcion que agregue los productos al carro
        if (str(producto.id) not in self.carro.key()):
            self.carro[producto.id] = {
                'producto_id': producto.id,
                'nombre': producto.nombre,
                'precio': str(producto.precio),
                'cantidad': 1,
                'imagen': producto.imagen.url,
            }
        else:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value['cantidad'] = value['cantidad'] + 1
                    break
        self.guardar_carro()


    def eliminar(self, producto):
        producto.id = str(producto.id)
        if producto.id in self.carro.key():
            del self.carro[producto.id]
            self.guardar_carro()

    def restar(self, producto):
        for key, value in self.carro.items():
            if key == str(producto.id):
                value['cantidad'] = value['cantidad'] - 1
                if value['cantidad'] < 1:
                    self.eliminar(producto)
                break
        self.guardar_carro()

    def vaciar(self):
        self.session['carro'] = {}
        self.session.modified = True