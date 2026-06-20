# [ALDS1] 割り当て - ALDS1_4_D

[問題リンク](https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/4/ALDS1_4_D)

## 実行結果 (Performance)
* 時間計算量 (Time Complexity): O(NlogM)
* 実行時間 (Execution Time): 00.31 sec
* メモリ使用量 (Memory): 12092 KB

## 問題概要 (Description)
* 最大積載量Pの最小値を求めなさい。
* 制約条件: 1 ≤ n ≤ 100,000、1 ≤ k ≤ 100,000、1 ≤ w[i] ≤ 100,000

## 解法 (Approach)
* 二分探索をつかいます。まず、条件でできるPの最小値と最大値の中央値をPに決めて計算してみます。Pができれば最小値を中央値+1にしてまた計算し、できない場合は最大値を中央値-1にして繰り返します。



