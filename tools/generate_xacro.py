import argparse
import numpy
import cnoid.Body
import cnoid.Util

if __name__=='__main__':
    parser = argparse.ArgumentParser(
            prog='generate_xacro.py', # プログラム名
            usage='Demonstration of cnoid_dump_model', # プログラムの利用方法

            add_help=True, # -h/–help オプションの追加
            )
    parser.add_argument('--bodyfile', type=str, default="robotname.body")
    parser.add_argument('--jointsuffix', type=str, default="")
    args = parser.parse_args()

    fname = args.bodyfile
    joint_suffix = args.jointsuffix
    rbody = cnoid.Body.BodyLoader().load(str(fname))

    num_link = rbody.getNumLinks()
    num_joint = rbody.getNumJoints()

    print('<?xml version="1.0" ?>')
    print(' '*2+'<robot name="{}" xmlns:xacro="http://ros.org/wiki/xacro">'.format(rbody.getModelName()))
    print(' '*2+'<xacro:include filename="$(find choreonoid_ros_control_assembler_sample)/urdf/common.xacro"/>')

    joint_position_list = []

    for idx in range(num_link):
        lk = rbody.getLink(idx)
        print(' '*2 + '<link name="%s">'%lk.getName())
        print(' '*2 + '</link>')
        if lk.isRoot():
            continue
        p = lk.getParent()
        if p:
            # print(lk.getJointType())
            axis  = lk.getJointAxis()
            l_trans = lk.getTranslation()
            l_rot   = lk.getRotation()
            p_trans =  p.getTranslation()
            p_rot   =  p.getRotation()

            p_inv_rot = numpy.transpose(p_rot)
            p_inv_trans = - numpy.dot(p_inv_rot, p_trans)
            rot   = p_inv_rot * l_rot
            trans = numpy.dot(p_inv_rot, l_trans) + p_inv_trans
            # print (rot)

            jtype = 'revolute'
            fixed = lk.isFixedJoint()
            if fixed:
                jtype = 'fixed'
            if lk.isRevoluteJoint():
                joint_position_list.append("%s%s"%(lk.getName(), joint_suffix))
            print('  <joint name="%s%s" type="%s">'%(lk.getName(), joint_suffix, jtype))
            print('    <parent link="%s"/>'%(p.getName()))
            print('    <child link="%s"/>'%(lk.getName()))
            print('    <origin xyz="%f %f %f" rpy="0 0 0" />'%(trans[0], trans[1], trans[2])) ##
            if not fixed:
                print('    <axis xyz="%f %f %f"/>'%(axis[0], axis[1], axis[2])) ##
                q_lower = lk.q_lower
                q_upper = lk.q_upper
                if q_lower < -10000:
                    q_lower = -10000
                if q_upper > 10000:
                    q_upper = 10000
                print('    <limit lower="%f" upper="%f" velocity="5" effort="500"/>'%(q_lower, q_upper))
            ##print('    <dynamics damping="0.2" friction="0"/>')
            print('  </joint>')

    print('  <!-- Transmission -->')
    for joint_position in joint_position_list:
        print('  <xacro:joint_position_trans_v0 name="{}"/>'.format(joint_position))

    print('</robot>')
