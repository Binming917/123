from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

x_weizhi = 0
y_weizhi = 0
z_weizhi = -10
d_shidian = 10
thta_y = 0
thta_x = 0

m_tranlate = [0, 0, -10]
m_rorate = [0, 0]
m_scale = 1.0
m_MouseDownPT = [0, 0]
m_bMouseDown = False

# 坐标轴及坐标面顶点坐标
verticies_zuobiao = [
    [0, 0, 0],
    [15, 0, 0],
    [0, 15, 0],
    [0, 0, 15],
    [10, 10, 0],
    [-10, 10, 0],
    [-10, -10, 0],
    [10, -10, 0]
]

# 坐标轴及必标面连线列表
edges_zuobiao = [
    [0, 1],
    [0, 2],
    [0, 3],
    [4, 5],
    [5, 6],
    [6, 7],
    [7, 4]
]


# 坐标轴绘制模块
def zuobiao():
    glLineWidth(3)
    glBegin(GL_LINES)
    for edge in edges_zuobiao:
        for vertex in edge:
            glVertex3fv(verticies_zuobiao[vertex])
    glEnd()
    glColor3f(1, 0.9, 0.3)
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex3fv([0, 0, d_shidian])
    glEnd()


def huachuzuobaio():
    glPushMatrix()
    glTranslatef(0, 0, 0.0)
    glRotatef(0, 0, 0, 1)
    glScalef(1, 1, 1)
    glColor3f(1, 1, 0.4)
    glLineWidth(3)
    zuobiao()
    glPopMatrix()


bianchang = 5
verticies = [
    [0, 0, 0],
    [0, 0, bianchang],
    [bianchang, 0, bianchang],
    [bianchang, 0, 0],
    [bianchang, bianchang, 0],
    [0, bianchang, 0],
    [0, bianchang, bianchang],
    [bianchang, bianchang, bianchang]
]
verticies_toushi = verticies
edges = [
    [0, 1],
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5],
    [5, 6],
    [6, 7],
    [7, 4],
    [7, 2],
    [6, 1],
    [3, 0],
    [5, 0]
]


def huadian():
    glColor3f(1, 0.5, 0.5)
    glPointSize(5)
    glBegin(GL_POINTS)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def huatoushexian():
    glLineWidth(2)
    glColor3f(1, 1, 0.2)
    glBegin(GL_LINES)
    for edge in edges:
        i = 0
        for vertex in edge:
            x = verticies[vertex][0]
            y = verticies[vertex][1]
            z = verticies[vertex][2]
            x2 = 0
            y2 = 0
            z2 = 0
            x1 = x * math.cos(thta_y / 57.3) + z * math.sin(thta_y / 57.3)
            y1 = y
            z1 = -x * math.sin(thta_y / 57.3) + z * math.cos(thta_y / 57.3)

            x2 = x1
            y2 = y1 * math.cos(thta_x / 57.3) + z1 * math.sin(thta_x / 57.3)
            z2 = y1 * math.sin(thta_x / 57.3) + z1 * math.cos(thta_x / 57.3)

            x3 = x2 + x_weizhi
            y3 = y2 + y_weizhi
            z3 = z2 + z_weizhi
            glVertex3fv([x3, y3, z3])

            xs = (0 - d_shidian) / (z3 - d_shidian) * (x3 - 0) + 0
            xs = (0 - d_shidian) / (z3 - d_shidian) * (y3 - 0) + 0
            zs = 0
            glVertex3fv([0, 0, d_shidian])
    glEnd()

    glColor3f(1, 0.1, 0.1)

    glPointSize(3)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            x = verticies[vertex][0]
            y = verticies[vertex][1]
            z = verticies[vertex][2]
            x2 = 0
            y2 = 0
            z2 = 0
            x1 = x * math.cos(thta_y / 57.3) + z * math.sin(thta_y / 57.3)
            y1 = y
            z1 = -x * math.sin(thta_y / 57.3) + z * math.cos(thta_y / 57.3)

            x2 = x1
            y2 = y1 * math.cos(thta_x / 57.3) + z1 * math.sin(thta_x / 57.3)
            z2 = y1 * math.sin(thta_x / 57.3) + z1 * math.cos(thta_x / 57.3)

            x3 = x2 + x_weizhi
            y3 = y2 + y_weizhi
            z3 = z2 + z_weizhi

            xs = (0 - d_shidian) / (z3 - d_shidian) * (x3 - 0) + 0
            ys = (0 - d_shidian) / (z3 - d_shidian) * (y3 - 0) + 0
            zs = 0
            glVertex3fv([xs, ys, zs])
    glEnd()


