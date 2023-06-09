

import webbrowser

# Abre la URL en el navegador predeterminado
webbrowser.open_new('http://127.0.0.1:5000')

from flask import Flask, render_template, request

app = Flask(__name__)

# Datos de cotización (aluminio y vidrio)
aluminio = {
    'Pulido': 50700,
    'Lacado Brillante': 54200,
    'Anodizado': 57300,
    'Lacado Mate': 53600,
}

vidrio = {
    'Transparente': 8.25,
    'Azul': 5.2,
    'Bronce': 9.15,
    'Esmerilado': 12.75,
}


ventana = {
    'O': 1,
    'XO': 2,
    'OXO': 3,
    'OXXO': 4,
}



@app.route('/', methods=['GET', 'POST'])
def cotizacion():
    if request.method == 'POST':
        # Obtener datos de formulario
        estilo = request.form['estilo']
        acabado = request.form['acabado']
        vidrio_tipo = request.form['vidrio']
        esmerilado = request.form.get('Esmerilado', False)
        cantidad = int(request.form['cantidad'])

        # Calcular costo de cotización
        costo_aluminio = aluminio[acabado]
        estilo_ventana = ventana[estilo]
        costo_vidrio = vidrio[vidrio_tipo]
        if vidrio_tipo == 'Bronce':
            costo_vidrio = vidrio['Bronce']
        if esmerilado:
            costo_vidrio = vidrio['Esmerilado']
          


        
        # Calculo de medidas y costos
        ancho = float(request.form['ancho'])
        alto = float(request.form['alto'])
        total_medida_ancho = (ancho - 6) * 2
        total_medida_alto = (alto - 6) * 2
        subtotal_aluminio = (total_medida_ancho + total_medida_alto) * (costo_aluminio / 100)
        ancho_vidrio = ancho - 3
        alto_vidrio = alto - 3
        total_vidrio = ancho_vidrio * alto_vidrio
        sub_total_vidrio = total_vidrio * costo_vidrio + 5.2
        total_chapas = 16200 
        total_esquinas = 4 * 4310
        total_ventana = subtotal_aluminio + sub_total_vidrio + total_chapas + total_esquinas
        valor_total=total_ventana * cantidad
        if vidrio_tipo == 'Bronce':
            sub_total_vidrio = total_vidrio * 9.15
        
        if acabado == 'Lacado Mate' and vidrio_tipo == 'Bronce' and cantidad >= 100:
            descuento = (total_ventana * 0.1) * cantidad
            total_ventana -= descuento
 

        
        total_ventana = total_ventana * estilo_ventana

        # Mostrar resultado
        return render_template('resultado.html', estilo=estilo, acabado=acabado,
                               vidrio_tipo=vidrio_tipo, esmerilado=esmerilado,
                               total=total_ventana,
                               cantidad=cantidad, costo_total=valor_total)
    else:
        # Mostrar formulario
        return render_template('formulario.html')


if __name__ == '__main__':
    app.run(debug=True)
    # Abre la URL en el navegador predeterminado
    webbrowser.open_new('http://127.0.0.1:5000')
