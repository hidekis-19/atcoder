@echo off

@REM 事前にコピー元のフォルダを作成しておく
@REM 作成するフォルダのディレクトリに移動する
cd arc

@REM inの中に何番から何番のフォルダを作成するかを記載する
for /l %%n in (100,1,130) do (
    robocopy arcXXXX arc%%n    
)