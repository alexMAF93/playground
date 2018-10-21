<html>
 <head>
  <title>YouTube Downloader</title>
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

#$command = "/var/www/html/ytdl/youtube.py " . $_GET["videolink"];
#$output = shell_exec($command);

$last_item_cmd = "ls -t /var/www/html/ytdl/Downloaded | head -1";
$part_link = shell_exec($last_item_cmd);
$final_message = "<a class='buttonDownload' href='Downloaded/". $part_link . "'>".$part_link."</a>";
echo "<p align=center>Download your song here:</p>";
echo "<p align=center>" . $final_message . "</p>";


?>

<br><br><br>
<p align="center">
<a class="myButton" href="index.php">Next Conversion !</a>
</p>


 </body>
</html>
