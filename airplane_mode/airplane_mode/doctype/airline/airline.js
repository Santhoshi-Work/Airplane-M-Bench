// Copyright (c) 2025, Navtech and contributors
// For license information, please see license.txt

// frappe.ui.form.on('Airline', {
//     refresh(frm) {
//         console.log('Airline form loaded');
//         if (frm.doc.website) {
//             console.log('website function entered');
//             frm.add_custom_button('Visit Website', () => {
//                 window.open(frm.doc.website, '_blank');
//             });
//         }
//     }
// });
// frappe.ui.form.on('Airline', {
//     refresh(frm) {
//         if (frm.doc.website) {
//             frm.set_df_property('visit_website', 'options',
//                 `<a href="{{frm.doc.website}}" target="_blank" style="font-weight: 500; color: #1d4ed8; text-decoration: underline;">
//                     Visit Website
//                 </a>`
//             );
//             frm.refresh_field('visit_website');
        
//         } else {
//             frm.set_df_property('visit_website', 'options', '');
//             frm.refresh_field('visit_website');
//         }
//     }
// });

frappe.ui.form.on('Airline', {
    refresh: function (frm) {
        // Show web link only if the website field is filled
        if (frm.doc.website) {
            frm.add_web_link(frm.doc.website, 'Visit Website');
        }
    }
});

