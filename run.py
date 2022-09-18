from app import app
import os

if __name__ == '__main__':
    porta = int(os.getenv('PORT'), '5000')
    app.run(host = '0.0.0.0', port = porta)

