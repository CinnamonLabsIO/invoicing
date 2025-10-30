// Copyright (c) 2025, BWH and contributors
// For license information, please see license.txt

frappe.query_reports["Revenue Dashboard"] = {
	filters: [
		{
			"fieldname": "customer",
			"label": __("Customer"),
			"fieldtype": "Link",
			"options": "Customer",
		},
	],
};
