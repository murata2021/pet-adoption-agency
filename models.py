from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()


def connect_db(app):
    db.app=app
    db.init_app(app)


#MODELS GO BELOW!

class Pet(db.Model):
    """Pets."""

    __tablename__='pets'

    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.Text,nullable=False)
    species=db.Column(db.Text,nullable=False)
    photo_url=db.Column(db.Text)
    age=db.Column(db.Integer)
    notes=db.Column(db.Text)
    available=db.Column(db.Boolean,nullable=False,default=True)


    def __repr__(self):
        p=self
        return f"<Pets {p.id} {p.name} {p.species} {p.photo_url} {p.age} {p.notes} {p.available}>"


# class Employee(db.Model):
#     """Employee Model"""

#     __tablename__='employees'

#     id=db.Column(db.Integer,primary_key=True,autoincrement=True)
#     name=db.Column(db.Text,nullable=False,unique=True)
#     state=db.Column(db.Text,nullable=False,default='CA')
#     dept_code=db.Column(db.Text,db.ForeignKey('departments.dept_code'))

#     dept=db.relationship('Department',backref='employees') ##It creates a dept attribute for Employee, we don't need to join anything

    


#     #this one allows us to skip middle table and we can directly reach to final table
#     #but we cannot reach any info about the middle table, 
#     #that's why we may want to keep a relationship with middle table look at the assignments rel. below
#     projects=db.relationship("Project",secondary='employees_projects',backref='employees',passive_deletes=True)
#     # assignments=db.relationship('EmployeeProject',backref='employee')




#     def __repr__(self):
#         return f"<Employee {self.id} {self.name} {self.state} {self.dept_code}>"


# def get_directory():
#     """Show phone dir of emps & their departments"""

#     # emps=Employee.query.all()   

#     # for emp in emps:
#     #     if emp.dept is not None:
#     #         print(emp.name,emp.dept.dept_code,emp.dept.phone)
#     #     else:
#     #         print(emp.name,"","")

#     #more efficient way is using join instead of setting a relationship via sql alchemy

#     emps=db.session.query(Employee.name,Department.dept_code,Department.phone).join(Department,isouter=True).all()

#     for (x,y,z) in emps:
#         if x is not None:
#             print(x,y,z)
#         else:
#             print(x,"","")


# class Project(db.Model):
#     """Project."""

#     __tablename__='projects'

#     proj_code=db.Column(db.Text,primary_key=True)
#     proj_name=db.Column(db.Text,nullable=False,unique=True)

#     #There is one-to-many relationship between a department and employees. One department can have more than one employees. But in general (most of the time) an employee has just one department.

#     # employees=db.relationship('Employee')

#     def __repr__(self):
#         return f"<Project {self.proj_code} {self.proj_name}>"
    
#     #direct navigation:project ->employeeproject & back

#     assignments=db.relationship('EmployeeProject',backref='project')


# class EmployeeProject(db.Model):
#     """A project can have more than one employees.And an employee can have more than one projects"""

#     __tablename__='employees_projects'

#     emp_id=db.Column(db.Integer,db.ForeignKey('employees.id',ondelete='CASCADE'),primary_key=True)
#     proj_code=db.Column(db.Text,db.ForeignKey('projects.proj_code'),primary_key=True)
#     role=db.Column(db.Text)

#     def __repr__(self):
#         return f"<EmployeeProject {self.emp_id} {self.proj_code} {self.role}>" 