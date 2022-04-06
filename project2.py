from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


verticies_zuobiao =[
    [0, 0, 0],
    [24, 0, 0],
    [0, 24, 0],
    [0, 0, 24],
    [24, 24, 0],
    [-24, 22, 0],
    [-24, -24, 0],
    [24, -24, 0],

]

edges_zuobiao =[
    [0, 1],
    [0, 2],
    [0, 3],
    [4, 5],
    [5, 6],
    [6, 7],
    [7, 4],
]
def zuobiao():
    glColor3f(0.3, 1, 1)
    glBegin(GL_LINES)
    for edge in edges_zuobiao:
        for vertex in edge:
            glVertex3fv(verticies_zuobiao[vertex])
    glEnd()

def huachuzuobiao():
    #画出坐标轴
    glPushMatrix()
    glTranslatef(0, 0, 0.0)
    glRotatef(0, 0, 0, 1)
    glScalef(0.05, 0.05, 0.05)
    glColor3f(1, 1, 1)
    zuobiao()
    glPopMatrix()

verticies =[
    [-7.55, 0, 0],
    [-7.55, 0, 15],
    [-7.55, 5, 0],
    [7.45, 0, 15],
    [7.45, 0, 0],
    [-7.55, 5, 15],
    [7.45, 5, 15],
    [7.45, 5, 0],
    [-2.55, 5, 0],
    [2.45, 5, 0],
    [2.45, 5, 7.5],
    [-2.55, 5, 7.5],
    [-2.55, 5, 7.5],
    [-2.55, 10, 0],
    [2.45, 10, 0],
    [2.45, 10, 7.5],
    [-2.55, 10, 7.5],

]

edges =[
    [0, 1],
    [1, 3],
    [3, 4],
    [4, 0],
    [2, 0],
    [2, 5],
    [5, 6],
    [6, 7],
    [7, 2],
    [1, 5],
    [3, 6],
    [4, 7],
    [8, 9],
    [9, 10],
    [10, 11],
    [11, 8],
    [13, 14],
    [14, 15],
    [15, 16],
    [8, 13],
    [9, 14],
    [10, 15],
    [11, 16],
    [16, 13],
]

def huadian():
    glColor3f(1, 0.5, 0.5)
# 设置点大小
    glPointSize(8)
    # 只绘制端点
    glBegin(GL_POINTS)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

# 画投射线
def huatoushexian():
    glLineWidth(1)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
            x = verticies[vertex][0]
            y = verticies[vertex][1]
            # print("x, y=", x, y)
            glVertex3fv([x, y, -10])

    glEnd()

def sanweiliti():

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


# 三视图的形成
def snashitu():
    # 主视图
    glLineWidth(1)
    glPushMatrix()
    glTranslatef(-0.45, 0, 0.0)
    glRotatef(0, 0, 0, 1)
    glScalef(0.05, 0.05, 0.001)
    glColor3f(1, 1, 1)
    sanweiliti()
    glPopMatrix()

    # 俯视图
    glLineWidth(1)
    glPushMatrix()
    glTranslatef(-0.45, -0.2, 0.0)
    glRotatef(90, 1, 0, 0)
    glScalef(0.05, 0.001, 0.05)
    glColor3f(1, 1, 1)
    sanweiliti()
    glPopMatrix()

    # 左视图
    glLineWidth(1)
    glPushMatrix()
    glTranslatef(0.25, 0, 0.0)
    glRotatef(-270, 0, 1, 0)
    glScalef(0.0001, 0.05, 0.05)
    glColor3f(1, 1, 1)
    sanweiliti()
    glPopMatrix()

# 轴测图
    glLineWidth(1)
    glPushMatrix()
    glTranslatef(0.42, -0.52, 0)
    glScalef(1, 1, 0.0018)
    glRotatef(48, 1, 0, 0)
    glRotatef(45, 0, 1, 0)
    glScalef(0.035, 0.035, 0.035)
    glColor3f(1, 1, 1)
    sanweiliti()
    glPopMatrix()

def litizhanshi():
    # 立体展示
    glLineWidth(3)
    glPushMatrix()
    glTranslatef(-0.45, 0, 0.5)
    glRotatef(0, 0, 1, 0)
    glScalef(0.05, 0.05, 0.05)
    glColor3f(1, 1, 1)
    sanweiliti()
    huadian()
    huatoushexian()
    glPopMatrix()

def Draw():
    glClear(GL_COLOR_BUFFER_BIT)

    glRotatef(0.1, 0, 0.1, 0)
    huachuzuobiao()
    snashitu()
    litizhanshi()
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutInitWindowSize(640, 480)
glutCreateWindow("三维投影练习20220314")
# glOrtho(left, right, bottom, top, near, far)
glOrtho(-2.0, 2.0, -2.0, 2.0, -2.0, 2.0)
glScalef(1.2, 1.2, 1.2)
glRotatef(38, 1, 0, 0)
glRotatef(35, 0, 1, 0)
glutDisplayFunc(Draw)
glutIdleFunc(Draw)
glutMainLoop()

if __name__ == '__main__':
    Draw()