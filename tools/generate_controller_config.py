import argparse
import numpy
import cnoid.Body
import cnoid.Util

def print_geom (filename = '', visual = True, scale = '1 1 1', xyz = '0 0 0', rpy = '0 0 0'):
    if visual:
        print('    <visual>')
    else:
        print('    <collisionl>')
    print('      <origin  xyz="%s" rpy="%s"/>'%(xyz, rpy))
    print('      <geometry>')
    print('        <mesh filename="%s" scale="%s"/>'%(filename, scale))
    print('      </geometry>')
    if visual:
        print('    </visual>')
    else:
        print('    </collisionl>')

def print_inertial (mass = 1.0, xyz = '0 0 0', rpy = '0 0 0', inertial = [1, 0, 0, 1, 0, 1]):
    print('    <inertial>')
    print('      <mass value="%s"/>'%(mass))
    print('      <origin xyz="%s" rpy="%s"/>'%(xyz, rpy))
    print('      <inertia ixx="%f" ixy="%f" ixz="%f" iyy="%f" iyz="%f" izz="%f"/>'%(inertial[0], inertial[1], inertial[2],
                                                                                      inertial[3], inertial[4], inertial[5]))
    print('    </inertial>')


if __name__=='__main__':
    parser = argparse.ArgumentParser(
            prog='cnoid_dump_model.py', # プログラム名
            usage='Demonstration of cnoid_dump_model', # プログラムの利用方法

            add_help=True, # -h/–help オプションの追加
            )
    parser.add_argument('--bodyfile', type=str, default="robotname.body")
    args = parser.parse_args()
    # fname = 'robotname.body'
    fname = args.bodyfile

    rbody = cnoid.Body.BodyLoader().load(str(fname))
    print('%s:'%rbody.getModelName())
    print('  joint_controler:')
    print('    type: "position_controllers/JointTrajectoryController"')

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
        print("    joints:")
        for joint in rotate_joint_list:
            print('      - %s'%joint)
        print("    gains:")
        for joint in rotate_joint_list:
            print('      %s:'%joint)
            print('        p: 100')
            print('        i: 10')
            print('        d: 1')