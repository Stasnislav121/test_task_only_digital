

def test_footer_main_page(main_page):
    footer = main_page.check_footer() \
        .check_start_project_button() \
        .check_social_block() \
        .check_year_text(expected_text='© 2014 - 2025') \
        .check_copyright(expected_text='creative digital production') \
        .check_privacy_link() \
        .check_text_about() \
        .check_contacts_block() \
        .check_email_link(expected_email='hello@only.digital') \
        .check_phone_link(expected_phone='+7 (495) 740 99 79') \
        .check_telegram_block(expected_telegram='@onlydigitalagency') \
        .check_documents_block() \
        .check_logo()
