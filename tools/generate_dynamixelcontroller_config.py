import argparse
import numpy

try:
    import cnoid.Body
    import cnoid.Util
except ImportError:
    import sys 
    sys.path.append('/choreonoid_ws/install/lib/choreonoid-1.8/python')
    import cnoid.Body
    import cnoid.Util



if __name__=='__main__':
    parser = argparse.ArgumentParser(
            prog='cnoid_dump_model.py', # プログラム名
            usage='Demonstration of cnoid_dump_model', # プログラムの利用方法

            add_help=True, # -h/–help オプションの追加
            )
    parser.add_argument('--bodyfile', type=str, default="robotname.body")

    args = parser.parse_args()
    fname = args.bodyfile

    rbody = cnoid.Body.BodyLoader().load(str(fname))
    rbody.updateLinkTree()
    rbody.initializePosition()
    rbody.calcForwardKinematics()

    rotate_joint_list = []

    num_link = rbody.getNumLinks()
    num_joint = rbody.getNumJoints()

    for idx in range(num_link):
        lk = rbody.getLink(idx)
        if lk.isRoot():
            continue
        p = lk.getParent()
        if p:
            if lk.isRevoluteJoint():
                rotate_joint_list.append(lk.getName())
    
    if len(rotate_joint_list)>0:
        for joint in rotate_joint_list:
            print('%s:'%(joint))
            print('  ID: 0')
            print('  Return_Delay_Time: 10')
            print('  Operating_Mode: 3')
