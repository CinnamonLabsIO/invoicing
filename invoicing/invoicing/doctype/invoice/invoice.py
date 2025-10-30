# Copyright (c) 2025, BWH and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Invoice(Document):
	def before_save(self):
		self.total_amount = 0

		for item in self.items:
			item.amount = item.rate * item.qty
			self.total_amount = self.total_amount + item.amount
