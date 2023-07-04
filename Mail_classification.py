import numpy as np
import skops.io as sio
from sklearn.svm import SVC

class MailClassification():

	def __init__(self, mail = None):
		self._model = sio.load("model/linear_all_data.skops", trusted=True)
		self._dictionary = None
		self._mail = mail
		self._vector = None

	def _filter_for_string_mail(self, mail:str):
		assert type(mail) is str , "Datatype is not str."

		string = mail.replace("\n"," ")
		for char in string:
			if not char.isalpha() and char != " ":
				string = string.replace(char, "")

		string = string.lower()
		while "  " in string:
			string = string.replace("  ", " ")

		return string

	def _encode_vector(self):
		self._vector = np.zeros((1, len(self._dictionary)))
		for word in self._mail:
			if word in self._dictionary:
				self._vector[0][self._dictionary.index(word)] += 1

	def set_dictionary(self, path = "model/dictionary.txt"):
		with open(path, "r", encoding="utf-8") as f:
			dictionary = f.read()
		self._dictionary = dictionary.split(" ")[:-1]

	def set_mail(self, mail):
		if self._dictionary is None:
			self.set_dictionary()
		if type(mail) is str:
			self._mail = self._filter_for_string_mail(mail).split(" ")[:-1]
		elif type(mail) is list:
			self._mail = mail
		else:
			raise Exception("String or List string only!")
		self._encode_vector()
		print(self._mail, self._vector,len(self._mail), sum(self._vector[0]))

	def get_vector(self):
		print(self._vector)

	def get_dictionary(self):
		print(self._dictionary, len(self._dictionary))

	def clasification_email(self):
		return "Spam" if self._model.predict(self._vector) == 1 else "Not spam"