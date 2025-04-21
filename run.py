import sys
sys.dont_write_bytecode=True

from garden import app

if __name__ == '__main__':
    app.run(debug=True)
