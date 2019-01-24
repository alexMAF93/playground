function beep_beep()
{

[console]::beep(500,300)
sleep 1
[console]::beep(500,300)
sleep 1
[console]::beep(500,300)

}


function reverse_counter()
{

param ([int]$number_of_seconds, [string]$action)
$current_progress = 0
while ($current_progress -le $number_of_seconds)
{
    $percent = $current_progress / $number_of_seconds
    $display_percent = "{0:p0}" -f $percent
    Write-Host -NoNewline "`r$display_percent $action"
    sleep 1
    $current_progress++
}

}


# After 7 minutes, the egg should be boiled
Write-Output "The egg is boiling ..."
reverse_counter 420 "boiled"
Write-Output "`nThe egg should be boiled by now..."
beep_beep


# After half an hour, the egg should be good to eat
reverse_counter 1800 "cooled"
Write-Output "`nThe egg can be eaten now. Bon Appetit!"
beep_beep
Read-Host "Press Enter to exit"

