from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    student_name = Column(String)

    grades = relationship('Grade', back_populates='student')
    groups = relationship('Group', secondary='student_groups', back_populates='students')

class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    group_name = Column(String)

    students = relationship('Student', secondary='student_groups', back_populates='groups')

class StudentGroup(Base):
    __tablename__ = 'student_groups'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    group_id = Column(Integer, ForeignKey('groups.id'), primary_key=True)

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    teacher_name = Column(String)

    subjects = relationship('Subject', back_populates='teacher')

class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True)
    subject_name = Column(String)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))

    teacher = relationship('Teacher', back_populates='subjects')
    grades = relationship('Grade', back_populates='subject')

class Grade(Base):
    __tablename__ = 'grades'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    grade = Column(Integer)
    date_received = Column(Date)

    student = relationship('Student', back_populates='grades')
    subject = relationship('Subject', back_populates='grades')

# Підключення до бази даних
db_url = 'postgresql+psycopg2://postgres:8748@localhost:5432/db'
engine = create_engine(db_url)
