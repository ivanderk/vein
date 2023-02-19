import os
from flask import Flask, render_template


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'vein.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    questions = [
        "My enthusiasm regarding the work I do...",
        "The Teamwork atmosphere and communication during the last sprints were...",
        "To what extent the tasks were challenging enough for me...",
        "I would rate my value contributed to the team as follows...",
        "The workload of this/the last sprint was...",
        "I feel supported by the client and stakeholders...",
        "I feel recognized and praised by the team...",
        "I feel inspired and excited to work in this team for the coming sprints..."
    ]

    @app.get("/")
    def home():
        return render_template('index.html', questions=questions)

    @app.get("/login")
    def login():
        return render_template('login.html', questions=questions)

    # a simple page that says hello
    @app.get('/hello')
    def hello():
        return 'Hello, World!'

    return app
