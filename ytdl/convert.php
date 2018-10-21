<?php
echo "Converting";
$command = "/var/www/html/ytdl/youtube.py " . $_POST["videolink"];
if ($_POST["videolink"] != '')
{
$output = shell_exec($command);
header("Location: downloaded.php");
}
else
{
header("Location: index.php");
}
?>
