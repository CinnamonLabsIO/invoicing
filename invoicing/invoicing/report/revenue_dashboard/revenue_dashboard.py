# Copyright (c) 2025, BWH and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters: dict | None = None):
	"""Return columns and data for the report.

	This is the main entry point for the report. It accepts the filters as a
	dictionary and should return columns and data. It is called by the framework
	every time the report is refreshed or a filter is updated.
	"""
	columns = get_columns()
	data = get_data(filters)

	return columns, data


def get_columns() -> list[dict]:
	"""Return columns for the report.

	One field definition per column, just like a DocType field definition.
	"""
	return [
		{
			"label": _("Invoice"),
			"fieldname": "invoice",
			"fieldtype": "Link",
			"options": "Invoice",
		},
		{
			"label": _("Total Amount"),
			"fieldname": "total_amount",
			"fieldtype": "Currency",
		},
	]


def get_data(filters=None) -> list[dict]:
	"""Return data for the report.

	The report data is a list of rows, with each row being a list of cell values.
	"""

	if filters is None:
		filters = {}

	filters["docstatus"] = 1  # Only submitted invoices

	data = frappe.get_list(
		"Invoice",
		fields=["name as invoice", "total_amount"], filters=filters
	)

	for row in data:
		row["total_amount"] = row["total_amount"] or 0.0

	return data
