def is_employee(user):
    return user.profile.role.name == 'Empleado' if hasattr(user, 'profile') and hasattr(user.profile, 'role') else False
