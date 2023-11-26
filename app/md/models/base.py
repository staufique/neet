from app import db 


class College_Data(db.Model):
    __tablename__ = "college_data"
    id = db.Column(db.Integer(),primary_key=True,autoincrement=True)
    college_code1 = db.Column(db.String(200),nullable=False)
    college_name = db.Column(db.String(200),nullable=False)
    city = db.Column(db.String(100),nullable=False)
    state = db.Column(db.String(100),nullable=False)
    college_type = db.Column(db.String(100),nullable=False)
    courses = db.relationship('College_Course', backref='college_data', lazy=True, cascade='all, delete-orphan, delete, save-update')
    cutoff = db.relationship('College_Cutoff', backref='college_data', lazy=True, cascade='all, delete-orphan, delete, save-update')

class College_Course(db.Model):
    __tablename__ = "college_course"
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    college_code2 = db.Column(db.String(200),nullable=False)
    course_name = db.Column(db.String(100), nullable=False) 
    category = db.Column(db.String(100), nullable=False) 
    no_of_seats = db.Column(db.String(100),nullable=False)
    college_id = db.Column(db.Integer(),db.ForeignKey('college_data.id',ondelete='CASCADE', onupdate='CASCADE'))

class College_Cutoff(db.Model):
    __tablename__ = 'college_cutoff'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    college_code3 = db.Column(db.String(200),nullable=False)
    course_name = db.Column(db.String(100), nullable=False) 
    category = db.Column(db.String(100), nullable=False)
    rank_high = db.Column(db.String(100),nullable=True)
    rank_low = db.Column(db.String(100),nullable=True)
    marks_high = db.Column(db.String(100),nullable=True)
    marks_low = db.Column(db.String(100),nullable=True)
    period = db.Column(db.String(100),nullable=False)
    college_id = db.Column(db.Integer(),db.ForeignKey('college_data.id',ondelete='CASCADE', onupdate='CASCADE'))

