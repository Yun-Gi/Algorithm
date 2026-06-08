# [ALDS1] 線形探索 - ALDS1_4_A

[問題リンク](https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/4/ALDS1_4_A)

## 実行結果 (Performance)
* 時間計算量 (Time Complexity): O(N^2)
* 実行時間 (Execution Time): 00.02 sec
* メモリ使用量 (Memory): 9436 KB

## 問題概要 (Description)
* SとTの中で重複する要素の個数を求めなさい。
* 制約条件: n ≤ 10,000、q ≤ 500、0 ≤ Sの要素, Tの要素 ≤ 10^9

## 解法 (Approach)
* 線形探索を使う。配列の中で一つを選んで、その要素の1番から他の配列のすべての要素と比べて同じことを探す。



