import logging
import os
from datetime import datetime
from http import HTTPStatus

from flask import Flask, request, session, jsonify, Response, send_file
from docx import Document
from werkzeug.datastructures.file_storage import FileStorage

from utils.helper import LLMHelper
from utils.document_generation import create_documentation

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

api_base = "/api"


@app.route(api_base)
def index():
    session.clear()
    return 'Backend is running'


@app.route(f'{api_base}/neo4j_healthcheck', methods=['GET'])
def neo4j_healthcheck():
    llm_helper = LLMHelper()
    try:
        llm_helper.get_connection_neo4j()
        return jsonify(status="ok", description="Neo4j is running!"), HTTPStatus.MULTI_STATUS
    except Exception as e:
        return jsonify(
            status="ko",
            description="Neo4j is not running"
        ), 404


@app.route(f'{api_base}/clear_session')
def clear_session():
    session.clear()
    return 'Session cleared'


@app.route(f'{api_base}/set_session_data')
def set_session_data():
    session['chat_history'] = []
    session['chat_askedquestion'] = ''
    session['chat_question'] = ''
    session['chat_followup_questions'] = []
    session['data_files_embeddings'] = []
    return 'Session data set'


@app.route(f'{api_base}/downloading', methods=['POST'])
def download_docx_file() -> Response:
    """
    Download the text into the Downloads folder
    :return: Return the download
    :rtype: Response
    """
    try:

        explanation = request.form['explanation']
        document = Document()
        document.add_paragraph(explanation)
        chemin_telechargement = os.path.join(os.path.expanduser('~'), 'Downloads')

        document.save(chemin_telechargement + '/' + 'documentation.docx')

        return jsonify({'explanation': 'Documment Created'})
    except Exception as e:
        logging.error(f"Error generating code: {e}")


@app.route(f'{api_base}/explain_application', methods=['POST'])
def explanation_with_graph():
    """
    Explain project with graph approach
    :return: Return explanation
    :rtype: Response
    """
    try:
        information = []
        input_code = request.files.getlist('files')
        explanation = request.form['difficulty']
        llm_helper = LLMHelper()

        for code in input_code:
            fichier = FileStorage(code)
            information.append(fichier.read().decode('utf-8'))

        main_explanation, function_explanation_functional = llm_helper.explaining_project(information, explanation)

        if main_explanation and function_explanation_functional:
            file_path = create_documentation(main_explanation, function_explanation_functional)
            now = datetime.now()
            formatted_time = now.strftime("%d_%m_%Y_%H_%M")
            file_name = f"documentation_{formatted_time}.docx"

            return send_file(file_path, as_attachment=True, download_name=file_name)

    except Exception as e:
        logging.error(f"Error explaining code: {e}")


@app.route(f'{api_base}/chat', methods=['POST'])
def info_functions():
    try:
        print("hello")
        # Initialize chat history
        if 'chat_question' not in session:
            session['chat_question'] = ''
        if 'chat_askedquestion' not in session:
            session.chat_askedquestion = ''
        if 'chat_history' not in session:
            session['chat_history'] = []
        if 'chat_followup_questions' not in session:
            session['chat_followup_questions'] = []
        if 'input_message_key' not in session:
            session['input_message_key'] = 1
        llm_helper = LLMHelper()

        session['chat_question'] = request.json.get('question', '')

        result = llm_helper.get_function_details(session['chat_question'], session['chat_history'])
        return jsonify({'answer': result})

    except Exception as e:
        logging.error(f"Error explaining code: {e}")


if __name__ == '__main__':
    app.run()
