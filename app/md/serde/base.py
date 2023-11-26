from marshmallow import Schema,fields

class College_DataSchema(Schema):
    id = fields.Int(dump_only=True)
    college_code1 = fields.Str()
    college_name = fields.Str()
    city = fields.Str()
    state = fields.Str()
    college_type = fields.Str()
    # courses = fields.Nested("college_course",only=("name","id"), dump_only=True)
    # cutoff = fields.Nested("college_cutoff",only=("name","id"), dump_only=True)
    # fields = ["id","college_code1","college_name","city","state","college_type"]

class College_CourseSchema(Schema):
    id = fields.Int(dump_only=True)
    college_code2 = fields.Str()
    course_name = fields.Str()
    category = fields.Str()
    no_of_seats = fields.Str()
    college_id = fields.Int()
    
    # fields = ["id","college_code2","course_name","category","no_of_seats","college_id"]

class College_CutoffSchema(Schema):
    id = fields.Int(dump_only=True)
    college_code3 = fields.Str()
    category = fields.Str()
    rank_high = fields.Str()
    rank_low = fields.Str()
    marks_high = fields.Str()
    marks_low = fields.Str()
    period = fields.Str()
    college_id = fields.Int()
    # fields = ["id","college_code3","course_name","category","rank_high","rank_low","marks_high","marks_low","period","college_id"]
