# [ALDS1] 二分探索 - ALDS1_4_B

[問題リンク](https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/4/ALDS1_4_B)

## 実行結果 (Performance)
* 時間計算量 (Time Complexity): O(QlogN)
* 実行時間 (Execution Time): 00.14 sec
* メモリ使用量 (Memory): 19912 KB

## 問題概要 (Description)
* SとTの中で重複する要素の個数を求めなさい。
* 制約条件: n ≤ 100,000、q ≤ 50,000、0 ≤ Sの要素, Tの要素 ≤ 10^9

## 解法 (Approach)
* 二分探索を使う。配列の中で一つを選んで、その要素をSの中央と比べて小さい場合は中央より低い部分を、また大きい場合は高い部分を、その中でまた中央を決めてそれを繰り返して計算する。



