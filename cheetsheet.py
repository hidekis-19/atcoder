#文字が1つのとき
a = input()

#数字が複数のとき
a,b= map(int, input().split())

#1行に複数の入力値を取得する
s = input().split() 
#1行に複数の整数の入力を取得する
i = list(map(int, input().split())) 

#複数行に複数の入力値を取得する
s = [input() for i in range(3)]

num_list = list(map(int, input().split()))  # n個の数字がリストに格納される

# データを取る
#1行目を取得
N,S,D= map(int, input().split())

#複数行で複数の入力値の時
num_list = []
for i in range(N):
    num_list.append(list(map(int,input().split())))

#ここから先がロジック


#2列で何行かわからないとき
while True:
    a,b = map(int, input().split())
    if a == 0 and b == 0: break
    print(a,b)


#数字を配列から標準出力
L=[str(a) for a in a]
L=" ".join(L)
#文字列を配列から標準出力
L=' '.join(L)


#インプットが行数不明の場合
import sys 
members = [] 
for i in sys.stdin.readlines(): 
    members.append(i.rstrip()) 

#文字列からリストにする
i = i.split(' ',2)


#インデックス番号と要素を取得するとき
for i, name in enumerate(a):
    print(i, name)

#10進数の文字列を数値に変換
l_si_i = [int(s) for s in a]


#リストで一致する要素のインデックスをすべて返す
indexes = [i for i, x in enumerate(list) if x == 1]

#10進数をn変数に変換
#X...変換する値。n...変数
def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)

#最小公倍数
import math
int(a * b / math.gcd(a, b))

"""
実装するときの注意メモ
　・桁が多い時の割り算は//を使う
　　掛け算したり、割り算をするとfloatで持とうとするから桁あふれが起きる可能性がある
　・inputが多い時はとりあえずリスト等に入れてから処理をする
　　inputの処理に合わせて、処理をするとTLEになる可能性がある abc164c
  ・数えあげはcollections.Counter(A)を使う
  　量が多い時にfor文でとかで回すとTLEになりがち abc154c,155c
  ・2重ループにするとTLEになりそうなときは、どうにかして足算になるようにする abc202c
  ・NGのときは制約の境界値を気にする　abc157c
"""