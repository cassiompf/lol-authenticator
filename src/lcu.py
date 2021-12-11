import os

class LcuInfo:
  def __init__(self):
    info_cmd = os.popen("wmic PROCESS WHERE name='RiotClientUx.exe' GET commandline").read()
    remoting_auth_label = "--remoting-auth-token="
    app_port_label = "--app-port="
    
    index_after_remoting_auth_label = info_cmd.find(remoting_auth_label) + len(remoting_auth_label)
    index_after_app_port_label = info_cmd.find(app_port_label) + len(app_port_label)
    
    self.remoting_auth_token = info_cmd[index_after_remoting_auth_label:(index_after_remoting_auth_label + 22)]
    self.access_port = int(info_cmd[index_after_app_port_label:(index_after_app_port_label + 5)])
