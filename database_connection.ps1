[void][System.Reflection.Assembly]::LoadFrom("/home/mysql-connector-net/v4.5/MySql.Data.dll")

#Add-Type –Path "/home/mysql-connector-net/v4.5/MySql.Data.dll"
#Initiate the database connection
$db_server="localhost"
$db_user="root"
$db_password="7S2Dh972m8k535"
$database="hems"
$Connection = [MySql.Data.MySqlClient.MySqlConnection]@{ConnectionString='server=localhost;uid=root;pwd=7S2Dh972m8k535;database=hems'}
$Connection.Open()


#$db_command = New-Object MySql.Data.MySqlClient.MySqlCommand
#$db_command.Connection = $db_connection
#$db_command.CommandText = "SHOW TABLES"
#$reader = $db_command.ExecuteReader()
#while($reader.Read()){ $reader.GetString(0) }
$Connection.Close()
