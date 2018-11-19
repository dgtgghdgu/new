# -*- conding:Utf-8 -*-
from sys import exit
from random import randint

class Scene(object):
    def enter(self):
        print("这个场景还没有配置，子类会重新构造它")
        exit(1)

class Engine(object):
    def __init__(self,scene_map):
        self.scene_map = scene_map

    def play(self):

        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')


        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        #be sure to print out the last scene
        current_scene.enter()


class Death(Scene):

    quips=[
            "你挂了，没你的事了",
            "你不行，输不起",
            "快回家抱孩子吧",
            "有个一忠告，你不适合在这个地方闯荡"]

    def enter(self):
        print(Death.quips[randint(0,len(self.quips)-1)])
        exit(1)


class Centralcorridor(Scene):
    def enter(self):
        print("赛伯坦星球的哥斯拉驾驶25号星舰攻入了你的飞船并摧毁了它")
        print("全体船员都牺牲了，只剩下最一个人，就是你。")
        print("你的任务就是从弹药库里取出武器，摧毁敌人的飞船。")
        print("把炸弹放在舰桥上，然后引爆它。如果你及时到达逃生舱，还可以活下来")
        print("\n")
        print("""当你从主舰上跑向武器库找弹药的时候，一个小怪兽跳了出来，他有红色的皮肤，蓝色的毛发，
            从它的眼睛里，你可以看到它的敌意，它那可恶躯体把门堵住了。它手里拿着的武器对准了你。""")
        action = input("请输入你的选择：‘攻击’或‘闪开’或‘讲笑话’")

        if action == "攻击":
            print("""
            你拔出枪来，向怪兽开火。它的小丑服装在他的身体周围流动和移动，
            你打偏了一点。你的激光击中了他的衣服，但完全错过了他。
            这“完全毁掉了他妈妈给他买的新衣服，”这让他勃然大怒，
            不断地打你的脸，直到“你死了”。然后他吃了你。
            """)
            return 'death'

        if action == "闪开":
            print(""" 
            像一个世界级的拳击手，你闪避，编织，滑动和向右滑动
            当Gothon的爆破器把激光从你的头上划过。
            你巧妙地避开你的脚滑倒的中间，你的头撞在金属墙上，
            然后昏倒了。你醒来后不久就死了，
            Gothon跺着你的头，吃掉了你。""")
            return 'death'

        if action == "讲笑话":
            print("""
            幸运的是，他们让你在学院里学会了Gothon侮辱性语言。
            你讲了一个你知道的Gothon笑话:
            Lbhe zbgure vf fb sng, jura fur fvgf nebhaq ubhfr, 
            fur fvgf nebhaq ubhfr。
            Gothon停下来，试着不笑，然后突然大笑起来，动弹不得。
            当他在笑的时候，你跑过去对着他的脑袋开枪。
            把他放下，然后跳进武器库的门。          
            """)
            return 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'

class LaserWeaponArmory(Scene):
    def enter(self):
        print("""
        你冲进武器库里，蹲下，扫视房间。
        为了更多可能隐藏的哥顿人。太安静了，太安静了。
        你站起来，跑到房间的另一边去找
        中子弹在它的容器。盒子上有一个键盘锁
        你需要代码把炸弹弄出来。如果你得到代码
        错了10次锁就永远关闭了，你不能搞砸了
        炸弹。代码是3位数字。""")
        code = "%d%d%d" % (randint(1,9),randint(1,9),randint(1,9))
        guess = input("[请输入密码]>")
        guesses = 0

        while guess !=code and guesses <10:
            print("错了，BIBIBI")
            if int(guess) > int(code):
                print("大了")
            else:
                print("小了")
            guesses += 1
            guess = input("[请输入密码]>")

        if guess == code:
            print("""
            容器喀哒一声打开，密封破裂，气体泄漏。
            你拿起中子弹，以最快的速度跑向桥，
            你必须把它放在正确的位置。""")
            return 'the_bridge'
        else:
            print("""
            锁响了最后一次，然后你听到一阵恶心的声音
            熔融的声音，因为机制是融合在一起。
            你决定坐在那里，最后哥顿人炸毁了
            离开他们的船，你就会死。          
            """)
            return 'death'

class TheBridge(Scene):
    def enter(self):
        print("""
        你带着电子毁灭炸弹冲到桥上
        在你的手臂下，给5个试图这么做的哥顿人一个惊喜
        控制这艘船。他们每个人都有一个更丑的
        比上次的小丑戏服多。他们还没有退出
        武器还在，因为他们看到了你下面的炸弹
        手臂，不想引爆它。""")
        action = input("请输入你的选择：‘扔炸弹’或‘慢慢安装’")
        if action == "扔炸弹":
            print("""
            你惊慌失措地把炸弹扔向一群哥顿人
            向门口跳过去。就在你放下它的时候
            Gothon朝你后背开枪，杀了你。
            当你死的时候，你会看到另一只蜥蜴疯狂地试图解除武装
            炸弹。你死的时候知道他们可能会爆炸
            它离开。""")
            return 'death'
        elif action == "慢慢安装":
            print("""
            你把炸弹对准手臂下的炸弹
            哥顿人举起手开始出汗。
            你向门后退一步，打开它，然后小心翼翼
            把炸弹放在地板上，用你的爆破枪对准它。
            然后你跳回门，按下关闭按钮
            把锁炸了，哥顿人就出不去了。
            既然炸弹被放置好了，你就跑到逃生舱去
            把这个罐头拿开。""")
            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE")
            return "the_bridge"

class EscapePod(Scene):
    def enter(self):
        print("""
        你拼命地闯过那条船，想闯过去整个飞船爆炸前的逃生舱。似乎
        船上几乎没有哥顿人，所以你逃不掉干扰。你带着逃生舱来到房间
        现在需要选择一个。其中一些可能会受损
        但你没有时间去看。有5个分离舱，哪一个
        你需要吗?""")
        good_pod =randint(1,5)
        guess = input("请选择几号逃生舱")

        if int(guess) != good_pod:
            print("""
            你进入了你选择的%s逃生舱，按下了弹出按钮，
            逃生舱飞入了太空，但舱体经不起折腾，你被
            压破了。""" % guess)
            return 'death'
        else:
            print("""
            你跳进%s号吊舱，按弹出按钮。
            舱体很容易滑出，进入太空下面的行星。
            当它飞向地球时，你看到飞船发生了爆炸，
            就借一颗明亮的星，同时带走了Gothon飞船
            上所有的人。你赢了!
            """ % guess)
            return 'finished'
class Finished(Scene):

    def enter(self):
        print("你赢了，你真了不起")
        return 'finished'


class Map(object):

    scenes = {
        'central_corridor':Centralcorridor(),
        'laser_weapon_armory':LaserWeaponArmory(),
        'the_bridge':TheBridge(),
        'escape_pod':EscapePod(),
        'death':Death(),
        'finished':Finished(),
        }

    def __init__(self,start_scene):
        self.start_scene = start_scene

    def next_scene(self,scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
