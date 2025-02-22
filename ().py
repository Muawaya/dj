# coding: utf-8
from projects.models import Project
p1 = Project(
    title='My First Project',
    description='A web development project.',
    technology='Django',
    image='img/project1.png'
)
p1.save()
p2 = Project(
    title='My Second Project',
    description='Another web development project.',
    technology='Flask',
    image='img/project2.png'
)
p2.save()
p3 = Project(
    title='My Third Project',
    description='A final development project.',
    technology='Django',
    image='img/project3.png'
)
p3.save()
