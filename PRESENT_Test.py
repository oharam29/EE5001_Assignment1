from PRESENT import *

def Test_AddRoundKey():
    init_state = 448378203247
    init_round = 3472328296227680304
    fin_state = 75243893245493544500122956672380566504886612924084728658502794401327901192377682972514062140468801492014347853065572607017563558115261553415888647917690597969856555232467142605320086390450827989945395593109740212600923637653172436147682524304963211527838808099804740137131013347136942979768399157047415666297411996214628721040252223630396218026340354657505020418668080765689670813761088389778218905343600478849076141651883292819942330590737649631296115881289151034652216949361473050951806701759098903237628730863980128653040111103669243244889691085493411968671854296679627023871165966510365942195857811046404197779324844189745736991417251525189568006

    addRoundKey(init_state, init_round)
    assert(init_state == fin_state)
    print("Test - AddRoundKey pass")
