from flask import Flask
from flask_cors import CORS
from routes import routes
from db import get_connection

app = Flask(__name__)
CORS(app)

db = get_connection()

def     create_table():
    conn = db
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            completed BOOLEAN DEFAULT FALSE
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

# Call this before app.run()
create_table()

app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)