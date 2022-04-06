#
from tkinter import *

root = Tk()

Label(root, text="科恩-苏瑟兰德直线裁剪算法演示").grid(row=0, columnspan=12)
Label(root, text="200701 源斌明").grid(row=1, columnspan=12)
Label(root, text="请输入参数，范围： 10~300").grid(row=2, columnspan=4)

# 窗口参数
Label(root, text = "窗口参数：").grid(row = 3)
Label(root, text="左边界 x_left =").grid(row=4)
x_left = Entry(root, width=3)
x_left.grid(row=4, column=1)
x_left.delete(5, END)
x_left.insert(5, "50")

Label(root, text="右边界 x_right = ").grid(row=4, column=2)
x_right = Entry(root, width=3)
x_right.grid(row=4, column=3)
x_right.delete(0, END)
x_right.insert(5, "200")

Label(root, text="下边界 y_bottom = ").grid(row=5, column=0)
y_bottom = Entry(root, width=3)
y_bottom.grid(row=5, column=1)
y_bottom.delete(0, END)
y_bottom.insert(5, "100")

Label(root, text="上边界 y_top = ").grid(row=5, column=2)
y_top = Entry(root, width=3)
y_top.grid(row=5, column=3)
y_top.delete(0, END)
y_top.insert(5, "200")

# 直线段参数
Label(root, text="直线段参数：").grid(row=6)
Label(root, text="P1的x =").grid(row=7)
xP1 = Entry(root, width=3)
xP1.grid(row=7, column=1)
xP1.delete(5, END)
xP1.insert(5, "60")
x1 = int(xP1.get())

Label(root, text="P1的y =").grid(row=7, column=2)
yP1 = Entry(root, width=3)
yP1.grid(row=7, column=3)
yP1.delete(0, END)
yP1.insert(5, "60")
y1 = int(yP1.get())

Label(root, text="P2的x =").grid(row=8, column=0)
xP2 = Entry(root, width=3)
xP2.grid(row=8, column=1)
xP2.delete(0, END)
xP2.insert(5, "240")
x2 = int(xP2.get())

Label(root, text="P2的y =").grid(row=8, column=2)
yP2 = Entry(root, width=3)
yP2.grid(row=8, column=3)
yP2.delete(0, END)
yP2.insert(5, "280")
y2 = int(yP2.get())

Label(root, text="计算结果 =").grid(row=14, column=2)
res = Entry(root, width=12)
res.grid(row=14, column=3)
res.delete(5, END)
res.insert(5, "等待结果")

# 编码
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8

xMin = 50
xMax = 200
yMin = 100
yMax = 200

w = Canvas(root, width=300, height=300, bg="gray")
w.grid(row=2, column=10, rowspan=10)




# 画出基础图形
def printBase():
    w.delete(ALL)
    x1 = int(xP1.get())
    y1 = int(yP1.get())
    x2 = int(xP2.get())
    y2 = int(yP2.get())
    xMin = int(x_left.get())
    xMax = int(x_right.get())
    yMin = int(y_bottom.get())
    yMax = int(y_top.get())

    # 画出窗口矩阵及其边界延长线
    window = w.create_rectangle(xMin, yMin, xMax, yMax, fill="blue")
    borderL = w.create_line(xMin, 0, xMin, 300, fill="white", width=2, dash=(2, 4))
    borderR = w.create_line(xMax, 0, xMax, 300, fill="white", width=2, dash=(2, 4))
    borderB = w.create_line(0, yMin, 300, yMin, fill="blue", width=2, dash=(2, 4))
    borderT = w.create_line(0, yMax, 300, yMax, fill="blue", width=2, dash=(2, 4))

    # 画出原始P1 P2线段 求出编码
    w.create_line(x1, y1, x2, y2, fill="white", width=3, dash=(4, 4))
    px1_text = int(xP1.get())
    py1_text = int(yP1.get()) - 10
    text_p1 = w.create_text(px1_text, py1_text, text="P1(" + xP1.get() + "," + yP1.get() + ")", fill="white")

    px2_text = int(xP2.get())
    py2_text = int(yP2.get()) + 10
    text_p2 = w.create_text(px2_text, py2_text, text="P2(" + xP2.get() + "," + yP2.get() + ")", fill="white")

    # 画出坐标轴
    w.create_line(0, 5, 300, 5, fill="white", width=3)
    text1 = w.create_text(280, 25, text="x轴", fill="white")
    text1 = w.create_text(280, 12, text="300", fill="white")
    text1 = w.create_text(180, 12, text="200", fill="white")
    text1 = w.create_text(80, 12, text="100", fill="white")

    w.create_line(5, 0, 5, 300, fill="white", width=3)
    text1 = w.create_text(25, 260, text="y轴", fill="white")
    text1 = w.create_text(25, 280, text="300", fill="white")
    text1 = w.create_text(25, 180, text="200", fill="white")
    text1 = w.create_text(25, 80, text="100", fill="white")


# 编码
def encode(x, y):
    c = 0
    if x < xMin:
        c = c | LEFT
    if x > xMax:
        c = c | RIGHT
    if y < yMin:
        c = c | BOTTOM
    if y > yMax:
        c = c | TOP
    return c


def cohensutherland():
    # 取出文本框的值
    test = 0
    global x1, y1, x2, y2, xl, xr, yb, yt
    x1 = int(xP1.get())
    y1 = int(yP1.get())
    x2 = int(xP2.get())
    y2 = int(yP2.get())
    xl = int(x_left.get())
    xr = int(x_right.get())
    yb = int(y_bottom.get())
    yt = int(y_top.get())

    code1 = encode(x1, y1)
    code2 = encode(x2, y2)
    outcode = code1
    area = False
    while True:
        if (code1 | code2) == 0:
            area = True
            break
        elif (code1 & code2) != 0:
            break
        else:
            new_x, new_y = 0, 0
            # 取窗外点
            outcode = code1 if code1 != 0 else code2
            if (LEFT & outcode) != 0:
                new_x = xl
                new_y = y1 + (y2 - y1) * (xl - x1) / (x2 - x1)
            elif (RIGHT & outcode) != 0:
                new_x = xr
                new_y = y1 + (y2 - y1) * (xr - x1) / (x2 - x1)
            elif (BOTTOM & outcode) != 0:
                new_y = yb
                new_x = x1 + (x2 - x1) * (yb - y1) / (y2 - y1)
            elif (TOP & outcode) != 0:
                new_y = yt
                new_x = x1 + (x2 - x1) * (yt - y1) / (y2 - y1)
            # 用交点代替窗外点 完成一次裁剪
            if outcode == code1:
                x1 = int(new_x)
                y1 = int(new_y)
                code1 = encode(x1, y1)
            else:
                x2 = int(new_x)
                y2 = int(new_y)
                code2 = encode(x2, y2)

    if area == True:
        res.delete(0, END)
        res.insert(0, "与窗口相交")
        w.create_line(x1, y1, x2, y2, fill="red", width=4)
    else:
        res.delete(0, END)
        res.insert(0, "不相交")
    return


printBase()
Button(text="CohenSutherland算法", width=16, comman=cohensutherland).grid(row=13, columnspan=4, pady=5)
Button(text="图形显示刷新", width=16, comman=printBase).grid(row=12, columnspan=4, pady=5)
mainloop()
