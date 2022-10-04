class operaciones:
    """Esta es una primera descripción de la clase
    """

    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2

    def suma(self):
        """Esta funcion realiza una suma
        """
        return self.op1+self.op2

    def resta(self):
        """Esta funcion realiza una resta
        """
        return self.op1-self.op2


#sphinx-quckstart --ext-autodoc