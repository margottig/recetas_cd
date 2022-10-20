from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.recipe_models import  Recipes
from werkzeug.utils import secure_filename
import os

# https://flask-es.readthedocs.io/patterns/fileuploads/
RUTA_DE_MI_APP = "agregar_ruta_absoluta_aqui...../flask_app/static/uploads/"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/crear_receta')
def formulario_receta():
    if 'usuario_id' not in session:
        return redirect('/')
    return render_template('crear_receta.html')


@app.route('/crear_receta', methods=['POST'])
def crear_receta():
# validar si mi formulario contiene un input de nombre imagenreceta
    print(request.files, "QUES ES REQUEST.FILES?")
    if 'imagenreceta' not in request.files:
        flash('No ingresaste una imagen')
        return redirect("/crear_receta")
    file = request.files['imagenreceta']
    print(file, "AQUI ARCHIVO")
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        flash('No has seleccionado una imagen')
        return redirect("/crear_receta")
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        print(filename, "Nombre del archivo")
        print(os.path, "QUE ES OS.PATH???")

        data = {
        "name": request.form['name'],
        "description": request.form['description'],
        "date_made": request.form['date_made'],
        "under": request.form['under'],
        "instruction": request.form['instruction'],
        "nombre_imagen": f"uploads/{filename}",
        "usuario_id": request.form['usuario_id']
        }

        receta_id=Recipes.crear_receta(data)
        file.save(f"{RUTA_DE_MI_APP}{filename}")
       #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect("/welcome")
        
@app.route('/ver/receta/<int:id_receta>')
def ver_receta(id_receta):
    if 'usuario_id' not in session:
        return redirect("/")

    una_receta = Recipes.una_receta({"id_receta":id_receta})
    return render_template("show_recipe.html", una_receta=una_receta)

      
   


   
