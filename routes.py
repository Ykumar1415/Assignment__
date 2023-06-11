from flask import jsonify, request
from app import app
from models import db, Task

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    result = []
    for task in tasks:
        task_data = {}
        task_data['id'] = task.id
        task_data['title'] = task.title
        task_data['description'] = task.description
        task_data['due_date'] = task.due_date
        task_data['status'] = task.status
        result.append(task_data)
    return jsonify(result)

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.get(task_id)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    task_data = {
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'due_date': task.due_date,
        'status': task.status
    }
    return jsonify(task_data)

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    due_date = data.get('due_date')
    status = data.get('status', 'Incomplete')
    task = Task(title, description, due_date, status)
    db.session.add(task)
    db.session.commit()
    return jsonify({'message': 'Task created successfully'})

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get(task_id)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    data = request.get_json()
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.due_date = data.get('due_date', task.due_date)
    task.status = data.get('status', task.status)
    db.session.commit()
    return jsonify({'message': 'Task updated successfully'})

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted successfully'})
