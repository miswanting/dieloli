import core.EraPrint as eprint
import script.TextLoading as textload
import core.game as game
import core.CacheContorl as cache
import script.Ans as ans
import core.PyCmd as pycmd
import random
import script.AttrCalculation as attr

playerId = '0'

def inputName_func():
    cache.playObject['objectId'] = playerId
    cache.playObject['object'][playerId] = cache.temporaryObject.copy()
    eprint.pline()
    eprint.pl(textload.loadMessageAdv('4'))
    yrn = ans.option(ans.yesorno)
    eprint.p('\n')
    if yrn == 4:
        pycmd.clr_cmd()
        inputNickName_func()
        return
    elif yrn == 5:
        pycmd.clr_cmd()
        eprint.pline()
        eprint.pl(textload.loadMessageAdv('3'))
        playerName = game.askfor_str()
        eprint.pl(playerName)
        eprint.p('\n')
        cache.temporaryObject['Name'] = playerName
        pycmd.clr_cmd()
        inputName_func()
    elif yrn == 12:
        cache.wframeMouse['wFrameRePrint'] = 1
        eprint.pnextscreen()
        import script.mainflow as mainflow
        mainflow.main_func()
    else:
        pycmd.clr_cmd()
        eprint.p('\n')
        inputName_func()
    pass

def inputNickName_func():
    cache.playObject['object'][playerId] = cache.temporaryObject.copy()
    eprint.pline()
    eprint.pl(textload.loadMessageAdv('6'))
    yrn = ans.option(ans.inputNickNameList)
    eprint.p('\n')
    if yrn == 4:
        pycmd.clr_cmd()
        inputSexConfirm_func()
    elif yrn == 5:
        pycmd.clr_cmd()
        eprint.pline()
        eprint.pl(textload.loadMessageAdv('5'))
        playerNickName = game.askfor_str()
        eprint.pl(playerNickName)
        eprint.p('\n')
        cache.temporaryObject['NickName'] = playerNickName
        pycmd.clr_cmd()
        inputNickName_func()
    elif yrn == 14:
        pycmd.clr_cmd()
        cache.temporaryObject['NickName'] = cache.temporaryObject['Name']
        inputNickName_func()
    elif yrn == 12:
        pycmd.clr_cmd()
        eprint.p('\n')
        inputName_func()
    else:
        pycmd.clr_cmd()
        eprint.p('\n')
        inputNickName_func()
    pass

def inputSexConfirm_func():
    pycmd.clr_cmd()
    sexId = cache.playObject['object'][playerId]['Sex']
    eprint.pline()
    eprint.pl(textload.loadMessageAdv('8')[sexId])
    yrn = ans.option(ans.yesorno)
    eprint.p('\n')
    if yrn == 4:
        pycmd.clr_cmd()
        acknowledgmentAttribute_func()
    elif yrn == 5:
        pycmd.clr_cmd()
        inputSexChoice_func()
    elif yrn == 12:
        pycmd.clr_cmd()
        inputNickName_func()
    else:
        pycmd.clr_cmd()
        inputSexConfirm_func()
    pass

def inputSexChoice_func():
    pycmd.clr_cmd()
    eprint.pline()
    eprint.pl(textload.loadMessageAdv('7'))
    yrn = ans.option(ans.sex)
    eprint.p('\n')
    sex = textload.loadRoleAtrText('Sex')
    sexList = ['6', '7', '8', '9', '10', '11']
    if str(yrn) in sexList:
        for i in range(0,len(sexList)):
            if str(yrn) == sexList[i]:
                sexAtr = sex[i]
                cache.temporaryObject['Sex'] = sexAtr
                cache.playObject['object'][playerId] = cache.temporaryObject.copy()
                pycmd.clr_cmd()
                inputSexConfirm_func()
    elif yrn == 13:
        rand = random.randint(0, len(sex))
        sexAtr = sex[rand]
        cache.temporaryObject['Sex'] = sexAtr
        cache.playObject['object'][playerId] = cache.temporaryObject.copy()
        pycmd.clr_cmd()
        inputSexConfirm_func()
    elif yrn == 12:
        pycmd.clr_cmd()
        eprint.p('\n')
        inputSexConfirm_func()
    else:
        pycmd.clr_cmd()
        eprint.p('\n')
        inputSexChoice_func()
    pass

def acknowledgmentAttribute_func():
    playerSex = cache.playObject['object']['0']['Sex']
    temlist = attr.getTemList()
    temId = temlist[playerSex]
    temData = attr.getAttr(temId)
    playerAge = cache.playObject['object']['0']['Age'] = temData['Age']
    title1 = textload.loadStageWordText('1')
    playerName = cache.playObject['object']['0']['Name']
    eprint.plt(title1)
    eprint.pl(playerName)
    eprint.p(textload.loadStageWordText('2'))
    eprint.p(playerSex)
    eprint.p('\n')
    eprint.p(textload.loadStageWordText('3'))
    eprint.p(playerAge)
    eprint.p('\n')
    eprint.p('\n')
    eprint.pline()
    pass