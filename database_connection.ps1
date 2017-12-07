#[void][System.Reflection.Assembly]::LoadFrom("/home/mysql-connector-net/v4.0/MySql.Data.dll")
[void][System.Reflection.Assembly]::LoadWithPartialName("MySql.Data")
#Initiate the database connection
$db_server="localhost"
$db_user="root"
$db_password="7S2Dh972m8k535"
$database="hems"
$db_connection = New-Object MySql.Data.MySqlClient.MySqlConnection
$db_connection.ConnectionString = "server=$db_server;uid=$db_user;pwd=$db_password;database=$database;"
$db_connection.Open()


#$db_command = New-Object MySql.Data.MySqlClient.MySqlCommand
#$db_command.Connection = $db_connection
#$db_command.CommandText = "SHOW TABLES"
#$reader = $db_command.ExecuteReader()
#while($reader.Read()){ $reader.GetString(0) }
#$db_connection.Close()
