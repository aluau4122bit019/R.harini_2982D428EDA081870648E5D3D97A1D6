<!DOPCTYPE html>
<html>
<head>
<title>
navigation example
</title>
</head>
<body>
<h1>
WELCOME TO MY WEBSITE
</h1>
<?php
if(isset($_GET['page']))
{
$page=$_GET['page'];
if($page==='home')
{
include('home.php');
}
elseif($page==='about')
{
include('about.php');
}
elseif($page==='contact')
{

include('contact.php');
}
}
?>
<hr>
<h3>
NAVIGATION
</h3>
<ul>
<li><a href="index.php?page=home">HOME</a></li>
<li><a href="index1.php?page=about">ABOUT</a></li>
<l><a href="index2.php?page=contact">CONTACT</a></li>
</ul>
</body>
</html>

