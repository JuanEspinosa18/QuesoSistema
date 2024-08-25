def is_employee(user):
    return user.groups.filter(name='Empleado').exists()
