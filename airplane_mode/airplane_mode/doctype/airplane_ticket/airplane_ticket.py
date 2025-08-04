# Copyright (c) 2025, Navtech and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import random
import string


class AirplaneTicket(Document):
	def validate(self):
		unique_add_ons = []
		seen = set()

		for item in self.add_ons:
			if item.item not in seen:
				seen.add(item.item)
				unique_add_ons.append(item)

		self.add_ons = unique_add_ons
	def before_insert(self):
		pass
		# self.set_seat()
		# self.seat=f"{random.randint(1,100)}{random.choice(['A','B','C','D','E'])}"
	# self.seat = f"{random.randint(1, 100)}{random.choice(string.ascii_uppercase[:5])}"
	def before_insert(self):
		self.seat = f"{random.randint(1, 100)}{random.choice(string.ascii_uppercase[:5])}"


	def before_save(self):
		self.cost=0
		for item in self.add_ons:
			self.cost+=item.amount
			self.total_amount=self.flight_price + self.cost 

	def before_submit(self):
		if self.status!="Boarded":
			frappe.throw(" STATUS SHOULD BE BOARDED")
	
