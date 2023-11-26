from app.md.models.base import College_Data
from app import db
from app.md.serde.base import College_DataSchema
from flask_restful import Resource
from flask import g, request,jsonify

class College_DataView(Resource):
    def get(self):
        data = College_Data.query.all()
        schema_detail = College_DataSchema(many=True)
        return schema_detail.dump(data)
    
    def post(self):
        college_code1 = request.json['college_code1']
        college_name = request.json['college_name']
        city = request.json['city']
        state = request.json['state']
        college_type = request.json['college_type']

        data = College_Data(college_code1=college_code1,college_name=college_name,city=city,state=state,college_type=college_type)
        db.session.add(data)
        db.session.commit()
        return jsonify({"msg":"Data Inserted"})
    
    
class College_Data_crudView(Resource):
    def get(self,id):
        college_detail = College_Data.query.get_or_404(id)
        schema_detail = College_DataSchema()
        return schema_detail.dump(college_detail)
    
    def put(self,id):
        college_detail = College_Data.query.get_or_404(id)
        college_code1 = request.json['college_code1']
        college_name = request.json['college_name']
        city = request.json['city']
        state = request.json['state']
        college_type = request.json['college_type']

    
        college_detail.college_code1=college_code1
        college_detail.college_name=college_name
        college_detail.city=city
        college_detail.state=state
        college_detail.college_type=college_type

        db.session.commit()
        return jsonify({"msg":"Data Updated"})
    
    def delete(self,id):
        college_detail = College_Data.query.get_or_404(id)
        db.session.delete(college_detail)
        db.session.commit()
        return jsonify({"msg":'Data Deleted Successfully'})