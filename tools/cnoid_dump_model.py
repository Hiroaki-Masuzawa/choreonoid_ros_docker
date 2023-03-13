import cnoid.Body
import cnoid.Util
import numpy

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

fname = 'catkin_ws/src/choreonoid_ros_control_assembler_sample/model/one_joint_robot.body'
rbody = cnoid.Body.BodyLoader().load(str(fname))
rbody.updateLinkTree()
rbody.initializePosition()
rbody.calcForwardKinematics()
num_link = rbody.getNumLinks()
num_joint = rbody.getNumJoints()

# for idx in range(num_link):
#     lk = rbody.getLink(idx)

#     mass_pos = lk.getCenterOfMass()

#     print('<!-- link: %s -->'%(lk.getName()))
#     print('  <link name="%s">'%(lk.getName()))
#     print_geom(filename='', visual = True)
#     print_geom(filename='', visual = False)
#     print_inertial(mass = lk.getMass(), xyz = '%f %f %f'%(mass_pos[0], mass_pos[1], mass_pos[2]))
#     print('  </link>')
#     ### dump link

for idx in range(num_link):
    lk = rbody.getLink(idx)
    if lk.isRoot():
        continue
    p = lk.getParent()

    if p:
        print(lk.getJointType())
        axis  = lk.getJointAxis()
        l_trans = lk.getTranslation()
        l_rot   = lk.getRotation()
        p_trans =  p.getTranslation()
        p_rot   =  p.getRotation()

        p_inv_rot = numpy.transpose(p_rot)
        p_inv_trans = - numpy.dot(p_inv_rot, p_trans)

        rot   = p_inv_rot * l_rot
        trans = numpy.dot(p_inv_rot, l_trans) + p_inv_trans
        print (rot)

        jtype = 'revolute'
        fixed = lk.isFixedJoint()
        if fixed:
            jtype = 'fixed'
        print('  <joint name="%s_jt" type="%s">'%(lk.getName(), jtype))
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