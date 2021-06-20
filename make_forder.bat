@echo off

@REM 事前にコピー元のフォルダを作成しておく
@REM 作成するフォルダのディレクトリに移動する
cd abc

@REM inの中に何番から何番のフォルダを作成するかを記載する in (開始値、増分、終了値)
for /l %%n in (207,1,250) do (
    robocopy abcXXXX abc%%n    
)

cd ..