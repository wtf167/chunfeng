from Crypto.Util.number import *
import gmpy2
from z3 import *


N=18974131303606517108116779221394983351107953418674246808002046468756695163654887691911576186421805200250724321568280195905290442205232517227748969364090141063128939314878515317496341421052786397637775756920934374402845581351369492477771453093640094024467419280993344938852728756640716156565675517813218333062731827741326761259969868455874961692512448497903630657495966824453734032513674207164780712696722182628908402340122033085935890252243199482816629275286868697072041774808266299597266915191885557647884902011866719857934046712299602699100891310652940496655959481394816839239749563560927325844243871359449301928659
p = 157194667273395078091690715359649373226005247729684564897233925620451263163534476559233007477874770144949074471296577678270820453203784261690001421933906316488224081275610737920296334697466445787310072301759253431687655435272535953996103257268055911344285357880348486067423090573148921357811044304231614285373
q = N // p
print(q)