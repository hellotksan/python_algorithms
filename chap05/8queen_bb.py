# 各行・各列に１個の王妃を配置する組合せを再帰的に列挙

pos = [0] * 8        # 各列の王妃の位置
flag = [False] * 8   # 各行に王妃が配置ずみか

def put() -> None:
    """盤面（各列の王妃の位置）を出力"""
    for i in range(8):
        print(f'{pos[i]:2}', end=' ')
    print()

def set(i: int) -> None:
    """i列目の適切な位置に王妃を配置"""
    for j in range(8):
        if not flag[j]:     # j行には王妃は未配置
            pos[i] = j          # 王妃をj行に配置
            if i == 7:          # 全列に配置終了
                put()
            else:
                flag[j] = True
                set(i + 1)      # 次の列に王妃を配置
                flag[j] = False

set(0)          # 0列目に王妃を配置
