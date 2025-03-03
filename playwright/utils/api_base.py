from playwright.sync_api import Playwright

orders_payload = {"orders":[{"country":"Ukraine","productOrderedId":"6581ca399fd99c85e8ee7f45"}]}
class APIutils:
    def getToken(self,playwright:Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/auth/login",
                                 data={userEmail: "rahulshetty@gmail.com", userPassword: "Iamking@000"})
        assert response.ok
        print(response.json())
        responseBody = response.json()
        return responseBody["token"]

    def create_order(self,playwright:Playwright):
        token= self.getToken(playwright)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/order/create-order",
                                 data= orders_payload,
                                 headers={"Authorization": token,
                                          "Content-type:": "application/json"
                                          })
        print(response.json())