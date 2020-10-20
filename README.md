[![License](https://img.shields.io/:license-apache2.0-red.svg)](https://opensource.org/licenses/Apache-2.0)

# paypay-sample-ecommerce-backend-python

This is a python based implementation of PayPay's SDK. For the demonstration purpose we have used a simple Flask server with polling library to create QR code link and to check the order status of a QR code

### Install Requirements

```sh
$ cd server/python
$ pip install -r requirements.txt
```

### Add API Keys to environment

```sh
$ export API_KEY="REPLACE_WITH_YOUR_API_KEY"
$ export API_SECRET="REPLACE_WITH_YOUR_SECRET_KEY" 
$ export MERCHANT_ID="REPLACE_WITH_YOUR_MERCHANT_ID" 
```

### Run Flask API server
```sh
$ flask run
```
You should now have the API server running on http://localhost:5000

### Cloud deployment

Additionally to trying out this application locally, you can deploy it to a variety of host services.


[![Deploy with Heroku](https://www.herokucdn.com/deploy/button.svg)](https://www.heroku.com/deploy/?template=https://github.com/paypay/paypay-sample-ecommerce-backend-python/tree/master) 