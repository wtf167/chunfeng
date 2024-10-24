import gmpy2
from Crypto.Util.number import long_to_bytes


def CMA(n, e1, e2, c1, c2):
    s = gmpy2.gcdext(e1, e2)
    s1 = s[1]
    s2 = s[2]
    if s1 < 0:
        s1 = -s1
        c1 = gmpy2.invert(c1, n)
    if s2 < 0:
        s2 = -s2
        c2 = gmpy2.invert(c2, n)
    m = pow(c1, s1, n) * pow(c2, s2, n) % n
    return m


def CMA2(n, e1, e2, c1, c2):
    s, s1, s2 = gmpy2.gcdext(e1, e2)
    m = (pow(c1, s1, n) * pow(c2, s2, n)) % n
    return m


n = int('''
21058339337354287847534107544613605305015441090508924094198816691219103399526800112802416383088995253908857460266726925615826895303377801614829364034624475195859997943146305588315939130777450485196290766249612340054354622516207681542973756257677388091926549655162490873849955783768663029138647079874278240867932127196686258800146911620730706734103611833179733264096475286491988063990431085380499075005629807702406676707841324660971173253100956362528346684752959937473852630145893796056675793646430793578265418255919376323796044588559726703858429311784705245069845938316802681575653653770883615525735690306674635167111
''')
c1 = int('''
20152490165522401747723193966902181151098731763998057421967155300933719378216342043730801302534978403741086887969040721959533190058342762057359432663717825826365444996915469039056428416166173920958243044831404924113442512617599426876141184212121677500371236937127571802891321706587610393639446868836987170301813018218408886968263882123084155607494076330256934285171370758586535415136162861138898728910585138378884530819857478609791126971308624318454905992919405355751492789110009313138417265126117273710813843923143381276204802515910527468883224274829962479636527422350190210717694762908096944600267033351813929448599
''')
c2 = int('''
11298697323140988812057735324285908480504721454145796535014418738959035245600679947297874517818928181509081545027056523790022598233918011261011973196386395689371526774785582326121959186195586069851592467637819366624044133661016373360885158956955263645614345881350494012328275215821306955212788282617812686548883151066866149060363482958708364726982908798340182288702101023393839781427386537230459436512613047311585875068008210818996941460156589314135010438362447522428206884944952639826677247819066812706835773107059567082822312300721049827013660418610265189288840247186598145741724084351633508492707755206886202876227
''')
e1 = 2767
e2 = 3659
m = CMA(n, e1, e2, c1, c2)
print(long_to_bytes(m).decode())
