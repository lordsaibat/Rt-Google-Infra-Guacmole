#Metasploit
#Download Kali
FROM kalilinux/kali-rolling:latest

#Update the instance
RUN apt-get update 

#Add missing tools
RUN apt-get install metasploit-framework postgresql -y

#Start Postgres service
RUN service postgresql start && msfdb init

#Start Metasploit 
CMD service postgresql start; msfconsole
