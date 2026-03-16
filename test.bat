@echo off
for /l %%i in (1,1,1000) do (
    echo msgbox "Are you just going to keep pressing this button out of boredom?", vbquestion + vbyesno, "Question" > popup.vbs
    cscript //nologo popup.vbs
)
del popup.vbs
pause