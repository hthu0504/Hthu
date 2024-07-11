def getinfo_LopH(self):
	print(f"lop {self.tenlop} khoa {self.khoa}")
	print(f"Lop gom {self.HS_cnt} hoc sinh")
	print(f"Giao vien:")
	for gv in self.gv_list:
		print(f"{gv.name} day mon {gv.sub}")

def getinfo_GV(self):
	print(f"{self.name} day mon {self.sub} sinh nam {self.birth}")
	for lop in self.lop_list:
			print(f"{lop.tenlop}")

def getinfo_HS(self):
	print(f"Hoc sinh {self.name} hoc lop {self.lop.tenlop} sinh nam {self.birth}")