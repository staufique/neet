from flask import Blueprint
from flask_restful import Api

from app.md.controllers.base import College_Data_UploadView
md_blueprint = Blueprint("md_blueprint", __name__, url_prefix="/md")
api = Api(md_blueprint)
from app.md.controllers.college_data import College_DataView,College_Data_crudView
from app.md.controllers.college_course import College_CourseView,College_Course_crudView
from app.md.controllers.college_cutoff import College_CutoffView,College_Cutoff_crudView


# http://127.0.0.1:5000/api/md/college-data-upload/
api.add_resource(College_Data_UploadView, "/college-data-upload/")

api.add_resource(College_DataView, "/college-data")
api.add_resource(College_Data_crudView, "/college-data/<int:id>")

api.add_resource(College_CourseView, "/college-course")
api.add_resource(College_Course_crudView, "/college-course/<int:id>")

api.add_resource(College_CutoffView, "/college-cutoff")
api.add_resource(College_Cutoff_crudView, "/college-cutoff/<int:id>")