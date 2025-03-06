from playwright.sync_api import Playwright
credentials = {"userEmail":"rahulshetty@gmail.com","userPassword":"Iamking@000"}
orders_payload = {"orders":[{"country":"Ukraine","productOrderedId":"67a8df1ac0d3e6622a297ccb"}]}

class APIutils:

    def get_token(self,playwright: Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/auth/login", data = credentials)
        assert response.ok
        print(response.json())
        response_body = response.json()
        return response_body["token"]

    def create_order(self,playwright:Playwright):
        token=self.get_token(playwright)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/order/create-order",
                                            headers = {"Authorization": token, "Content-type": "application/json"},
                                            data=orders_payload
        )
        print(response.json())
