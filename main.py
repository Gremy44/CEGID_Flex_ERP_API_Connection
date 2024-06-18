import json
import sys
from get_token import get_oauth_token
from xrp_flex_connection import XrpFlexConnection

def main(config_path):
    with open(config_path, 'r') as file:
        config = json.load(file)

    api_url = config.get("url")
    token_url = config.get("tokenUrl")
    username = config.get("username")
    password = config.get("password")
    scope = config.get("scope")
    client_id = config.get("client_id")
    client_secret = config.get("client_secret")

    token = get_oauth_token(username, password, scope, client_id, client_secret, token_url)
    flex = XrpFlexConnection(api_url, token)

    req1 = ("Customer?$expand=MainContact,MainContact/Address,BillingContact&$select=CustomerID,"
            "CustomerName,CustomerClass,StatementCycleID,MainContact/Email,MainContact/Phone1,"
            "MainContact/Address/AddressLine1,MainContact/Address/AddressLine2,MainContact/Address/City,"
            "MainContact/Address/State,MainContact/Address/PostalCode,MainContact/DisplayName&"
            "filter=CustomerName eq 'Hotel du Lac'")
    print(flex.execute_get_request(req1))

    # Uncomment and use these lines if needed for additional requests
    # req2 = ("Customer?$select=CustomerID,CustomerName,MainContact/Email&$expand=MainContact&"
    #         "filter=CustomerID eq 'C000000004'")
    # print(flex.execute_get_request(req2))

    # req3 = ("Customer?$select=CustomerID,MainContact/Email&$expand=MainContact&"
    #         "filter=MainContact/Email eq 'ghrum@ghrum.bis'")
    # param3 = json.dumps({"CustomerName": {"value": "Gupp info"}})
    # print(flex.execute_put_request(req3, param3))

if __name__ == "__main__":
    config_path = sys.argv[1]
    main(config_path)
