from app.md.models.base import College_Course
from app import db
from app.md.serde.base import College_CourseSchema
from flask_restful import Resource
from flask import g, request,jsonify

class College_CourseView(Resource):
    def get(self):
        data = College_Course.query.all()
        schema_detail = College_CourseSchema(many=True)
        return schema_detail.dump(data)
    
    def post(self):
        college_code2= request.json['college_code2']
        course_name=request.json['course_name']
        category=request.json['category']
        no_of_seats=request.json['no_of_seats']

        data = College_Course(college_code2=college_code2,course_name=course_name,category=category,no_of_seats=no_of_seats)
        db.session.add(data)
        db.session.commit()
        return jsonify({"msg":"Data Inserted"})
    
class College_Course_crudView(Resource):
    def get(self,id):
        college_detail = College_Course.query.get_or_404(id)
        schema_detail = College_CourseSchema()
        return schema_detail.dump(college_detail)

    def put(self,id):
        college_detail = College_Course.query.get_or_404(id)
        college_code2= request.json['college_code2']
        course_name=request.json['course_name']
        category=request.json['category']
        no_of_seats=request.json['no_of_seats']

        college_detail.college_code2=college_code2
        college_detail.course_name=course_name
        college_detail.category=category
        college_detail.no_of_seats=no_of_seats
        db.session.commit()
        return jsonify({"msg":"Data Updated"})

    def delete(self,id):
        college_detail = College_Course.query.get_or_404(id)
        db.session.delete(college_detail)
        db.session.commit()
        return jsonify({"msg":'Data Deleted Successfully'})
    
