# web_interface.py

from flask import Flask, request, jsonify
from utilities import logger
from ui import UserInterface

app = Flask(__name__)
ui = UserInterface()

@app.route('/')
def home():
    return "Welcome to our advanced AI development ecosystem!"

@app.route('/assistant', methods=['POST'])
def create_assistant():
    characteristics = request.json.get('characteristics', {})
    ui.create_assistant(characteristics)
    return jsonify({"message": f"Assistant created with characteristics: {characteristics}"}), 201

@app.route('/thread', methods=['POST'])
def create_thread():
    initial_message = request.json.get('initial_message', '')
    ui.create_thread(initial_message)
    return jsonify({"message": f"Thread created with initial message: {initial_message}"}), 201

@app.route('/run', methods=['POST'])
def create_run():
    assistant = ui.assistant
    thread = ui.thread
    ui.create_run(assistant, thread)
    return jsonify({"message": "Run created with selected Assistant on a Thread."}), 201

@app.route('/run_step', methods=['POST'])
def create_run_step():
    run = ui.run
    step = request.json.get('step', '')
    ui.create_run_step(run, step)
    return jsonify({"message": f"Run step created with step: {step}"}), 201

@app.errorhandler(500)
def server_error(e):
    logger.error(f"An error occurred during a request. {e}")
    return jsonify({"message": "An internal error occurred."}), 500

if __name__ == '__main__':
    app.run(debug=True)