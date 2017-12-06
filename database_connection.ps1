[void][System.Reflection.Assembly]::LoadFrom("/home/mysql-connector-net/v4.0/MySql.Data.dll")

#Initiate the database connection
$db_server="localhost"
$db_user="hems_user"
$db_password="nF4mTRDT69RySz"
$database="hems"
$db_connection = New-Object MySql.Data.MySqlClient.MySqlConnection
$db_connection.ConnectionString = "server=$db_server;user id=$db_user;password=$db_password;database=$database;pooling=false"
$db_connection.Open()


$db_command = New-Object MySql.Data.MySqlClient.MySqlCommand
$db_command.Connection = $db_connection
$db_command.CommandText = "SHOW TABLES"
$reader = $db_command.ExecuteReader()
while($reader.Read()){ $reader.GetString(0) }
$db_connection.Close()