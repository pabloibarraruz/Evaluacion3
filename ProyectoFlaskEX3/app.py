from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def menu_principal():
    return render_template('menu_principal.html')

@app.route('/formulario1', methods=['GET', 'POST'])
def formulario1():
    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        promedio = (nota1 + nota2 + nota3) / 3
        aprobado = promedio >= 40 and asistencia >= 75

        return render_template('formulario1.html', promedio=promedio, aprobado=aprobado)
    return render_template('formulario1.html', promedio=None)

@app.route('/formulario2', methods=['GET', 'POST'])
def formulario2():
    if request.method == 'POST':
        nombres = [
            request.form['nombre1'],
            request.form['nombre2'],
            request.form['nombre3']
        ]

        nombre_mayor = max(nombres, key=len)
        cantidad_caracteres = len(nombre_mayor)

        return render_template('formulario2.html', nombre_mayor=nombre_mayor, cantidad_caracteres=cantidad_caracteres)
    return render_template('formulario2.html')

if __name__ == '__main__':
    app.run(debug=True)
