from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Pitch,Category,Comment,Votes
from flask_migrate import Migrate,MigrateCommand

#creating app instance

app = create_app("development")

manager = Manager(app)
manager.add_command("server",Server)

migrate = Migrate(app,db)
manager.add_command("db",MigrateCommand)
@manager.shell
def make_shell_context():
    return dict(app=app,db=db,User=User,Pitch=Pitch,Category=Category,Votes=Votes,Comment=Comment)
    
if __name__ == "__main__":
    manager.run()