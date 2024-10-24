# -*- coding:utf-8 -*-

import gmpy2
import libnum

p = 161729790046446437217195813202527052012461361071046958193901644212843375071651266512082272718567071498225233829792251772275445073251621757317867395475805295760132489668315379019412661996544219147404503987277269402230456845899602988640733488828987928440149385091707872288537873588359380211273358393642469366651
q = 139507779262260081800577846019469467328409189710368457013745017476657313042307744912237762684599053303430088502425088926567727609749864233317376936732404712304677012756176206100097437463396083026091641294491551918871517998980469302884120831247301055408791948715476173540454159104397205692795284856096583915043
r = 159918855804627998305826868565976367322836999832171411074353995708669835387356541606413264041879412981193185531206455126864341259685489640396728527444633798510619982994325213762227680841954459247631071471827229492218958510492542603285822587245402522422702250367134901403894684530559748215293804985482120452643
dp = 2970416408448580369645508751910602807227688777055500819643790252331901555979076016400778936117732099156726332540087470816656767229123200454022603772241384530868142372727241021375223756239025132074514281561076131443757064458594191044754554876912650805134876311200372891741713675517013132559776834139321372069367419257776299868168928255441176279366870231500768039960146734470356114376275167863920275124721869904238947133559521150776238803511871778366346720420921611322931324433127347195586926342990232594408819819814208823725985806627108320399292854712571448343928764920669346539611008930087205673521768862095565205629
dq = 10040334175371102728861582752912647437753947253345406324049019560222188432835109432401748928776291317478848198242677120450935695493247304000111025747091448011355441330260087283441808479772671380011847105972077054411910031230688683456866851623009843824839949899585821627463232541789135330114133642597272232499550022911426845258992482645377344846153636988081391950413998655742451668454020784175041081262023300650422312789349777570694938394705852673692329341217287695798118279523883649416482952464974968694746697001538062647781408069775247383839305313863718187178864404487853997488464976863238148199856616563448047426577
dr = 19366840088682517059167963117961353225161975442684496735850343848444992247370786244168299962213224242379124307756380289602141953172002554067598714754404384061916626751382270262639891574946517396060404856278619292882812399824988260892776446866579875445209130291751028819723632731560198731673100265759707856007745346813284116192168350346769571659109211558618124008518238725853663928981728907442628507289239998499801012994963833079371276716753705094044436384920937567788820951591559487991560525370587247592344876939763042695792089996232319542834136792190704775398966178835292378781215825128777794062111397805725953911877
c = 2698019900397588328417958299317536690346885493838757927687779635484139673379477801294449842879547276216181546340578970727045566792159935150642230743109451099295088972522948845651539854030812238696728329453666116439538741021110479002791654716134616809551597206014415617017990937021939222485571260512690883688058706554998419917454428156570780474202359030475268519421332919773753833557505063610943033854100439026814341325300983754454415458764251746336412074905865091204754278733703457173216027763684834252791241538877722657431416065445657423658410263394128199658210543802017579760704970254921751766972728433275475828981408067330185932613920547091152857787920854982419120730593550616421477440467906878636929603743974999901343211159504479445581546020894911946153387072611940241989079195348707757557471454219874136524564988068217097390272308741281849437813926497839189577333913748760712321618040191614735137961241003840572130214942
#flag= flag{9eb5285c-b58c-4c07-8a1d-48b45b540fd1}

n = 3               # 同余方程个数
a = [dp, dq, dr]    # 余数
m = [(q-1)*(r-1), (p-1)*(r-1), (p-1)*(q-1)] # 模数

"""扩展欧几里得"""
def exgcd(a, b):
    if 0 == b:
        return 1, 0, a
    x, y, q = exgcd(b, a % b)
    x, y = y, (x - a // b * y)
    return x, y, q
 

"""扩展中国剩余定理"""
def CRT():
    if n == 1 :
        if m[0] > a[0]:
            return a[0]
        else:
            return -1
     
    for i in range(n):
        if m[i] <= a[i]:
            return -1

        x, y, d = exgcd(m[0], m[i])
        if (a[i] - a[0]) % d != 0:
            return -1;    
            
        t = m[i] // d
        x = (a[i] - a[0]) // d * x % t
        a[0] = x * m[0] + a[0]
        m[0] = m[0] * m[i] // d
        a[0] = (a[0] % m[0] + m[0]) % m[0]
 
    return a[0]

d = CRT()
m = gmpy2.powmod(c, d, p*q*r)
print(m)
print(libnum.n2s(int(m)))
