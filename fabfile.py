from fabric import *
import time
api.env.user="fabric"
api.env.password="soumya"
api.env.hosts="172.31.84.34"
Time=time.localtime()
v_time=str(Time[0])+"_"+str(Time[1])+"_"+str(Time[2])+"-"+str(Time[3])+"."+str(Time[4])+"."+str(Time[5])
def tom_bkp():
	api.put("/root/fabric/Tomcat_bkp.py" , "/tmp/")
	api.run("python /tmp/Tomcat_bkp.py ")
	api.run("rm -rf /tmp/Tomcat_bkp.py /tmp/tom.txt")
	api.local("mkdir -p "+ v_time)
	api.get("/tmp/bkp/*" , "/root/fabric/"+v_time)
	api.run("rm -rf /tmp/bkp")
		
