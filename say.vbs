If WScript.Arguments.Count > 0 Then

    Set FSO = CreateObject("Scripting.FileSystemObject")
    If FSO.FileExists(WScript.Arguments(0)) Then
        Set tfile = FSO.OpenTextFile(WScript.Arguments(0))
        TextSay = tfile.ReadAll()
    Else
    ReDim arr(WScript.Arguments.Count-1)
       For i = 0 To WScript.Arguments.Count-1
     arr(i) = WScript.Arguments(i)
    Next
       TextSay = Join(arr," ")
    End If

    Set speech = CreateObject("SAPI.spVoice")
    speech.Speak TextSay
Else

'No arguments, nothing to do...
   
End If
