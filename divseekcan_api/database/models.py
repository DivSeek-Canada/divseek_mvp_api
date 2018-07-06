# The examples in this file come from the Flask-SQLAlchemy documentation
# For more information take a look at:
# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#simple-relationships

from datetime import datetime

from divseekcan_api.database import db


class QTL(db.Model):
	qtl_id = db.Column(db.Integer(11), primary_key=True)
	qtl_name = db.Column(db.String(255))
	trait_id = db.Column(db.Integer(11), db.ForeignKey('trait.trait_id'))
	locus_id = db.Column(db.Integer(11), db.ForeignKey('locus.locus_id'))
	
	def __init__(self):
		pass
		
class Locus(db.Model):
	locus_id = db.Column(db.Integer(11), primary_key=True)
	base_pair_start = db.Column(db.Integer(11))
	base_pair_end = db.Column(db.Integer(11))
	
	def __init__(self):
		pass
		
class Query(db.Model):
	id = db.Column(db.Integer(11), primary_key=True)
	trait_id = db.Column(db.Integer(11),db.ForeignKey('trait.trait_id'))
	germplasm_id = db.Column(db.Integer(11), db.ForeignKey('germinate_3_4_0.germinatebase.id'))

	def __init__(self):
		pass

class Trait(db.Model):
	trait_id = db.Column(db.Integer(11), primary_key=True)
	trait_name = db.Column(db.String(255))
	trait_type = db.Column(db.String(255))
	trait_description = db.Column(db.String(255))
	
	def __init__(self):
		pass
		
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, title, body, category, pub_date=None):
        self.title = title
        self.body = body
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
        self.category = category

    def __repr__(self):
        return '<Post %r>' % self.title


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name
