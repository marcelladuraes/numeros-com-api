from sre_constants import SRE_FLAG_UNICODE
from flask import Flask, request

app = Flask(__name__)
# http://127.0.0.1:5000/teste/1
@app.route('/teste/1', methods=['GET', 'POST'])
def teste_dados_formulario_html():

    if request.method == 'POST':
        numero1 = int(request.form.get('numero1'))
        numero2 = int(request.form.get('numero2'))
        numero3 = int(request.form.get('numero3'))

        maior = numero1
        if (numero2 > maior):
            maior = numero2
        if (numero3 > maior):
            maior = numero3
        
        menor = numero1
        if (numero2 < menor):
            menor = numero2
        if (numero3 < menor):
            menor = numero3
        
        media=(numero1+numero2+numero3)/3

        return '''
                <h1>Primeiro número informado: {}</h1>
                <h1>Segundo número informado: {}</h1>
                <h1>Terceiro número informado: {}</h1>
                <h2>Maior número: {}</h2>
                <h2>Menor número: {}</h2>
                <h2>Média dos números: {}</h2>'''.format(numero1, numero2, numero3, maior,menor,media)
    return '''
            <form method="POST">
            <div><label>Informe um número: <input type="number"
            name="numero1"></label></div>
            <div><label>Informe um número: <input type="number"
            name="numero2"></label></div>
            <div><label>Informe um número: <input type="number"
            name="numero3"></label></div>
            <input type="submit" value="Enviar">
            </form>'''

if __name__ == '__main__':
    app.run(debug = True, port = 5000)