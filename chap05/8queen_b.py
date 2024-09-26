# 各列に１個の王妃を配置する組合せを再帰的に列挙

pos = [0] * 8   # 各列の王妃の位置

def put() -> None:
    """盤面（各列の王妃の位置）を出力"""
    for i in range(8):
        print(f'{pos[i]:2}', end=' ')
    print()

def set(i: int) -> None:
    """i列目に王妃を配置"""
    for j in range(8):
        pos[i] = j          # 王妃をj行に配置
        if i == 7:          # 全列に配置終了
            put()
        else:
            set(i + 1)      # 次の列に王妃を配置

set(0)          # 0列目に王妃を配置
