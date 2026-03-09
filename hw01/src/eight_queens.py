def solve_n_queens(n: int) -> list[list[str]]:
    """
    使用回溯法解决N皇后问题
    :param n: 棋盘大小
    :return: 所有合法的棋盘布局
    """

    def backtrack(row: int, queens: list[int],
                  cols: set[int], diags1: set[int], diags2: set[int]):
        if row == n:
            board = ['.' * q + 'Q' + '.' * (n - q - 1) for q in queens]
            solutions.append(board)
            return
        for col in range(n):
            d1 = row - col
            d2 = row + col
            if col not in cols and d1 not in diags1 and d2 not in diags2:
                cols.add(col)
                diags1.add(d1)
                diags2.add(d2)
                queens.append(col)
                backtrack(row + 1, queens, cols, diags1, diags2)
                queens.pop()
                cols.remove(col)
                diags1.remove(d1)
                diags2.remove(d2)

    solutions = []
    backtrack(0, [], set(), set(), set())
    return solutions


if __name__ == "__main__":
    # 测试8皇后问题
    solutions = solve_n_queens(8)
    print(f"Found {len(solutions)} solutions for 8-Queens problem.")