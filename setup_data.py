import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_sys.settings')
django.setup()

from accounts.models import CustomUser
from core.models import StudentProfile, TeacherProfile, Subject, Notification

def create_data():
    # Admin
    if not CustomUser.objects.filter(username='admin').exists():
        admin = CustomUser.objects.create_superuser('admin', 'admin@example.com', 'adminpass')
        print("Created Superuser: admin/adminpass")

    # Teacher
    if not CustomUser.objects.filter(username='teacher1').exists():
        t_user = CustomUser.objects.create_user('teacher1', 'teacher@example.com', 'teacherpass', is_teacher=True)
        TeacherProfile.objects.create(user=t_user, department='Science')
        
        # Subject
        Subject.objects.create(name='Physics', code='PHY101', teacher=t_user.teacher_profile)
        print("Created Teacher: teacher1/teacherpass")

    # Student
    if not CustomUser.objects.filter(username='student1').exists():
        s_user = CustomUser.objects.create_user('student1', 'student@example.com', 'studentpass', is_student=True)
        StudentProfile.objects.create(user=s_user, roll_no='S101', grade='12th')
        
        # Notification
        Notification.objects.create(recipient=s_user, message='Welcome to the 3D Portal!')
        print("Created Student: student1/studentpass")

if __name__ == '__main__':
    create_data()
