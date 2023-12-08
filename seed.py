from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random
from models import Student, Group, Teacher, Subject, Grade, Base, StudentGroup

from sqlalchemy.exc import IntegrityError

# Підключення до бази даних
db_url = 'postgresql+psycopg2://postgres:8748@localhost:5432/db'
engine = create_engine(db_url)

# Створення сесії
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Ініціалізація Faker
fake = Faker()

# Додавання студентів
for _ in range(random.randint(30, 50)):
    student = Student(student_name=fake.name())
    session.add(student)

# Додавання груп
group_names = ['Group A', 'Group B', 'Group C']
for group_name in group_names:
    group = Group(group_name=group_name)
    session.add(group)

# Додавання викладачів
for _ in range(random.randint(3, 5)):
    teacher = Teacher(teacher_name=fake.name())
    session.add(teacher)

# Додавання предметів і вказівка викладача
subjects = ['Math', 'Physics', 'History', 'Biology', 'Chemistry']
for subject_name in subjects:
    teacher = session.query(Teacher).order_by(func.random()).first()  # Вибираємо випадкового викладача
    subject = Subject(subject_name=subject_name, teacher=teacher)
    session.add(subject)



# Збереження змін у базі даних
session.commit()

# Закриття сесії
session.close()


# Збереження змін у базі даних
session.commit()

# Закриття сесії
session.close()


