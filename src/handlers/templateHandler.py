from src import models, db


class TemplateHandler:

    @staticmethod
    def update_template(cert_data_1, cert_data_2, cert_data_3, cert_data_4, cert_data_5, cert_data_6, cert_data_7,
                        cert_data_8, cert_data_9, cert_data_10, cert_data_11, cert_data_12, cert_data_13, cert_data_14,
                        cert_data_15, cert_data_16, cert_data_17, cert_data_18, cert_data_19, cert_data_20,
                        cert_data_21, cert_data_22, cert_data_23, cert_data_24, cert_data_25, cert_data_26):

        select_template = models.CertificateTemplate.query.get(1)

        select_template.cert_data_1 = cert_data_1
        select_template.cert_data_2 = cert_data_2
        select_template.cert_data_3 = cert_data_3
        select_template.cert_data_4 = cert_data_4
        select_template.cert_data_5 = cert_data_5
        select_template.cert_data_6 = cert_data_6
        select_template.cert_data_7 = cert_data_7
        select_template.cert_data_8 = cert_data_8
        select_template.cert_data_9 = cert_data_9
        select_template.cert_data_10 = cert_data_10
        select_template.cert_data_11 = cert_data_11
        select_template.cert_data_12 = cert_data_12
        select_template.cert_data_13 = cert_data_13
        select_template.cert_data_14 = cert_data_14
        select_template.cert_data_15 = cert_data_15
        select_template.cert_data_16 = cert_data_16
        select_template.cert_data_17 = cert_data_17
        select_template.cert_data_18 = cert_data_18
        select_template.cert_data_19 = cert_data_19
        select_template.cert_data_20 = cert_data_20
        select_template.cert_data_21 = cert_data_21
        select_template.cert_data_22 = cert_data_22
        select_template.cert_data_23 = cert_data_23
        select_template.cert_data_24 = cert_data_24
        select_template.cert_data_25 = cert_data_25
        select_template.cert_data_26 = cert_data_26

        try:
            db.session.commit()
            print('Update model success!')
        except:
            print('Update model failed...')
