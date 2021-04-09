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
