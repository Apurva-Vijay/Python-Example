import threading
import paramiko
import time
import ip_config as config

class Connectionestab:
    def __init__(self,ip,user,password):
        print("inisde Comnect class")
        self.ip = ip
        self.user = user
        self.password = password

    def create_ssh_connection(self,name,delay):
        try:
            print("values received",self.ip,self.user,self.password)
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(self.ip, username=self.user, password=self.password)
            print("Connection Established!!!!!\n")
            print(name," thread executing")
            time.sleep(delay)
        except Exception as e:
            print(e)

        finally:
            ssh_client.close()



class myThread:
    def __init__(self,num_of_thread,delay):
        print("insiode thread class")
        self.num_of_thread = num_of_thread
        self.delay = delay
        self.connection_object = Connectionestab(<<<IP>>>,<<<USERNAME>>>,<<<PASSWORD>>>)

    def run_my_threads(self):
        threadlist = []
        for t in range(self.num_of_thread):
            try:
                t = threading.Thread(target = self.connection_object.create_ssh_connection,args = ("Thread -->"+str(t),self.delay))
                threadlist.append(t)
                t.start()
            except Exception as e:
                print(e,"----->message")
        for t in threadlist:
            t.join()

thread = myThread(5,4)
thread.run_my_threads()
print("Exiting from main Thread")