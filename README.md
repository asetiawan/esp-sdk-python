# esp_sdk
This is a description

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v2
- Package version: 1.0.0
- Build date: 2017-03-01T11:03:54.879-05:00
- Build package: class io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import esp_sdk 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import esp_sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = esp_sdk.ExternalaccountsApi()
id = 56 # int | External Account Id

try:
    # Show the latest completed report for an External Account
    api_instance.v2_external_accounts_id_complete_json_patch(id)
except ApiException as e:
    print("Exception when calling ExternalaccountsApi->v2_external_accounts_id_complete_json_patch: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ExternalaccountsApi* | [**v2_external_accounts_id_complete_json_patch**](docs/ExternalaccountsApi.md#v2_external_accounts_id_complete_json_patch) | **PATCH** /v2/external_accounts/{id}/complete.json | Show the latest completed report for an External Account
*ExternalaccountsApi* | [**v2_external_accounts_id_json_delete**](docs/ExternalaccountsApi.md#v2_external_accounts_id_json_delete) | **DELETE** /v2/external_accounts/{id}.json | Remove an External Account
*ExternalaccountsApi* | [**v2_external_accounts_id_json_get**](docs/ExternalaccountsApi.md#v2_external_accounts_id_json_get) | **GET** /v2/external_accounts/{id}.json | Show a single External Account
*ExternalaccountsApi* | [**v2_external_accounts_id_json_patch**](docs/ExternalaccountsApi.md#v2_external_accounts_id_json_patch) | **PATCH** /v2/external_accounts/{id}.json | Update an External Account
*ExternalaccountsApi* | [**v2_external_accounts_json_post**](docs/ExternalaccountsApi.md#v2_external_accounts_json_post) | **POST** /v2/external_accounts.json | Create an External Account
*ExternalaccountsApi* | [**v2_external_accounts_json_put**](docs/ExternalaccountsApi.md#v2_external_accounts_json_put) | **PUT** /v2/external_accounts.json | Get a list of External Accounts
*ExternalaccountsApi* | [**v2_external_accounts_subscribed_accounts_json_get**](docs/ExternalaccountsApi.md#v2_external_accounts_subscribed_accounts_json_get) | **GET** /v2/external_accounts/subscribed_accounts.json | Show a list of Subscribed Accounts
*OrganizationsApi* | [**create**](docs/OrganizationsApi.md#create) | **POST** /v2/organizations.json | Create an Organization
*OrganizationsApi* | [**destroy**](docs/OrganizationsApi.md#destroy) | **DELETE** /v2/organizations/{id}.json | Remove an Organization
*OrganizationsApi* | [**list**](docs/OrganizationsApi.md#list) | **PUT** /v2/organizations.json | Get a list of Organizations
*OrganizationsApi* | [**show**](docs/OrganizationsApi.md#show) | **GET** /v2/organizations/{id}.json | Show a single Organization
*OrganizationsApi* | [**update**](docs/OrganizationsApi.md#update) | **PATCH** /v2/organizations/{id}.json | Update an Organization


## Documentation For Models

 - [ExternalAccount](docs/ExternalAccount.md)
 - [Organization](docs/Organization.md)
 - [PaginatedCollection](docs/PaginatedCollection.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author



