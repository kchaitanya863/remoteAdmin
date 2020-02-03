# remoteAdmin
An all powerful tool for remote administration, in making!
Primary focus will be on getting Linux systems to have client and a Linux/docker server.
Tool shall be able to monitor/command "clients".

Server:

 - Store client metrics (Disk space, RAM, CPU,..) probably in Elasticsearch.
 - Chart client metrics
 - Have alerts on metrics
 - Remote Shell to client
 - Execute remote commands on client(s)
 - Manage processes on client OS.
 - Upload & Download files from clients
 - remote execute a shell script to client
 - expose client ports to internet using ngrok (not important)
 - Nice to have:
	 - Role based authentications
	 - Teams
	 - Timed team/Individual ssh time
	 - Alert Teams/Individuals on client not active

Client:

 - Send system metrics
 - Send additional metrics about custom services
 - Run server commands
 - Provide remote ssh