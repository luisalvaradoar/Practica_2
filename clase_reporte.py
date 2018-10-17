import subprocess

class MiReporte():
    def __init__(self, nombre):
        self.nombre = nombre + '.tex'
        self.archivo = open(self.nombre, 'w')
        self.contador = 1

    def iniciarReporte(self):
        #self.archivo.write("\\documentclass{report} \n")
        self.archivo.write("\\documentclass{standalone} \n")
        self.archivo.write("\\begin{document} \n")

    def terminarReporte(self):
        self.archivo.write("\n")
        self.archivo.write("\\end{document} \n")
        self.archivo.close()

    def iniciarTabla(self):
        self.archivo.write("\\begin{tabular}{|c|c|c|c|} \n")
        self.archivo.write("\\hline \n")
        self.archivo.write("No. Jugada & Poste seleccionado & Disco seleccionado & Poste llegada \\\\ \n")
        self.archivo.write("\\hline \n")

    def terminarTabla(self):
        self.archivo.write("\\end{tabular}\n")

    def escribirFila(self, triada):
        self.archivo.write("{} & {} & {} & {} \\\\ \n".format(self.contador, triada[0], triada[2], triada[1]))
        self.archivo.write("\\hline \n")
        self.contador += 1

    def compilarReporte(self):
        subprocess.call(["pdflatex", self.nombre])
        subprocess.call(["rm", self.nombre.replace('.tex', '.log'), self.nombre.replace('.tex', '.aux')])
        #subprocess.call(["zip", "reporte.zip", self.nombre, self.nombre.replace('.tex', '.pdf')])
        subprocess.call(["rm", self.nombre])
    
    def getNombre(self):
        return self.nombre