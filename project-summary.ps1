Write-Host "Project summary (generated $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss'))`n"

Write-Host "Project files in this folder:`n"
Get-ChildItem *.md

Write-Host "`nLine counts:"

# Safely count lines in tasks.md
if (Test-Path .\tasks.md) {
    $tasksLines = (Get-Content .\tasks.md | Measure-Object -Line).Lines
    $tasksLabel = "tasks.md:"
} else {
    $tasksLines = 0
    $tasksLabel = "tasks.md (missing):"
}

# Safely count lines in project-notes.md
if (Test-Path .\project-notes.md) {
    $notesLines = (Get-Content .\project-notes.md | Measure-Object -Line).Lines
    $notesLabel = "project-notes.md:"
} else {
    $notesLines = 0
    $notesLabel = "project-notes.md (missing):"
}

# Total lines across both files (missing files contribute 0)
$totalLines = $tasksLines + $notesLines

Write-Host ("{0,-22} {1}" -f $tasksLabel, $tasksLines)
Write-Host ("{0,-22} {1}" -f $notesLabel, $notesLines)
Write-Host ("{0,-22} {1}" -f "TOTAL:",     $totalLines)
