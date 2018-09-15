import numpy
class Symbol:
    def __init__(self, eventid, iyear, imonth , iday ):
        self.eventid = eventid
        self.iyear = iyear
        self.imonth = imonth
        self.iday = iday

class Event:
    def __init__(self):


class Place:
    def __init__(self, country, country_txt, region, region_txt, provstate, city ,latitude ,longtitude):
        self.country = country
        self.country_txt = country_txt
        self.region = region
        self.region_txt = region_txt
        self.provstate = provstate
        self.city = city
        self.latitude = latitude
        self.longitude = longtitude

class Attack:
    def __init__(self, attacktype1, attacktype1_txt ,success):
        self.attacktype1 = attacktype1   #攻击类型
        self.attracktype1_txt = attacktype1_txt
        self.success = success   #攻击成功率

class Arms:
    def __init__(self, weaptype1, weaptype1_txt, weapsubtype1, weapsubtype1_txt):
        self.weaptype1 = weaptype1   #武器类型
        self.weaptype1_txt = weaptype1_txt
        self.weapsubtype1 = weapsubtype1
        self.weapsubtype1_txt = weapsubtype1_txt

class Victim:
    def __init__(self, targtype1, targtype1_txt, targsubtype1, targsubtype1_txt, corp1, target1, nalty1, nalty1_txt ):
        self.targtype1 = targtype1
        self.targtype1_txt = targtype1_txt
        self.corp1 = corp1  #实体名称
        self.target1 = target1  #目标，人、设施、建筑
        self.nalty1 = nalty1  #国籍
        self.nalty1_txt = nalty1_txt


class Murderer:
    def __init__(self, gname, motive, nperps):
        self.gname = gname   #犯罪集团名称
        self.motive = motive
        self.nperps = nperps   #凶手数量


class Result:
    def __init__(self, nkill, nwound, property, propextent):
        self.nkill = nkill  #死亡总数
        self.nwound = nwound  #受伤总数
        self.property = property  #是否损失财产
        self.propextent = propextent  #财产损失程度

class Others:
    def __init__(self):


