class AzartClass:
	def __init__(self):
		self.test = False
	
	def main(self, many_triger):
                text_triger = input("text: ")
                if text_triger == "banck":
                        self.test =True
                        temp = int(input("how mutch loan want to get? "))
                        cl = many_triger + temp
                        return cl, self.test
		# if self.test == 0:
		# 	self.test +=1
                #         return "test = 1"
