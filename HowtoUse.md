# How to use for RobotAssembler
見出し最後の()内で記載されているファイルが，手順で得られる成果物．
1. RobotAssemblerでロボットを組み立て，bodyファイルを保存する．(choreonoid_ros_control_assembler_sample/model/one_joint_robot.body)
1. bodyファイルを基にxacroファイルを作成する．(choreonoid_ros_control_assembler_sample/model/one_joint_robot.xacro)
    1. bodyファイルはlink_1->link_2->link_3の構造のため，それをlink_1->joint_a->link_2->joint_b->link3の形に書き直す．その際にxacro内のjointタブのnameプロパティとlinkタブのnameプロパティはかぶって構わない（ようだ）．
    1. xacroファイルの先頭に以下のマクロを記載する．(もしくは，別ファイルにしてincludeする)
        
        位置制御用マクロ

            ```
            <xacro:macro name="joint_position_trans_v0" params="name">
            <transmission name="${name}_trans">
            <type>transmission_interface/SimpleTransmission</type>
            <joint name="${name}">
            <hardwareInterface>PositionJointInterface</hardwareInterface>
            </joint>
            <actuator name="${name}_motor">
            <hardwareInterface>PositionJointInterface</hardwareInterface>
            </actuator>
            </transmission>
            </xacro:macro>
            ```
        
    1. 制御を行いたいjointについて，xacroの最後に以下のように追記する．
        'LINK_0'を制御したい場合
        
            ```
            <xacro:joint_position_trans_v0 name="LINK_0"/>
            ```
    注意 : 単位系がmであることに注意する．また，読み込む対象のメッシュも単位系がmでないといけないことに注意する．  

1. 位置制御用のconfigを作成する．(choreonoid_ros_control_assembler_sample/config/coint_control.yaml)
1. プロジェクトファイルを作成する．(choreonoid_ros_control_assembler_sample//projectAssembleRobot.cnoid)
    1. 'rosrun choreonoid_ros choreonoid'とコマンドを打ちchoreonoidを立ち上げる．
    1. File -> New -> Worldと選択し Worldを作成する．
    1. Itemsで'World'を選択した状態で，File -> Load -> Bodyと選択し，作成したBodyをロードする
    1. Itemsで'World'を選択した状態で，File -> Load -> Bodyと選択し，'catkin_ws/src/choreonoid/share/model/misc'にあるfloor.bodyをロードする．
    1. Itemsで'World'を選択した状態で，File -> New -> WorldROSを選択する．
    1. Itemsで'World'を選択した状態で，File -> New -> AISTSimulatorを選択する．
    1. Itemsで'AssembleRobot'(ロードしたロボット)を選択した状態で，File -> New -> BodyROSを選択する．
    1. Itemsで'AssembleRobot'(ロードしたロボット)を選択した状態で，File -> New -> ROSControlを選択する．
    1. ROSControlを選択，Propertyをクリックし，Name spaceにロボット名を入れる．
1. launchファイルを作成する．(choreonoid_ros_control_assembler_sample/launch/choreonoid.launch, choreonoid_ros_control_assembler_sample/launch/control.launch)
1. ReadMeの手順に従い，実行する．

## わかったようでわかっていないこと
- どこの名前を統一すべきか？
    - 現状'AssembleRobot'や'LINK_0'はどことどこが紐づいているかはしっかり把握できていない．（現状コンフリクトしていないので，問題ないはず）

## Tips
- xacroを手で作成する場合にrvizへの表示方法
  ```
  $ roslaunch urdf_tutorial display.launch model:=modelfile
  ```