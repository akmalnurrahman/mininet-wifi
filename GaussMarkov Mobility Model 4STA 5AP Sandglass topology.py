import sys

from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi


def topology(args):
    "Create a network."
    net = Mininet_wifi()

    info("*** Creating nodes\n")
    sta1 = net.addStation('sta1', mac='00:00:00:00:00:02', ip='10.0.0.2/8',range ='10',
                   min_x=0, max_x=160, min_y=0, max_y=160)
    sta2 = net.addStation('sta2', mac='00:00:00:00:00:04', ip='10.0.0.3/8',range ='10',
                   min_x=10, max_x=80, min_y=10, max_y=80)
    sta3 = net.addStation('sta3', mac='00:00:00:00:00:05', ip='10.0.0.4/8',range ='10',
                   min_x=20, max_x=160, min_y=20, max_y=160)
    sta4 = net.addStation('sta4', mac='00:00:00:00:00:06', ip='10.0.0.5/8',range ='10',
                   min_x=80, max_x=160, min_y=80, max_y=160)
    ap1 = net.addAccessPoint('ap1',  ssid='ssid1', mode='g',channel='1', failMode="standalone",position='80,80,0',range='20')
    ap2 = net.addAccessPoint('ap2', ssid='ssid2', mode='g',channel='1', failMode="standalone",position='100,140,0',range='20')
    ap3 = net.addAccessPoint('ap3', ssid='ssid3', mode='g',channel='1', failMode="standalone",position='60,140,0',range='20')
    ap4 = net.addAccessPoint('ap4', ssid='ssid4', mode='g',channel='1', failMode="standalone",position='100,20,0',range='20')
    ap5 = net.addAccessPoint('ap5', ssid='ssid5', mode='g',channel='1', failMode="standalone",position='60,20,0',range='20')
    

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()
    
    info("*** Configuring propagation model\n")
    net.setPropagationModel(model="logDistance", exp=4.5)

    
    info("*** Associating and Creating links\n")
    net.addLink(ap1,ap2)
    net.addLink(ap1,ap3)
    net.addLink(ap1,ap4)
    net.addLink(ap1,ap5)
    net.addLink(ap2,ap3)
    net.addLink(ap4,ap5)

    if '-p' not in args:
        net.plotGraph()
       

    net.setMobilityModel(time=0, model='GaussMarkov', max_x=160, max_y=160, seed=20)

    info("*** Starting network\n")
    net.build()
    ap1.start([])
    ap2.start([])

    info("*** Running CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology(sys.argv)
