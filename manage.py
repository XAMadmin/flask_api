from flask_script import Manager
from MindxServer import create_app

# 创建app应用
app = create_app("product")

manager = Manager(app)

if __name__ == "__main__":
    manager.run()