def sanweiliti():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def litizhanshi():
    glLineWidth(5)
    glPushMatrix()
    glTranslatef(x_weizhi, y_weizhi, z_weizhi)
    glRotatef(thta_x, 1, 0, 1)
    glRotatef(thta_y, 1, 0, 1)
    glScalef(1, 1, 1)
    glColor3f(1, 1, 1)
    sanweiliti()
    huadian()
    glPopMatrix()
    huatoushexian()


def Draw():
    glPushMatrix()

    glColor3f(0.4, 0.5, 0.5)
    glTranslatef(0, 0, 0)
    glRotatef(m_rorate[0], 1, 0, 0)
    glRotatef(m_rorate[1], 0, 1, 0)
    glScalef(m_scale, m_scale, m_scale)
    glTranslatef(0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    huachuzuobaio()
    litizhanshi()
    huatoushexian()
    glFlush()
    glPopMatrix()


def MouseEvent(button, state, x, y):
    global m_scale
    if (state == GLUT_UP):
        if (button == 3):
            m_scale += 0.1
        elif (button == 4):
            m_scale -= 0.1
            if (m_scale < 0.1):
                m_scale = 0.1

    global m_bMouseDown
    global m_MouseDownPT
    if (state == GLUT_DOWN and button == GLUT_LEFT_BUTTON):
        m_bMouseDown = True
        m_MouseDownPT[0] = x
        m_MouseDownPT[1] = y
    else:
        m_bMouseDown = False


def MotionEvent(x, y):
    global m_rorate
    global m_MouseDownPT
    if (m_bMouseDown == True):
        m_rorate[0] += y - m_MouseDownPT[1]
        m_rorate[1] += x - m_MouseDownPT[0]
        m_MouseDownPT[0] = x
        m_MouseDownPT[1] = y


def KeyboardEvent(key, x, y):
    global x_weizhi, y_weizhi, z_weizhi, d_shidian, thta_y, thta_x

    if (key == b'W'):
        y_weizhi += 0.2
    elif (key == b'S'):
        y_weizhi -= 0.2
    elif (key == b'A'):
        x_weizhi -= 0.2
    elif (key == b'D'):
        x_weizhi += 0.2
    elif (key == b'Q'):
        z_weizhi -= 0.2
    elif (key == b'E'):
        z_weizhi += 0.2

    elif (key == b'R'):
        d_shidian -= 0.2
    elif (key == b'F'):
        d_shidian += 0.2
    elif (key == b'T'):
        thta_y -= 5
    elif (key == b'G'):
        thta_y += 5
    elif (key == b'Y'):
        thta_x -= 0.5
    elif (key == b'H'):
        thta_x += 0.5


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutInitWindowSize(640, 480)
glutCreateWindow("3D toushi")
shijingti = 30
glOrtho(-shijingti, shijingti, -shijingti, shijingti, -shijingti, shijingti)
glScalef(1.2, 1.2, 1.2)
glRotatef(38, 1, 0, 0)
glRotatef(-35, 0, 1, 0)
glutKeyboardFunc(KeyboardEvent)
glutMouseFunc(MouseEvent)
glutMotionFunc(MotionEvent)
glutDisplayFunc(Draw)
glutIdleFunc(Draw)
glutMainLoop()

if __name__ == '__main__':
    Draw()
