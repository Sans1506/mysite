<head>
	<title>UNIVERSITAS</title>
</head>
<body bgcolor="yellow">
	<h1 align="center"> UNIVERSITAS INDONESIA </h1>
	<p>
		<hr size="10 width" =1500 align="center">
	</p>
<?php
$no=$_POST['id'];
$Nama=$_POST['nama'];
$Alamat=$_POST['Alamat'];
$telepon=$_POST['Nomor'];
echo"
<center>
<table border='1'>
		<tr>
			<td cosplan='3' align='center'>Data Diri Peserta</td>
		</tr>
		<tr>
			<td>No.Formulir</td>
			<td>=</td>
			<td>$no</td>
		</tr>
		<tr>
			<td>Nama</td>
			<td>=</td>
			<td>$Nama</td>
		</tr>
		<tr>
			<td>Alamat</td>
			<td>=</td>
			<td>$Alamat</td>
		</tr>
		<tr>
			<td>No Telepon</td>
			<td>=</td>
			<td>$telepon</td>
		</tr>
</table>
<a href='Form.php'>Isi Kembali </a>";
?>
</body>

