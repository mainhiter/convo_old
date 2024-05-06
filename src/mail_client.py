import re

import mailslurp_client

configuration = mailslurp_client.Configuration()
configuration.api_key['x-api-key'] = 'ef7d8e5f6f95065fb6fa40ae06edce9a635b3c90017640d4ecbacfcf8e98026e'


def create_inbox():
    with mailslurp_client.ApiClient(configuration) as api_client:
        api_instance = mailslurp_client.InboxControllerApi(api_client)
        inbox = api_instance.create_inbox()
        return {
            "id": inbox.id,
            "email": inbox.email_address
        }


def get_code_from_email2(inbox_id):
    with mailslurp_client.ApiClient(configuration) as api_client:
        waitfor_controller = mailslurp_client.WaitForControllerApi(api_client)
        email = waitfor_controller.wait_for_latest_email(inbox_id=inbox_id, timeout=30000, unread_only=True)
        code = re.search('([0-9]{4})', email.body).group(0)
        return code


def get_code_from_email():
    get_code_from_email2('a12d6c1b-f20b-43c6-941b-ede09b7c1b2f')

