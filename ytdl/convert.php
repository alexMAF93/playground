<html>
 <head>
  <title>Converting your video</title>
<link rel="stylesheet" href="styles.css">
 </head>
 <body>

<!-- The text box -->

<br>
<br>
<br>
<br>
<br>


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

</body>
</html>



