@echo off

@REM 事前にコピー元のフォルダを作成しておく
@REM 作成するフォルダのディレクトリに移動する
cd agc

@REM inの中に何番から何番のフォルダを作成するかを記載する
for /l %%n in (10,1,99) do (
    robocopy agcXXXX agc0%%n    
)