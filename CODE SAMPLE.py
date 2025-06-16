from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)

# Simulated database of tasks
tasks = [
    {"id": 1, "title": "Finish application", "completed": False, "timestamp": "2024-06-16 10:00:00"},
    {"id": 2, "title": "Push code to GitHub", "completed": True, "timestamp": "2024-06-15 18:30:00"}
]

def get_timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify({"tasks": tasks}), 200

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    if not data or not data.get("title"):
        return jsonify({"error": "Title is required."}), 400

    new_task = {
        "id": tasks[-1]["id"] + 1 if tasks else 1,
        "title": data["title"],
        "completed": False,
        "timestamp": get_timestamp()
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = data.get("title", task["title"])
            task["completed"] = data.get("completed", task["completed"])
            return jsonify(task), 200
    return jsonify({"error": "Task not found."}), 404

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return jsonify({"message": f"Task {task_id} deleted."}), 200

if __name__ == "__main__":
    app.run(debug=True)
