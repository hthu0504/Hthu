from Getinfo import getinfo_LopH, getinfo_GV, getinfo_HS
from Fix import fix_LopH, fix_GV, fix_HS

class LopH:
	def __init__(self, tenlop, khoa):
		self.tenlop = tenlop
		self.khoa = khoa
		self.gv_list = []
		self.HS_cnt = 0
	def getinfo (self):
		getinfo_LopH(self)	
	def fix(self, tenlop, khoa):
		fix_lopH(self, tenlop, khoa)


class GV:
	def __init__ (self, name, sub, birth):
		self.name = name
		self.sub = sub
		self.birth = birth
		self.lop_list = []
	def getinfo (self):
		getinfo_GV(self)	
	def addtocls (self, clss):
		clss.gv_list.append(self)
		self.lop_list.append(clss)	
	def remove (self, clss):
		clss.gv_list.remove(self)
		self.lop_list.remove(clss)	
	def fix(self, name, sub, birth):
		fix_GV(self, name, sub, birth)


class HS:
	def __init__(self, name, lop, birth):
		self.name = name
		self.lop = lop 
		self.birth = birth
		self.lop.HS_cnt += 1
	def getinfo (self):
		getinfo_HS(self)
	def fix(self, name, birth):
		fix_HS(self, name, birth)
	def change(self, lop):
		self.lop.HS_cnt -= 1
		self.lop = lop
		self.lop.HS_cnt += 1
	



Tin1 = LopH("Tin1", 2326)
Tin2 = LopH("Tin2", 2326)
Toan1 = LopH("Toan1", 2326)

Hai = GV("Hai", "Tinhoc", 1980)
Dung = GV("Dung", "Su", 1999)
Ngoc = GV("Ngoc", "Van", 1989)

Hai.addtocls(Tin1)
Dung.addtocls(Tin2)
Ngoc.addtocls(Toan1)

#Hai.remove(Tin1)

Bao = HS("Bao", Tin1, 2008)
Lac = HS("Lac", Tin2, 2007)
Thu = HS("Thu", Toan1, 2006)

Tin1.getinfo()
Bao.getinfo()
print('\n')
Tin2.getinfo()
Lac.getinfo()
print('\n')
Toan1.getinfo()
Thu.getinfo()
print('\n')







