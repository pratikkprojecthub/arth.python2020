#################################package  
import os
import getpass

os.system("clear")
passwd="arth_learner"
x=getpass.getpass("Enter the password for authetication:")
if x!=passwd:
	print("Wrong password!!!")
	exit()

print("Where you want to perform this menu (local/remote)",end=" ")
user=input()
if user=="remote":
	ip_address=input("Enter the ip address of remote system:")

os.system("clear")
while True:
	os.system("tput setaf 2")
	print("\t\t\tWelcome to menu driven program")
	print("\t\t\t==============================")

	os.system("tput setaf 6")
	print("""Press 1:To use AWS Technology
Press 2:To use Docker Technology
Press 3:To run Linux command
Press 4:To setup Networking stuff
Press 5:To manage Partitions of Harddisk
Press 6:To use Hadoop technology
Press 7:To Exit""")
	choice=int(input("Enter Your Choice:"))


	if user=="local":
		if choice==1:
			print("""===============================================================
Press 1:To configure AWS Linux.
Press 2:To login To AWS.
Press 3:To create Key Pair.
Press 4:To describe All Key Pairs.
Press 5:To create Security Group.
Press 6:To add Inbound Rule.
Press 7:To describe All Security Group. 
Press 8:To launch Instance.
Press 9:To create Ebs Volume. 
Press 10:To attach Ebs to Instance.
Press 11:To create S3 Bucket.
Press 12:To upload Object on S3 Bucket.
""")
			ch=int(input("Enter Your choice:"))
			if ch==1:
	    			os.system("curl ""https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip"" -o ""awscliv2.zip""")
	    			os.system("unzip awscliv2.zip")
	    			os.system("sudo ./aws/install")

			#Login to AWS
			elif ch==2:
	    			print("To configure aws just enter the Access key, Secret Access Key and the Region")
	    			os.system("aws configure")

			#Creating Key Pair
			elif ch==3:
	    			key_name=input("Enter the Key Name")
	    			os.system("aws ec2 create-key-pair --key-name {}".format(key_name))

			#Describe All key pair
			elif ch==4:
	    			print("All the keypairs are:")
	    			os.system("aws ec2 describe-key-pairs")

			#Creating security group
			elif ch==5:
	    			security_grp=input("Enter the Security Group Name")
	    			desc=input("Enter some description")
	    			os.system("aws ec2 create-security-group --group-name {} --description {}".format(security_grp,desc))

			#Adding inbound rules
			elif ch==6:
	    			security_grp=input("Enter the Security Group ID")
	    			protocol=input("Enter the protocol name")
	    			port=input("Enter the port number")
	    			cidr=input("Enter the CIDR which is 0.0.0.0/0 for allowing all traffic")
	    			os.system("aws ec2 authorize-security-group-ingress-group-id {} --protocol {} --port {} --cidr {}".format(security_grp,protocol,port,cidr))

			#describe all security groups
			elif ch==7:
	    			print("All the Security Groups are:")
	    			os.system("aws ec2 describe-security-groups")

			#launch instance
			elif ch==8:
				ami=input("Enter the AMI ID")
				instance_type=("Enter the instance type")
				subnet=input("Enter the subnet")
				security_grp=input("Enter the security group")
				key_name=input("Enter the Key Name")
				count=input("Enter the number of instances you want to launch")
				os.system("aws ec2 run-instances --image-id {} --instance-type {} --count {} --subnet-id {} --security-group {} --key-name {}".format(ami,instance_type,count,subnet,security_grp,key_name))

			#creating EBS Volume
			elif ch==9:
	    			v_type=input("Enter the Volume type like gp2")
	    			size=input("Enter the Sixe of the Volume")
	    			az=input("Enter the Availability Zone")
	    			os.system("aws ec2 create-volume --volume-type {] --size {} --availability-zone {}".format(v_type,size,az))

			#Attaching EBS Volume
			elif ch==10:
	    			v_id=input("Enter the Volume ID")
	    			instance_id=input("Enter the Instance ID")
	    			device=input("Enter the Device name like the /dev/sdf")
	    			os.system("aws ec2 attach-volume --volume-id {} --instance-id {} --device {}".format(v_id,instance_id,device))

			#Creating Bucket
			elif ch==11:
				b_name=input("Enter the Bucket Name")
				region=input("Enter the Region ID like the us-east-1")
				os.system("aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration LocationConstraint={}".format(b_name,region,region))

			#Uploading Object to the bucket
			elif ch==12:
	    			source=input("Enter the Object Local path")
	    			path=input("Enter the Bucket Path like s3://bucket_name")
	    			os.system("aws s3 cp {} {}".format(source,path))

		elif choice==2:
			print("""===============================================================
Press 1:To check where docker is installed or not.
Press 2:To check details information of docker.
Press 3:To check how many container is in running state.
Press 4:To see how many docker images are present.
Press 5:To download the docker images from docker hub.
Press 6:To lauch new docker container.
Press 7:To see the list of all the container currently running or stopped.
Press 8:To start the container.
Press 9:To get the command line of the container.
Press 10:To stop the container.
Press 11:To remove/delete/terminate the container.
Press 12:To launch container and run single command and then terminate the container.
Press 13:To remove/delete/terminate all the container in single go.
Press 14:To search a docker image.
Press 15:to see logs.
""")
			ch=int(input("Enter Your choice:"))
			if ch==1:
				os.system("rpm -q docker-ce")
			elif ch==2:
				os.system("docker info")
			elif ch==3:
				os.system("docker ps")
			elif ch==4:
				os.system("docker images")
			elif ch==5:
				image_name=input("Enter the name of docker image:")
				version=input("Enter the version of docker image:")
				os.system("docker pull {0}:{1}".format(image_name,version))
			elif ch==6:
				os.system("docker images")
				image_name=input("Enter the name of docker image:")
				version=input("Enter the version of docker image:")
				cont_name=input("With which name you want to launch the container:")
				os.system("docker run -it --name {0} {1}:{2}".format(cont_name, image_name,version))
			elif ch==7:
				os.system("docker ps -a")
			elif ch==8:
				os.system("docker ps -a")
				cont_name_id=input("Enter the container name or ID:")
				os.system("docker start {0}".format(cont_name_id))
			elif ch==9:
				os.system("docker ps")
				cont_name_id=input("Enter the container name or ID:")
				os.system("docker attach {0}".format(cont_name_id))
			elif ch==10:
				os.system("docker ps")
				cont_name_id=input("Enter the container name or ID:")
				os.system("docker stop {0}".format(cont_name_id))
			elif ch==11:
				os.system("docker ps -a")
				cont_name_id=input("ENter the container name or ID:")
				os.system("docker rm {0}".format(cont_name_id))
			elif ch==12:
				os.system("docker images")
				cont_name=input("Enter the docker image name:")
				version=input("Enter the version of container:")
				comnd=input("Enter the command that you want to run:")
				os.system("docker run -i {0}:{1} {2}".format(cont_name,version,comnd))
			elif ch==13:
				os.system("docker rm `docker ps -a -q`")
			elif ch==14:
				imge_name=input("Enter the name of docker image:")
				os.system("docker search {0}".format(imge_name))
			elif ch==15:
				os.system("docker ps")
				cont_name=input("Enter the container name:")
				os.system("docker logs {0}".format(cont_name))

		elif choice==3:
			print("""===============================================================
Press 1:To see the status of Filesystem/Harddisk.
Press 2:To see the Utilization of RAM/Memory.
Press 3:To clean cache memory.
Press 4:To create a empty file.
Press 5:To find the details of current running process.
Press 6:To create directory.
Press 7:To see date.
Press 8:To see calender.
Press 9:To check the list of port associated with which program.
Press 10:To check the details of CPU.
Press 11:To check current directory.
Press 12:To check logged in user ID.
Press 13:To find the PID of the program.
Press 14:To kill the process with PID.
""")
			ch=int(input("Enter Your Choice:"))
			if ch==1:
				os.system("df -h")
			elif ch==2:
				os.system("free -m")
			elif ch==3:
				exit_code=os.system("echo 3 > /proc/sys/vm/drop_caches")
				if exit_code==0:
					print("Caches clean successfully")
				else:
					print("Error while cleaning the cache")
			elif ch==4:
				filename=input("Enter the file name:")
				exit_code=os.system("touch {}".format(filename))
				if exit_code==0:
					print("File created successfully")
				else:
					print("Error while creating file")	
			elif ch==5:
				os.system("ps -aux")
			elif ch==6:
				path=input("Enter the path where you want to make directory:")
				os.system("mkdir {0}".format(path))
			elif ch==7:
				os.system("date")
			elif ch==8:
				os.system("cal")
			elif ch==9:
				os.system("netstat -tnlp")
			elif ch==10:
				os.system("lscpu")
			elif ch==11:
				os.system("pwd")
			elif ch==12:
				os.system("whoami")	
			elif ch==13:
				cmd=input("Enter the program name:")
				os.system("pgrep {0}".format(cmd))
			elif ch==14:
				pid=input("Enter the PID of a program:")
				os.system("kill {}".format(pid))		

		elif choice==4:
			print("""===============================================================
Press 1:To run the ping command
Press 2:To know the ip address of the os""")
			ch=int(input("Enter Your Choice:"))
			if ch==1:
				ip=input("Enter the Ip address of the system with which you want to check the connecivity:")
				exit_code=os.system("ping -c 3 {}".format(ip))
				os.system("tput setaf 1")
				if exit_code==0:
					print("Connectivity exist with IP {}".format(ip))
				else:
					print("Connectivity does not exist with IP {}".format(ip))
				os.system("tput setaf 6")
			elif ch==2:
				os.system("ifconfig")

		elif choice==5:
			print("""===============================================================
Press 1:To see the list of hardisk attached with Operating system.
Press 2:To make partitions or delete partitions of the harddisk.
Press 3:To load driver for newly created partitions.
Press 4:To format partitions.
Press 5:To mount partitions with folder.
Press 6:To unmount partition with folder.
Press 7:To create physical volume(PV).
Press 8:To see the status of physical volume(PV).
Press 9:To create volume group(VG).
Press 10:To see the status of Volume group(VG).
Press 11:To create logical volume(LV).
Press 12:To see the status of logical volume(LV).
Press 13:To format Logical volume(LV).
Press 14:To mount the Logical volume(LV) with folder.
Press 15:To extend the Logical Volume(LV).
Press 16:To format the extended part of Logical volume(LV).
Press 17:To extend the volume group.
""")
			ch=int(input("Enter Your Choice:"))
			if ch==1:
				os.system("fdisk -l")
			elif ch==2:
				os.system("fdisk -l")
				os.system("tput setaf 1")
				harddisk_name=input("Enter the hardisk name from the above details:")
				os.system("tput setaf 6")
				os.system("fdisk {}".format(harddisk_name))
			elif ch==3:
				exit_code=os.system("udevadm settle")
				if exit_code==0:
					print("Driver loaded successfully")
				else:
					print("Error while loading driver")
			elif ch==4:
				os.system("lsblk")
				partition_name=input("Enter the partition name from above details:")			
				exit_code=os.system("mkfs.ext4 /dev/{}".format(partition_name))
				if exit_code==0:
					print("partition formated successfully")
				else:
					print("Errror while formating partitions")
			elif ch==5:
				folder_status=input("for mounting,you want to create a new folder or mount on existing folder (new/existing):")
				if folder_status=="new":
					folder_name=input("Enter folder name:")
					exit_code=os.system("mkdir {}".format(folder_name))
					if exit_code==0:
						print("Folder created successfully")
					else:
						print("Error while creating folder")
				elif folder_status=="existing":
					folder_name=input("Enter the folder name:")
				else:
					print("Wrong input..")
				os.system("lsblk")
				partition_name=input("Enter the partition name from the above details:")
				exit_code=os.system("mount /dev/{0} {1}".format(partition_name,folder_name))
				if exit_code==0:
					print("partition mounted successfully")	
				else:
					print("Error while mounting partitions")
			elif ch==6:
				os.system("df -h")
				unmount_folder=input("Enter the folder name that you want to unmount from the above details:")
				exit_code=os.system("umount {}".format(unmount_folder))
				print(exit_code)
				if exit_code==0:
					print("Unmount done successfully")
				else:
					print("Error occured while unmounting")
			elif ch==7:
				os.system("lsblk")
				harddisk_name=input("Enter the hard disk name")
				os.system("pvcreate /dev/{0}".format(harddisk_name))		
			elif ch==8:
				os.system("pvdisplay")
			elif ch==9:
				os.system("pvdisplay")
				pv_name=input("Enter the name of different physical volume(PV) by giving space")
				vg_name=input("Enter the name of volume group(VG)")
				os.system("vgcreate {0} {1}".format(vg_name,pv_name))
			elif ch==10:
				os.system("vgdisplay")
			elif ch==11:
				os.system("vgdisplay")
				size=input("Enter the size of Logical volume (G:Gib,M:Mib):")
				lv_name=input("Enter the name of Logical volume(LV):")
				vg_name=input("Enter the name of Volume group(VG):")
				os.system("lvcreate --size {0} --name {1} {2}".format(size,lv_name,vg_name))
			elif ch==12:
				os.system("lvdisplay")
			elif ch==13:
				os.system("lvdisplay")
				vg_name=input("Enter the name of volume group(VG):")
				lv_name=input("Enter the name of logical volume(LV):")
				os.system("mkfs.ext4 /dev/{0}/{1}".format(vg_name,lv_name))
			elif ch==14:
				folder_status=input("for mounting,you want to create a new folder or mount on existing folder (new/existing):")
				if folder_status=="new":
					folder_name=input("Enter folder name:")
					os.system("mkdir {}".format(folder_name))
				elif folder_status=="existing":
					folder_name=input("Enter the folder name:")
				else:
					print("Wrong input..")
				os.system("lvdisplay")
				vg_name=input("Enter the name of volume group(VG):")
				lv_name=input("Enter the name of logical volume(LV):")
				os.system("mount /dev/{0}/{1} /{3}".format(vg_name,lv_name,folder_name))
			elif ch==15:
				os.system("lvdisplay")
				size=input("Enter the extended size of Logical volume (G:Gib,M:Mib):")
				vg_name=input("Enter the name of volume group(VG):")
				lv_name=input("Enter the name of logical volume(LV):")
				os.system("lvextend --size +{0} /dev/{1}/{2}".format(size,vg_name,lv_name))
			elif ch==16:
				os.system("lvdisplay")
				vg_name=input("Enter the name of volume group(VG):")
				lv_name=input("Enter the name of logical volume(LV):")
				os.system("resize2fs /dev/{0}/{1}".format(vg_name,lv_name))
			elif ch==17:
				os.system("lsblk")
				new_harddisk=input("Enter the name of new hard disk:")
				vg_name=input("Enter the name of volume group(VG):")
				os.system("vgextend {0} /dev/{1}".format(vg_name,new_harddisk))
					

		elif choice==6:
			print("""=====================================================
Press 1:Check Java and Hadoop Software Installed or not
Press 2:Configure a System as a Node (Name/Data/Client)
Press 3:Start Node (Name/Data)
Press 4:Check the Service is Started or not
Press 5:Check the Report of HDFS
Press 6:Upload File in HDFS
Press 7:Back in main menu""")
			ch=int(input("Enter Your Choice:"))
			if ch==1:
				os.system("java -version")
				os.system("hadoop -version")
			elif ch==2:
				while True:
					print("""***************************************
Press 1:for make system as a Name-node
Press 2:format the Name-node
Press 3:for make system as a Data-node
Press 4:for make system as a Client-node
Press 5:Back to HDFS Cluster menu..""")
					n = input("Press Valid Number to make system as Node: ")
					if int(n)==1:
						f = input("Type folder name: ")
						os.system("mkdir /{}".format(f))
						print("/{} is Created".format(f))
						os.system("vim /etc/hadoop/hdfs-site.xml")
						os.system("vim /etc/hadoop/core-site.xml")
					elif int(n)==2:
						os.system("hadoop namenode -format")
					elif int(n)==3:
						f = input("Type folder name: ")
						os.system("mkdir /{}".format(f))
						print("/{} is Created".format(f))
						os.system("vim /etc/hadoop/hdfs-site.xml")
						os.system("vim /etc/hadoop/core-site.xml")
					elif int(n)==4:
						os.system("vim /etc/hadoop/core-site.xml")
					elif int(n)==5:
						os.system("clear")
						break
					else:
						print("Enter the valid Option")
			elif ch==3:
				while True:
					print("""***************************************
Press 1:for Start the Name-node
Press 2:for Start the Data-node
Press 3:back to HDFS Cluster menu""")
					s=input("Enter your choice:")
					if int(s)==1:
						os.system("hadoop-daemon.sh start namenode")
					elif int(s)==2:
						os.system("hadoop-daemon.sh start datanode")
					elif int(s)==3:
						os.system("clear")
						break
					else:
						print("Enter the valid Options")
			elif ch==4:
				os.system("jps")

			elif ch==5:
				os.system("hadoop dfsadmin -report")

			elif ch==6:
				f = input("Enter the Location/name of file: ")
				os.system("hadoop fs -put {}".format(f))

			elif ch==7:
				os.system("clear")
				continue

			else:
				print("Enter the valid Option")


		
		elif choice==7:
			print("Thanks for using this software.Have a nice day.")
			exit()

		else:
			print("Wrong choice")

	elif user=="remote":
		if choice==1:
			print("""===============================================================
Press 1:To configure AWS Linux.
Press 2:To login To AWS.
Press 3:To create Key Pair.
Press 4:To describe All Key Pairs.
Press 5:To create Security Group.
Press 6:To add Inbound Rule.
Press 7:To describe All Security Group. 
Press 8:To launch Instance.
Press 9:To create Ebs Volume. 
Press 10:To attach Ebs to Instance.
Press 11:To create S3 Bucket.
Press 12:To upload Object on S3 Bucket.
""")
			ch=int(input("Enter Your choice:"))
			if ch==1:
	    			os.system("ssh {0} curl ""https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip"" -o ""awscliv2.zip""".format(ip_address))
	    			os.system("ssh {0} unzip awscliv2.zip".format(ip_address))
	    			os.system("ssh {0} sudo ./aws/install".format(ip_address))

			#Login to AWS
			elif ch==2:
	    			print("To configure aws just enter the Access key, Secret Access Key and the Region")
	    			os.system("ssh {0} aws configure".format(ip_address))

			#Creating Key Pair
			elif ch==3:
	    			key_name=input("Enter the Key Name")
	    			os.system("ssh {0} aws ec2 create-key-pair --key-name {1}".format(ip_address,key_name))

			#Describe All key pair
			elif ch==4:
	    			print("All the keypairs are:")
	    			os.system("ssh {0} aws ec2 describe-key-pairs".format(ip_address))

			#Creating security group
			elif ch==5:
	    			security_grp=input("Enter the Security Group Name")
	    			desc=input("Enter some description")
	    			os.system("ssh {0} aws ec2 create-security-group --group-name {1} --description {2}".format(ip_address,security_grp,desc))

			#Adding inbound rules
			elif ch==6:
	    			security_grp=input("Enter the Security Group ID")
	    			protocol=input("Enter the protocol name")
	    			port=input("Enter the port number")
	    			cidr=input("Enter the CIDR which is 0.0.0.0/0 for allowing all traffic")
	    			os.system("ssh {0} aws ec2 authorize-security-group-ingress-group-id {1} --protocol {2} --port {3} --cidr {}".format(ip_address,security_grp,protocol,port,cidr))

			#describe all security groups
			elif ch==7:
	    			print("All the Security Groups are:")
	    			os.system("ssh {0} aws ec2 describe-security-groups".format(ip_address))

			#launch instance
			elif ch==8:
				ami=input("Enter the AMI ID")
				instance_type=("Enter the instance type")
				subnet=input("Enter the subnet")
				security_grp=input("Enter the security group")
				key_name=input("Enter the Key Name")
				count=input("Enter the number of instances you want to launch")
				os.system("ssh {0} aws ec2 run-instances --image-id {1} --instance-type {2} --count {3} --subnet-id {4} --security-group {5} --key-name {6}".format(ip_address,ami,instance_type,count,subnet,security_grp,key_name))

			#creating EBS Volume
			elif ch==9:
	    			v_type=input("Enter the Volume type like gp2")
	    			size=input("Enter the Sixe of the Volume")
	    			az=input("Enter the Availability Zone")
	    			os.system("ssh {0} aws ec2 create-volume --volume-type {1} --size {2} --availability-zone {3}".format(ip_address,v_type,size,az))

			#Attaching EBS Volume
			elif ch==10:
	    			v_id=input("Enter the Volume ID")
	    			instance_id=input("Enter the Instance ID")
	    			device=input("Enter the Device name like the /dev/sdf")
	    			os.system("ssh {0} aws ec2 attach-volume --volume-id {1} --instance-id {2} --device {3}".format(ip_address,v_id,instance_id,device))

			#Creating Bucket
			elif ch==11:
				b_name=input("Enter the Bucket Name")
				region=input("Enter the Region ID like the us-east-1")
				os.system("ssh {0} aws s3api create-bucket --bucket {1} --region {2} --create-bucket-configuration LocationConstraint={3}".format(ip_address,b_name,region,region))

			#Uploading Object to the bucket
			elif ch==12:
	    			source=input("Enter the Object Local path")
	    			path=input("Enter the Bucket Path like s3://bucket_name")
	    			os.system("ssh {0} aws s3 cp {1} {2}".format(ip_address,source,path))


		elif choice==2:
			print("""===============================================================
Press 1:To check where docker is installed or not.
Press 2:To check details information of docker.
Press 3:To check how many container is in running state.
Press 4:To see how many docker images are present.
Press 5:To download the docker images from docker hub.
Press 6:To lauch new docker container.
Press 7:To see the list of all the container currently running or stopped.
Press 8:To start the container.
Press 9:To get the command line of the container.
Press 10:To stop the container.
Press 11:To remove/delete/terminate the container.
Press 12:To launch container and run single command and then terminate the container.
Press 13:To remove/delete/terminate all the container in single go.
Press 14:To search a docker image.
Press 15:to see logs.
""")
			ch=int(input("Enter Your choice:"))
			if ch==1:
				os.system("ssh {0} rpm -q docker-ce".format(ip_address))
			elif ch==2:
				os.system("ssh {0} docker info".format(ip_address))
			elif ch==3:
				os.system("ssh {0} docker ps".format(ip_address))
			elif ch==4:
				os.system("ssh {0} docker images".format(ip_address))
			elif ch==5:
				image_name=input("Enter the name of docker image:")
				version=input("Enter the version of docker image:")
				os.system("ssh {0} docker pull {1}:{2}".format(ip_address,image_name,version))
			elif ch==6:
				os.system("ssh {0} docker images".format(ip_address))
				image_name=input("Enter the name of docker image:")
				version=input("Enter the version of docker image:")
				cont_name=input("With which name you want to launch the container:")
				os.system("ssh {0} docker run -it --name {1} {2}:{3}".format(ip_address,cont_name, image_name,version))
			elif ch==7:
				os.system("ssh {0} docker ps -a".format(ip_address))
			elif ch==8:
				os.system("ssh {0} docker ps -a".format(ip_address))
				cont_name_id=input("Enter the container name or ID:")
				os.system("ssh {0} docker start {1}".format(ip_address,cont_name_id))
			elif ch==9:
				os.system("ssh {0} docker ps".format(ip_address))
				cont_name_id=input("Enter the container name or ID:")
				os.system("ssh {0} docker attach {1}".format(ip_address,cont_name_id))
			elif ch==10:
				os.system("ssh {0} docker ps".format(ip_address))
				cont_name_id=input("Enter the container name or ID:")
				os.system("ssh {0} docker stop {1}".format(ip_address,cont_name_id))
			elif ch==11:
				os.system("ssh {0} docker ps -a".format(ip_address))
				cont_name_id=input("ENter the container name or ID:")
				os.system("ssh {0} docker rm {1}".format(ip_address,cont_name_id))
			elif ch==12:
				os.system("ssh {0} docker images".format(ip_address))
				cont_name=input("Enter the docker image name:")
				version=input("Enter the version of container:")
				comnd=input("Enter the command that you want to run:")
				os.system("ssh {0} docker run -i {1}:{2} {3}".format(ip_address,cont_name,version,comnd))
			elif ch==13:
				os.system("ssh {0} docker rm `docker ps -a -q`".format(ip_address))
			elif ch==14:
				imge_name=input("Enter the name of docker image:")
				os.system("ssh {0} docker search {1}".format(ip_address,imge_name))
			elif ch==15:
				os.system("ssh {0} docker ps".format(ip_address))
				cont_name=input("Enter the container name:")
				os.system("ssh {0} docker logs {1}".format(ip_address,cont_name))


		elif choice==3:
			print("""===============================================================
Press 1:To see the status of Filesystem/Harddisk.
Press 2:To see the Utilization of RAM/Memory.
Press 3:To clean cache memory.
Press 4:To create a empty file.
Press 5:To find the details of current running process.
Press 6:To create directory.
Press 7:To see date.
Press 8:To see calender.
Press 9:To check the list of port associated with which program.
Press 10:To check the details of CPU.
Press 11:To check current directory.
Press 12:To check logged in user ID.
Press 13:To find the PID of the program.
Press 14:To kill the process with PID.
""")
			ch=int(input("Enter Your Choice:"))
			if ch==1:
				os.system("ssh {0} df -h".format(ip_address))
			elif ch==2:
				os.system("ssh {0} free -m".format(ip_address))
			elif ch==3:
				exit_code=os.system("ssh {0} echo 3 > /proc/sys/vm/drop_caches".format(ip_address))
				if exit_code==0:
					print("Caches clean successfully")
				else:
					print("Error while cleaning the cache")
			elif ch==4:
				filename=input("Enter the file name:")
				exit_code=os.system("ssh {0} touch {1}".format(ip_address,filename))
				if exit_code==0:
					print("File created successfully")
				else:
					print("Error while creating file")	
			elif ch==5:
				os.system("ssh {0} ps -aux".format(ip_address))
			elif ch==6:
				path=input("Enter the path where you want to make directory:")
				os.system("ssh {0} mkdir {1}".format(ip_address,path))
			elif ch==7:
				os.system("ssh {0} date".format(ip_address))
			elif ch==8:
				os.system("ssh {0} cal".format(ip_address))
			elif ch==9:
				os.system("ssh {0} netstat -tnlp".format(ip_address))
			elif ch==10:
				os.system("ssh {0} lscpu".format(ip_address))
			elif ch==11:
				os.system("ssh {0} pwd".format(ip_address))
			elif ch==12:
				os.system("ssh {0} whoami".format(ip_address))	
			elif ch==13:
				cmd=input("Enter the program name:")
				os.system("ssh {0} pgrep {1}".format(ip_address,cmd))
			elif ch==14:
				pid=input("Enter the PID of a program:")
				os.system("ssh {0} kill {1}".format(ip_address,pid))		


		elif choice==4:
			print("""===============================================================
Press 1:To run the ping command
Press 2:To know the ip address of the os""")
			ch=int(input("Enter Your Choice:"))
			if ch==1:
				ip=input("Enter the Ip address of the system with which you want to check the connecivity:")
				exit_code=os.system("ssh {0} ping -c 3 {1}".format(ip_address,ip))
				os.system("tput setaf 1")
				if exit_code==0:
					print("Connectivity exist with IP {}".format(ip))
				else:
					print("Connectivity does not exist with IP {}".format(ip))
				os.system("tput setaf 6")
			elif ch==2:
				os.system("ssh {0} ifconfig".format(ip_address))


		elif choice==5:
			print("""===============================================================
Press 1:To see the list of hardisk attached with Operating system.
Press 2:To make partitions or delete partitions of the harddisk.
Press 3:To load driver for newly created partitions.
Press 4:To format partitions.
Press 5:To mount partitions with folder.
Press 6:To unmount partition with folder.
Press 7:To create physical volume(PV).
Press 8:To see the status of physical volume(PV).
Press 9:To create volume group(VG).
Press 10:To see the status of Volume group(VG).
Press 11:To create logical volume(LV).
Press 12:To see the status of logical volume(LV).
Press 13:To format Logical volume(LV).
Press 14:To mount the Logical volume(LV) with folder.
Press 15:To extend the Logical Volume(LV).
Press 16:To format the extended part of Logical volume(LV).
Press 17:To extend the volume group.
""")
			ch=int(input("Enter Your Choice:"))
			if ch==1:
				os.system("ssh {0} fdisk -l".format(ip_address))
			elif ch==2:
				os.system("ssh {0} fdisk -l".format(ip_address))
				os.system("tput setaf 1")
				harddisk_name=input("Enter the hardisk name from the above details:")
				os.system("tput setaf 6")
				os.system("ssh {0} fdisk {1}".format(ip_address,harddisk_name))
			elif ch==3:
				exit_code=os.system("ssh {0} udevadm settle".format(ip_address))
				if exit_code==0:
					print("Driver loaded successfully")
				else:
					print("Error while loading driver")
			elif ch==4:
				os.system("ssh {0} lsblk".format(ip_address))
				partition_name=input("Enter the partition name from above details:")			
				exit_code=os.system("ssh {0} mkfs.ext4 /dev/{1}".format(ip_address,partition_name))
				if exit_code==0:
					print("partition formated successfully")
				else:
					print("Errror while formating partitions")
			elif ch==5:
				folder_status=input("for mounting,you want to create a new folder or mount on existing folder (new/existing):")
				if folder_status=="new":
					folder_name=input("Enter folder name:")
					exit_code=os.system("ssh {0} mkdir {1}".format(ip_address,folder_name))
					if exit_code==0:
						print("Folder created successfully")
					else:
						print("Error while creating folder")
				elif folder_status=="existing":
					folder_name=input("Enter the folder name:")
				else:
					print("Wrong input..")
				os.system("ssh {0} lsblk".format(ip_address))
				partition_name=input("Enter the partition name from the above details:")
				exit_code=os.system("ssh {0} mount /dev/{1} {2}".format(ip_address,partition_name,folder_name))
				if exit_code==0:
					print("partition mounted successfully")	
				else:
					print("Error while mounting partitions")
			elif ch==6:
				os.system("ssh {0} df -h".format(ip_address))
				unmount_folder=input("Enter the folder name that you want to unmount from the above details:")
				exit_code=os.system("ssh {0} umount {1}".format(ip_address,unmount_folder))
				print(exit_code)
				if exit_code==0:
					print("Unmount done successfully")
				else:
					print("Error occured while unmounting")
			elif ch==7:
				os.system("ssh {0} lsblk".format(ip_address))
				harddisk_name=input("Enter the hard disk name")
				os.system("ssh {0} pvcreate /dev/{1}".format(ip_address,harddisk_name))		
			elif ch==8:
				os.system("ssh {0} pvdisplay".format(ip_address))
			elif ch==9:
				os.system("ssh {0} pvdisplay".format(ip_address))
				pv_name=input("Enter the name of different physical volume(PV) by giving space")
				vg_name=input("Enter the name of volume group(VG)")
				os.system("ssh {0} vgcreate {1} {2}".format(ip_address,vg_name,pv_name))
			elif ch==10:
				os.system("ssh {0} vgdisplay".format(ip_address))
			elif ch==11:
				os.system("ssh {0} vgdisplay".format(ip_address))
				size=input("Enter the size of Logical volume (G:Gib,M:Mib):")
				lv_name=input("Enter the name of Logical volume(LV):")
				vg_name=input("Enter the name of Volume group(VG):")
				os.system("ssh {0} lvcreate --size {1} --name {2} {3}".format(ip_address,size,lv_name,vg_name))
			elif ch==12:
				os.system("ssh {0} lvdisplay".format(ip_address))
			elif ch==13:
				os.system("ssh {0} lvdisplay".format(ip_address))
				vg_name=input("Enter the name of volume group(VG):")
				lv_name=input("Enter the name of logical volume(LV):")
				os.system("ssh {0} mkfs.ext4 /dev/{1}/{2}".format(ip_address,vg_name,lv_name))
			elif ch==14:
				folder_status=input("for mounting,you want to create a new folder or mount on existing folder (new/existing):")
				if folder_status=="new":
					folder_name=input("Enter folder name:")
					os.system("ssh {0} mkdir {1}".format(ip_address,folder_name))
				elif folder_status=="existing":
					folder_name=input("Enter the folder name:")
				else:
					print("Wrong input..")
					input("Enter to continue...")
					os.system("clear")
					continue
				os.system("ssh {0} lvdisplay".format(ip_address))
				vg_name=input("Enter the name of volume group(VG):")
				lv_name=input("Enter the name of logical volume(LV):")
				os.system("ssh {0} mount /dev/{1}/{2} /{3}".format(ip_address,vg_name,lv_name,folder_name))
			elif ch==15:
				os.system("ssh {0} lvdisplay".format(ip_address))
				size=input("Enter the extended size of Logical volume (G:Gib,M:Mib):")
				vg_name=input("Enter the name of volume group(VG):")
				lv_name=input("Enter the name of logical volume(LV):")
				os.system("ssh {0} lvextend --size +{1} /dev/{2}/{3}".format(ip_address,size,vg_name,lv_name))
			elif ch==16:
				os.system("ssh {0} lvdisplay".format(ip_address))
				vg_name=input("Enter the name of volume group(VG):")
				lv_name=input("Enter the name of logical volume(LV):")
				os.system("ssh {0} resize2fs /dev/{1}/{2}".format(ip_address,vg_name,lv_name))
			elif ch==17:
				os.system("ssh {0} lsblk".format(ip_address))
				new_harddisk=input("Enter the name of new hard disk:")
				vg_name=input("Enter the name of volume group(VG):")
				os.system("ssh {0} vgextend {1} /dev/{2}".format(ip_address,vg_name,new_harddisk))


		elif choice==6:
			print("""=====================================================
Press 1:Check Java and Hadoop Software Installed or not
Press 2:Configure a System as a Node (Name/Data/Client)
Press 3:Start Node (Name/Data)
Press 4:Check the Service is Started or not
Press 5:Check the Report of HDFS
Press 6:Upload File in HDFS
Press 7:Back in main menu""")
			ch=int(input("Enter Your Choice:"))
			if ch==1:
				os.system("ssh {0} java -version".format(ip_address))
				os.system("ssh {0} hadoop -version".format(ip_address))
			elif ch==2:
				while True:
					print("""***************************************
Press 1:for make system as a Name-node
Press 2:format the Name-node
Press 3:for make system as a Data-node
Press 4:for make system as a Client-node
Press 5:Back to HDFS Cluster menu..""")
					n = input("Press Valid Number to make system as Node: ")
					if int(n)==1:
						f = input("Type folder name: ")
						os.system("ssh {0} mkdir /{1}".format(ip_address,f))
						print("/{} is Created".format(f))
						os.system("ssh {0} vim /etc/hadoop/hdfs-site.xml".format(ip_address))
						os.system("ssh {0} vim /etc/hadoop/core-site.xml".format(ip_address))
					elif int(n)==2:
						os.system("ssh {0} hadoop namenode -format".format(ip_address))
					elif int(n)==3:
						f = input("Type folder name: ")
						os.system("ssh {0} mkdir /{1}".format(ip_address,f))
						print("ssh {0} /{1} is Created".format(ip_address,f))
						os.system("ssh {0} vim /etc/hadoop/hdfs-site.xml".format(ip_address))
						os.system("ssh {0} vim /etc/hadoop/core-site.xml".format(ip_address))
					elif int(n)==4:
						os.system("ssh {0} vim /etc/hadoop/core-site.xml".format(ip_address))
					elif int(n)==5:
						os.system("ssh {0} clear".format(ip_address))
						break
					else:
						print("Enter the valid Option")
			elif ch==3:
				while True:
					print("""***************************************
Press 1:for Start the Name-node
Press 2:for Start the Data-node
Press 3:back to HDFS Cluster menu""")
					s=input("Enter your choice:")
					if int(s)==1:
						os.system("ssh {0} hadoop-daemon.sh start namenode".format(ip_address))
					elif int(s)==2:
						os.system("ssh {0} hadoop-daemon.sh start datanode".format(ip_address))
					elif int(s)==3:
						os.system("ssh {0} clear".format(ip_address))
						break
					else:
						print("Enter the valid Options")
			elif ch==4:
				os.system("ssh {0} jps".format(ip_address))

			elif ch==5:
				os.system("ssh {0} hadoop dfsadmin -report".format(ip_address))

			elif ch==6:
				f = input("Enter the Location/name of file: ")
				os.system("ssh {0} hadoop fs -put {1}".format(ip_address,f))

			elif ch==7:
				os.system("ssh {0} clear".format(ip_address))
				continue

			else:
				print("Enter the valid Option")


		elif choice==7:
			print("Thanks for using this software.Have a nice day.")
			exit()

		else:
			print("Wrong choice")

	else:  
		print("WRONG INPUT!!")

	os.system("tput setaf 7")
	input("Press 'enter' to continue..")
	os.system("clear")
