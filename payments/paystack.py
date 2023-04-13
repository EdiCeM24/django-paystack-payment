from django.conf import settings
import requests

class Paystack:
    PAYSTACK_SECRET_KEY = settings.PAYSTACK_SECRET_KEY
    base_url = 'https://api.paystay.co'
    
    # you can put down here all requirements, but we want put down verify_payment.
    def Verify_payment(self, ref,  *arg, **kwargs):
        path = f'/transactions/verify/{ref}'
        
        headers = {
            "Authorization": f"Bearer {self.PAYSTACK_SECRET_KEY}",
            "content-Type": "application/json",
        }
        url = self.base_url + path
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            response_data = response.json()
            return response_data['status'], response_data['data']
        response_data = response.json()
        return response_data['status'], response_data['message']