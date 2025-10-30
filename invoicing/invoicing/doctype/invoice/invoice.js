// Copyright (c) 2025, BWH and contributors
// For license information, please see license.txt

frappe.ui.form.on("Invoice", {
	refresh(frm) {
		frm.add_custom_button("Create Payment Entry", () => {
			frappe.new_doc("Payment Entry", {
				invoice: frm.doc.name,
				amount: frm.doc.total_amount
			})
		})
	},
});
