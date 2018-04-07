import core.GameConfig as config
import core.CacheContorl as cache
import core.TextLoading as textload
import core.Dictionaries as dictionaries

# 富文本计算
def setRichTextPrint(textMessage,defaultStyle):
    styleNameList = config.getFontDataList() + textload.getTextData(textload.barListId,'barlist')
    styleIndex = 0
    styleLastIndex = None
    styleMaxIndex = None
    styleList = []
    for i in range(0,len(styleNameList)):
        styleTextHead = '<' + styleNameList[i] + '>'
        if styleTextHead in textMessage:
            styleIndex = 1
        else:
            pass
    if styleIndex == 0:
        for i in range(0,len(textMessage)):
            styleList.append(defaultStyle)
    else:
        for i in range(0,len(textMessage)):
            if textMessage[i] == '<':
                inputTextStyleSize = textMessage.find('>',i) + 1
                inputTextStyle = textMessage[i + 1:inputTextStyleSize - 1]
                styleLastIndex = i
                styleMaxIndex = inputTextStyleSize
                if inputTextStyle[0] == '/':
                    if cache.textStylePosition['position'] == 1:
                        cache.outputTextStyle = 'standard'
                        cache.textStylePosition['position'] = 0
                        cache.textStyleCache = ['standard']
                    else:
                        cache.textStylePosition['position'] = cache.textStylePosition['position'] - 1
                        cache.outputTextStyle = cache.textStyleCache[cache.textStylePosition['position']]
                else:
                    cache.textStylePosition['position'] = len(cache.textStyleCache)
                    cache.textStyleCache.append(inputTextStyle)
                    cache.outputTextStyle = cache.textStyleCache[cache.textStylePosition['position']]
            else:
                if styleLastIndex != None:
                    if i == len(textMessage):
                        cache.textStylePosition['position'] = 0
                        cache.outputTextStyle = 'standard'
                        cache.textStyleCache = ['standard']
                    if i in range(styleLastIndex,styleMaxIndex):
                        pass
                    else:
                        styleList.append(cache.outputTextStyle)
                else:
                    styleList.append(cache.outputTextStyle)
    return styleList

# 移除富文本标签
def removeRichCache(string):
    string = str(string)
    string = dictionaries.handleText(string)
    barlist = textload.getTextData(textload.barListId, 'barlist')
    styleNameList = config.getFontDataList() + barlist
    for i in range(0, len(styleNameList)):
        styleTextHead = '<' + styleNameList[i] + '>'
        styleTextTail = '</' + styleNameList[i] + '>'
        if styleTextHead in string:
            string = string.replace(styleTextHead, '')
            string = string.replace(styleTextTail, '')
        else:
            pass
    return string