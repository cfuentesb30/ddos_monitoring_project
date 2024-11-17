from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import os
import json
from simulador_ddos import start_ddos_attack  # Asegúrate de que esta función esté definida en simulador_ddos.py

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Usuario y contraseña de ejemplo
users = {'admin': 'password'}

@app.route('/')
def home():
    if 'username' in session:
        return render_template('index.html')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return 'Credenciales incorrectas. Intente de nuevo.'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/data')
def data():
    # Simulación de datos para el gráfico
    cpu_usage = 50  # Reemplaza con el código real para obtener el uso de CPU
    memory_usage = 70  # Reemplaza con el código real para obtener el uso de memoria
    traffic = 120  # Reemplaza con el código real para obtener tráfico de red
    return jsonify(cpu=cpu_usage, memory=memory_usage, traffic=traffic)

@app.route('/metrics')
def metrics():
    """Obtiene las métricas registradas del archivo JSON."""
    try:
        with open('metrics_log.json', 'r') as log_file:
            metrics_data = log_file.readlines()
        return jsonify([json.loads(line) for line in metrics_data])
    except FileNotFoundError:
        return jsonify([])

@app.route('/attack', methods=['POST'])
def attack():
    ip_address = request.form.get('ip_address')
    if ip_address:
        start_ddos_attack(ip_address)  # Llama a la función para iniciar el ataque DDoS
        return jsonify(success=True, message="Ataque DDoS iniciado.")
    return jsonify(success=False, message="Dirección IP no válida.")

if __name__ == '__main__':
    app.run(debug=True)
