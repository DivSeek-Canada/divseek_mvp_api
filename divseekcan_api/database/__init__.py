from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def reset_database():
    from divseekcan_api.database.models import Post, Category, QTL, SNP, Session, Trait  # noqa
    db.drop_all()
    db.create_all()
