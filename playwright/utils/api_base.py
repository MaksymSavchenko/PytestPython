from playwright.sync_api import Playwright

orders_payload = {"orders":[{"country":"Ukraine","productOrderedId":"67a8df1ac0d3e6622a297ccb"}]}

class APIutils:

    def get_token(self, playwright: Playwright, user_credentials):
        user_email = user_credentials['userEmail']
        user_password = user_credentials['userPassword']
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/auth/login", data = {"userEmail":user_email,"userPassword":user_password})
        assert response.ok
        print(response.json())
        response_body = response.json()
        return response_body["token"]

    def create_order(self,playwright:Playwright,user_credentials):
        token=self.get_token(playwright,user_credentials)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/order/create-order",
                                            headers = {"Authorization": token, "Content-type": "application/json"},
                                            data=orders_payload
        )
        print(response.json())

        response_body = response.json()
        order_id = response_body["orders"][0]
        print("{} {}".format("Order ID is:", order_id))
        return order_id