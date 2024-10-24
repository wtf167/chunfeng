import os
import numpy as np

# aMaze 迷宫地图(二维数组)
# start 开始位置(0,0)
# end 出口(4,5)
# iRoad 能走的标识*/0
# iExit 出口标志F/#
def fMaze(aMaze, start, end, iRoad, iExit):
    lPath = [start]
    # 定义上下左右输入字符
    r = ['w', 's', 'a', 'd']
    flag = []
    while lPath:
        now = lPath[-1]
        if now == end:
            print("success")
            break
        row, col = now
        # 标记已走过的路，防止重复
        aMaze[row][col] = '@'
        # 上
        if aMaze[row - 1][col] == iRoad or aMaze[row - 1][col] == iExit:
            lPath.append((row - 1, col))
            flag.append(r[0])
            continue
        # 下
        elif aMaze[row + 1][col] == iRoad or aMaze[row + 1][col] == iExit:
            lPath.append((row + 1, col))
            flag.append(r[1])
            continue
        # 左
        elif aMaze[row][col - 1] == iRoad or aMaze[row][col - 1] == iExit:
            lPath.append((row, col - 1))
            flag.append(r[2])
            continue
        # 右
        elif aMaze[row][col + 1] == iRoad or aMaze[row][col + 1] == iExit:
            lPath.append((row, col + 1))
            flag.append(r[3])
            continue
        else:
            lPath.pop()
            flag.pop()
    return flag


def fStr2Maze(sMaze, rows, cols):
    aMaze = np.zeros([rows, cols], dtype=str)
    for r in range(rows):
        for c in range(cols):
            aMaze[r][c] = sMaze[r * cols + c]
    return aMaze


# sMaze = '*******+********* ******    ****   ******* **F******    **************'
sMaze = "##***********************#*#####*****************#*#***#*****************#*#***#****########*****###***#*******#***#***********#########***#***********************#**************####**!**#**************#**#**#**#**************#**#**#**#**************#**####**#**************#********#**************##########****************************"
aMaze = fStr2Maze(sMaze, 7, 10)
# print(aMaze)
start = (0, 7)
end = (4, 5)
flag = fMaze(aMaze, start, end, ' ', 'F')
print("".join(flag))