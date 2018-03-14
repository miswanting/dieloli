import core.EraPrint as eprint
import core.TextLoading as textload
import script.GameTime as gametime
import core.CacheContorl as cache
import script.AttrText as attrtext
import script.AttrPrint as attrprint
import script.AttrHandle as attrhandle
import core.PyCmd as pycmd

# 游戏主页流程
def mainFramePanel():
    cmdList = []
    playerId = cache.playObject['objectId']
    playerData = attrhandle.getAttrData(playerId)
    titleText = textload.getTextData(textload.stageWordId, '64')
    eprint.plt(titleText)
    dateText = gametime.getDateText()
    eprint.p(dateText)
    eprint.p(' ')
    playerName = playerData['Name']
    pycmd.pcmd(playerName,playerName,None)
    cmdList.append(playerName)
    eprint.p(' ')
    goldText = attrtext.getGoldText(playerId)
    eprint.p(goldText)
    eprint.p('\n')
    attrprint.printHpAndMpBar(playerId)
    mainMenuText = textload.getTextData(textload.stageWordId,'68')
    eprint.sontitleprint(mainMenuText)
    return cmdList