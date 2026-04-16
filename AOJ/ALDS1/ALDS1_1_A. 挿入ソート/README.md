# [ALDS1] 挿入ソート (Insertion Sort) - ALDS1_1_A

[問題リンク](https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/1/ALDS1_1_A)

## 実行結果 (Performance)
* 時間計算量 (Time Complexity): O(N^2)
* 実行時間 (Execution Time): 00.00 sec
* メモリ使用量 (Memory): 8256 KB

## 問題概要 (Description)
* N個の要素を持つ数列を挿入ソート(Insertion Sort)を用いて昇順に整列する。
* 各ソートのステップごとに配列の現在の状態を出力する。
* 制約条件: 1 <= N <= 100

## 解法 (Approach)
* 配列の2番目の要素から開始し、前の要素と比較しながら適切な位置に挿入するロジックを実装。
* Pythonの組み込み関数である `sort()` は使用せず、アルゴリズムの原理通りに二重ループを用いて直接実装した。



