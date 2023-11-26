from app.md.models.base import College_Cutoff
from app import db
from app.md.serde.base import College_CutoffSchema
from flask_restful import Resource
from flask import g, request,jsonify

class College_CutoffView(Resource):
    def get(self):
        data = College_Cutoff.query.all()
        schema_detail = College_CutoffSchema(many=True)
        return schema_detail.dump(data)
    
    def post(self):
        college_code3=request.json['college_code3']
        course_name=request.json['course_name']
        category=request.json['category']
        rank_high=request.json['rank_high']
        rank_low=request.json['rank_low']
        marks_high=request.json['marks_high']
        marks_low=request.json['marks_low']
        period=request.json['period']

        data = College_Cutoff(college_code3=college_code3,course_name=course_name,category=category,rank_high=rank_high,rank_low=rank_low,marks_high=marks_high,marks_low=marks_low,period=period)
        db.session.add(data)
        db.session.commit()
        return jsonify({"msg":"Data Inserted"})

class College_Cutoff_crudView(Resource):
    def get(self,id):
        college_detail = College_Cutoff.query.get_or_404(id)
        schema_detail = College_CutoffSchema()
        return schema_detail.dump(college_detail)
    
    def put(self,id):
        college_detail = College_Cutoff.query.get_or_404(id)
        college_code3=request.json['college_code3']
        course_name=request.json['course_name']
        category=request.json['category']
        rank_high=request.json['rank_high']
        rank_low=request.json['rank_low']
        marks_high=request.json['marks_high']
        marks_low=request.json['marks_low']
        period=request.json['period']
      
        college_detail.college_code3=college_code3
        college_detail.course_name=course_name
        college_detail.category=category
        college_detail.rank_high=rank_high
        college_detail.rank_low=rank_low
        college_detail.marks_high=marks_high
        college_detail.marks_low=marks_low
        college_detail.period=period

        db.session.commit()
        return jsonify({"msg":"Data Updated"})

    def delete(self,id):
        college_detail = College_Cutoff.query.get_or_404(id)
        db.session.delete(college_detail)
        db.session.commit()
        return jsonify({"msg":'Data Deleted Successfully'})