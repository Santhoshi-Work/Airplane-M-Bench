# Copyright (c) 2025, Navtech and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator

class AirplaneFlight(WebsiteGenerator):
	def on_submit(self):
		self.status="Completed"
		tickets=frappe.get_all("Airplane Ticket",
						 filters={
							 "flight":"self.name",
							 "status":"Boarded",
							 "docstatus":0
						 },fields=["name"])
		frappe.msgprint(f"Found {len(tickets)} ticket(s) to submit.")

		for ticket in tickets:
			
			ticket_doc=frappe.get_doc("Airplane Ticket",ticket.name)
			try:
				ticket_doc.submit()
				
			except Exception as e:
				frappe.msgprint(f"Could not submit ticket {ticket.name}: {e}")
		frappe.db.commit()