################# Imorts de Flask & Python #################
from flask import render_template, request, Blueprint, redirect, url_for, flash

from .forms import NewProjectForm, UpdateProjectForm
from .image_handler import add_image
from db.db_connection import get_connection

project_blueprint = Blueprint('project', __name__)

#### localhost:5000/project/list ####
#### localhost:5000/project/34 ####
#### localhost:5000/project/new ####
#### localhost:5000/project/34/edit ####
#### localhost:5000/project/34/delete ####

################### List Projects #################
@project_blueprint.route('/list')
def list():
    conn = get_connection()
    with conn.cursor() as cursor:
        sql = "SELECT * FROM project"
        cursor.execute(sql)
        projects = cursor.fetchall()
    return render_template('project/list.html', projects=projects)

################### Show Project #################
@project_blueprint.route('/<project_id>')
def show(project_id):
    conn = get_connection()
    with conn.cursor() as cursor:
        sql = f"SELECT * FROM project WHERE id = {project_id}"
        cursor.execute(sql)
        project = cursor.fetchone()
    return render_template('project/show.html', project=project)

################### Create New Project #################
@project_blueprint.route('/new', methods=['GET', 'POST'])
def new():
    form = NewProjectForm()

    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        url = form.url.data
        image = add_image(form.image.data)

        conn = get_connection()
        with conn.cursor() as cursor:
            sql = "INSERT INTO project (name, description, url, image) "
            sql += f"VALUES ('{name}', '{description}', '{url}', '{image}')"
            cursor.execute(sql)
            conn.commit()
            flash('Proyecto creado correctamente')
            return redirect(url_for('project.list'))

    return render_template('project/new.html', form=form)

################### Update a Project #################
@project_blueprint.route('/<project_id>/edit', methods=['GET', 'POST'])
def edit(project_id):
    if request.method == 'GET':
        conn = get_connection()
        with conn.cursor() as cursor:
            sql = f"SELECT * FROM project WHERE id = {project_id}"
            cursor.execute(sql)
            project = cursor.fetchone()

        form = UpdateProjectForm()
        form.name.data = project['name']
        form.description.data = project['description']
        form.url.data = project['url']
        image = project['image']
        
        return render_template('project/new.html', form=form, image=image)
    if request.method == 'POST':

        form = UpdateProjectForm()

        if form.validate_on_submit():
            name = form.name.data
            description = form.description.data
            url = form.url.data
            if form.image.data:
                image = add_image(form.image.data)
                sql = f"UPDATE project SET name = '{name}', description = '{description}'," 
                sql += f"url = '{url}', image = '{image}' WHERE id = {project_id}"
            else:
                sql = f"UPDATE project SET name = '{name}', description = '{description}'," 
                sql += f"url = '{url}' WHERE id = {project_id}"
            
            conn = get_connection()
            with conn.cursor() as cursor:
                cursor.execute(sql)
                conn.commit()
                flash('Proyecto actualizado correctamente')
                return redirect(url_for('project.list'))

################### Delete a Project #################
@project_blueprint.route('/<project_id>/delete', methods=['POST'])
def delete(project_id):
    conn = get_connection()
    with conn.cursor() as cursor:
        sql = f"DELETE FROM project WHERE id = {project_id}"
        cursor.execute(sql)
        conn.commit()
        flash('Proyecto eliminado correctamente')
        return redirect(url_for('project.list'))


