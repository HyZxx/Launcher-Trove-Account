SetTimer, A, 100000
return


A:
    WinGet, l, list, ahk_exe Trove.exe
    Loop %l%
    {
        ControlSend, , {space}, % "ahk_id" l%a_index%
    }
    return


Numpad1:: 
    WinGet, l, list, ahk_exe Trove.exe
    Loop %l%
    {
        ControlSend, , {e}, % "ahk_id" l%a_index%
    }
    return
Numpad2:: 
    WinGet, l, list, ahk_exe Trove.exe
    Loop %l%
    {
        ControlSend, , {b}, % "ahk_id" l%a_index%
    }
    return

Numpad3:: 
    WinGet, l, list, ahk_exe Trove.exe
    Loop %l%
    {
        ControlSend, , {l}, % "ahk_id" l%a_index%
    }
    return


Up::
    SetKeyDelay, 0, 50 ; Délais entre les pressions de touches
    Loop
    {
        if !GetKeyState("Up", "P")
            break
        WinGet, l, list, ahk_exe Trove.exe
        Loop %l%
        {
            ControlSend, , {z}, % "ahk_id" l%a_index%
        }
    }
    return

Down:: 
    SetKeyDelay, 0, 50 ; Délais entre les pressions de touches
    Loop
    {
        if !GetKeyState("Down", "P")
            break
        WinGet, l, list, ahk_exe Trove.exe
        Loop %l%
        {
            ControlSend, , {s}, % "ahk_id" l%a_index%
        }
    }
    return
Right:: 
    SetKeyDelay, 0, 50 ; Délais entre les pressions de touches
    Loop
    {
        if !GetKeyState("Right", "P")
            break
        WinGet, l, list, ahk_exe Trove.exe
        Loop %l%
        {
            ControlSend, , {d}, % "ahk_id" l%a_index%
        }
    }
    return
Left:: 
    SetKeyDelay, 0, 50 ; Délais entre les pressions de touches
    Loop
    {
        if !GetKeyState("Left", "P")
            break
        WinGet, l, list, ahk_exe Trove.exe
        Loop %l%
        {
            ControlSend, , {q}, % "ahk_id" l%a_index%
        }
    }
    return

Numpad0:: 
    ExitApp