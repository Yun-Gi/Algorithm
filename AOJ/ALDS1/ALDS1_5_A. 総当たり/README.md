# [ALDS1] 総当たり - ALDS1_5_A

[問題リンク](https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/5/ALDS1_5_A)

## 実行結果 (Performance)
* 時間計算量 (Time Complexity): O(q*2^n)
* 実行時間 (Execution Time): 01.61 sec
* メモリ使用量 (Memory): 107936 KB

## 問題概要 (Description)
* 配列Aの要素の中のいくつかを足し合わせてｍを作られるかを返しなさい。
* 制約条件: n ≤ 20、q ≤ 200、1 ≤ Aの要素 ≤ 2,000、1 ≤ m[i] ≤ 2,000

## 解法 (Approach)
* 総当たりをして、すべてのAの要素を足すのか足さないのかの場合を考えて、m[i]ができるのかできないのかを判断。
* こんなコードはpythonの特性のせいで制限時間内に解決するのが難しいです。だからpypy3を使用しました。



