from general.connection import MySSH
from general.server_details import server_details_dict
from threading import Thread
import pdb
import re
from datetime import timedelta
import pprint
#########################
class ApData:
    pass

# Create the SSH connection
ApData.dic = {}
ApData.cmd_out_dic = {}
def _connect(hst_n, hst_d):
    try:
        ApData.dic[str(hst_n)] = MySSH()
        ApData.dic[str(hst_n)].set_verbosity(False)
        ApData.dic[str(hst_n)].connect(hostname=hst_n,
                                        username=hst_d['username'],
                                        password=hst_d['password'],
                                        port=22)
        ApData.dic.update()
        if ApData.dic[str(hst_n)].connected() is False:
            print('ERROR: connection failed for host {}.'.format(
                ApData.dic[str(hst_n)]))
    except Exception as err:
        print("ERROR: {}".format(err))

def _run(con_obj, cmd, *args,**kwrgs):    
    print('=' * 64)
    print('command: %s' % (cmd))
    ApData.cmd_out_dic[con_obj] = {}
    for command in cmd:
        status, output = ApData.dic[con_obj].run(command)
        ApData.cmd_out_dic[con_obj][command] = output
        ApData.cmd_out_dic[con_obj].update()
        ApData.cmd_out_dic.update()
    print('status : %d' % (status))
    print('output : %d bytes' % (len(output)))
    print('=' * 64)
    print('%s' % (output))
    return ApData.cmd_out_dic
def start_exec(cmd, indata=None):
    '''
    Run a command with optional input.

    @param cmd    The command to execute.
    @param indata The input data.
    @returns The command exit status and output.
             Stdout and stderr are combined.
    '''
    for hst_name,details in server_details_dict.items():
        conn_thread = Thread(target=_connect, args=(hst_name, details))
        conn_thread.start()
        conn_thread.join()
    for conn_obj in ApData.dic:
        print('*' * 64)
        print("For Host: {} ".format(conn_obj))
        print('*' * 64)
        output = _run(conn_obj, cmd)
    return output
        # cmd_thread = Thread(target=_run, args=(conn_obj, cmd))
        # cmd_thread.start()
        # conn_thread.join()

def get_platform(command):
    #start_exec(['uname -a'])
    load_details = {}
    try:
        print(ApData.cmd_out_dic)
        for hst in ApData.cmd_out_dic:
            model = ApData.cmd_out_dic[hst][command]
            print("ss",model)

            load_details = model
    except Exception as err:
        print(err) 
    return load_details
