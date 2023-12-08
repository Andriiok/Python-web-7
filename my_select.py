from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker, session
from models import Student, Subject, Grade, Group, Teacher

engine = create_engine('postgresql+psycopg2://postgres:8748@localhost:5432/db', echo=True, future=True)
Session = sessionmaker(bind=engine)

def select_1(session):
    result = session.query(Student, func.avg(Grade.grade).label('average_grade')) \
        .join(Grade).group_by(Student.id).order_by(func.avg(Grade.grade).desc()).limit(5).all()
    return result

def select_2(session, subject_name):
    result = session.query(Student, func.avg(Grade.grade).label('average_grade')) \
        .join(Grade).join(Subject).filter(Subject.subject_name == subject_name) \
        .group_by(Student.id).order_by(func.avg(Grade.grade).desc()).first()
    return result

def select_3(session, subject_name):
    result = session.query(Group.group_name, func.avg(Grade.grade).label('average_grade')) \
        .join(Student).join(Grade).join(Subject).filter(Subject.subject_name == subject_name) \
        .group_by(Group.group_name).all()
    return result



def select_4(session):
    result = session.query(func.avg(Grade.grade).label('average_grade')).first()
    return result


def select_5(session, teacher_name):
    result = session.query(Subject.subject_name).join(Teacher).filter(Teacher.teacher_name == teacher_name).all()
    return result


def select_6(session, group_name):
    result = session.query(Student).join(Student.groups).filter(Group.group_name == group_name).all()
    return result


def select_7(group_name, subject_name):
    query = (
        session.query(Student.student_name, Grade.grade)
        .join(Group)
        .join(Grade)
        .join(Subject)
        .filter(Group.group_name == group_name, Subject.subject_name == subject_name)
    )
    return query.all()


def select_8(teacher_name):
    query = (
        session.query(func.avg(Grade.grade).label('avg_grade'))
        .join(Subject)
        .join(Teacher)
        .filter(Teacher.teacher_name == teacher_name)
    )
    return query.scalar()


def select_9(student_name):
    query = (
        session.query(Subject.subject_name)
        .join(Grade)
        .join(Student)
        .filter(Student.student_name == student_name)
        .distinct()
    )
    return query.all()


def select_10(student_name, teacher_name):
    query = (
        session.query(Subject.subject_name)
        .join(Grade)
        .join(Student)
        .join(Teacher)
        .filter(Student.student_name == student_name, Teacher.teacher_name == teacher_name)
        .distinct()
    )
    return query.all()




