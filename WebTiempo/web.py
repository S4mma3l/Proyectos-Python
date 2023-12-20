from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Lista de proyectos con su tiempo asociado
projects = []

# Ruta principal que muestra la lista de proyectos y tiempo registrado
@app.route('/')
def index():
    return render_template('index.html', projects=projects)

# Ruta para agregar un nuevo proyecto
@app.route('/add_project', methods=['POST'])
def add_project():
    project_name = request.form['project_name']
    start_time = datetime.now()
    projects.append({'name': project_name, 'start_time': start_time})
    return redirect(url_for('index'))

# Ruta para detener el tiempo en un proyecto
@app.route('/stop_time/<int:project_index>')
def stop_time(project_index):
    end_time = datetime.now()
    elapsed_time = end_time - projects[project_index]['start_time']
    projects[project_index]['elapsed_time'] = elapsed_time
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)