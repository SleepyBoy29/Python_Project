@echo off
setlocal enabledelayedexpansion

rem Tentukan tahun
set year=2024

rem Loop untuk setiap bulan
for /l %%m in (1,1,12) do (
    rem Format bulan menjadi dua digit
    set month=0%%m
    set month=!month:~-2!

    rem Tentukan jumlah hari dalam bulan
    if %%m==1  set days=31
    if %%m==3  set days=31
    if %%m==4  set days=30
    if %%m==5  set days=31
    if %%m==6  set days=30
    if %%m==7  set days=31
    if %%m==8  set days=31
    if %%m==9  set days=30
    if %%m==10 set days=31
    if %%m==11 set days=30
    if %%m==12 set days=31
    if %%m==2  (
        rem Hitung apakah tahun kabisat
        set /a isLeap=!year! %% 4
        if !isLeap! == 0 (
            set /a isLeap=!year! %% 100
            if !isLeap! neq 0 (
                set days=29
            ) else (
                set /a isLeap=!year! %% 400
                if !isLeap! == 0 (set days=29) else (set days=28)
            )
        ) else (
            set days=28
        )
    )

    rem Loop untuk setiap hari dalam bulan
    for /l %%d in (1,1,!days!) do (
        rem Format hari menjadi dua digit
        set day=0%%d
        set day=!day:~-2!

        rem Tampilkan tanggal dengan format YYYY_MM_DD
        echo !year!/!month!/!day!
    )
)

pause
