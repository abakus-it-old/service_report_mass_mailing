from openerp.osv import osv

class contract_report_mass_mailing(osv.osv_memory):
    _name = "contract.report.mass.mailing"
    _description = "Service Report Mass Mailing"

    def send_service_reports_by_email(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        active_ids = context.get('active_ids', []) or []

        email_template_obj = self.pool['mail.template']
        mail_mail_obj = self.pool['mail.mail']
        template_ids = email_template_obj.search(cr, uid, [('name', '=','Service report - Send by Email')], context=context)
        
        if template_ids:
            for account_id in active_ids:
                email_template_obj.send_mail(cr, uid, template_ids[0], account_id, force_send=True)
                
        return {'type': 'ir.actions.act_window_close'}