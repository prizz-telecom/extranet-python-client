# prizz_extranet.DefaultApi

All URIs are relative to *https://my.tests.prizz-telecom.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_service_contract_comment**](DefaultApi.md#add_service_contract_comment) | **POST** /external-api/v2/service_contracts/{id}/comments | Service Contract add comment
[**create_commercial_offer**](DefaultApi.md#create_commercial_offer) | **POST** /external-api/v2/commercial_offers | Commercial Offers
[**create_commercial_offer_section**](DefaultApi.md#create_commercial_offer_section) | **POST** /external-api/v2/commercial_offers/{id}/sections | Commercial Offer Sections
[**create_eligibility**](DefaultApi.md#create_eligibility) | **POST** /external-api/v2/eligibility | Create Eligibility
[**create_ticket_operator**](DefaultApi.md#create_ticket_operator) | **POST** /external-api/v2/exploitation/operator/{id} | Exploitation Operator Tickets
[**create_workflow**](DefaultApi.md#create_workflow) | **POST** /external-api/v2/workflow | Workflows
[**eligibility_history**](DefaultApi.md#eligibility_history) | **GET** /external-api/v2/eligibility/history | Eligibility History
[**fast_order**](DefaultApi.md#fast_order) | **POST** /external-api/v2/commercial_offers/fast_order/{elig_ctx_id} | Fast order with eligiblity result
[**get_api_tokens**](DefaultApi.md#get_api_tokens) | **GET** /external-api/v2/users/api_tokens | User Api Tokens
[**get_attachment**](DefaultApi.md#get_attachment) | **GET** /external-api/v2/attachments/{id} | Attachment
[**get_client_legal_entities**](DefaultApi.md#get_client_legal_entities) | **GET** /external-api/v2/client_legal_entities | Client legal entities
[**get_client_legal_entity**](DefaultApi.md#get_client_legal_entity) | **GET** /external-api/v2/client_legal_entities/{id} | Client legal entity
[**get_comment_thread**](DefaultApi.md#get_comment_thread) | **GET** /external-api/v2/comments/threads/{id} | Comment thread
[**get_comment_threads**](DefaultApi.md#get_comment_threads) | **GET** /external-api/v2/comments/threads | Comment threads
[**get_commercial_offer**](DefaultApi.md#get_commercial_offer) | **GET** /external-api/v2/commercial_offers/{id} | Commercial Offer
[**get_commercial_offer_by_name**](DefaultApi.md#get_commercial_offer_by_name) | **GET** /external-api/v2/commercial_offers_by_name/{offer_name} | Commercial Offer by reference CPTXXXXXX, CPIXXXXXX
[**get_commercial_offer_item**](DefaultApi.md#get_commercial_offer_item) | **GET** /external-api/v2/commercial_offer_items/{id} | Commercial Offer Item
[**get_commercial_offer_pdf**](DefaultApi.md#get_commercial_offer_pdf) | **GET** /external-api/v2/commercial_offers/{id}/pdf | Commercial Offer PDF
[**get_commercial_offer_section**](DefaultApi.md#get_commercial_offer_section) | **GET** /external-api/v2/commercial_offer_sections/{id} | Commercial Offer Section
[**get_commercial_offers**](DefaultApi.md#get_commercial_offers) | **GET** /external-api/v2/commercial_offers | Commercial Offers
[**get_current_user**](DefaultApi.md#get_current_user) | **GET** /external-api/v2/user | User
[**get_eligibility**](DefaultApi.md#get_eligibility) | **GET** /external-api/v2/eligibility/{id} | Get Eligibility
[**get_entity_attachments**](DefaultApi.md#get_entity_attachments) | **GET** /external-api/v2/attachments | Attachements entity
[**get_invoice**](DefaultApi.md#get_invoice) | **GET** /external-api/v2/invoices/{id} | Invoice
[**get_invoice_detail**](DefaultApi.md#get_invoice_detail) | **GET** /external-api/v2/invoice_details/{id} | Invoice Detail
[**get_invoice_pdf**](DefaultApi.md#get_invoice_pdf) | **GET** /external-api/v2/invoices/{id}/pdf | Invoice Pdf
[**get_invoices**](DefaultApi.md#get_invoices) | **GET** /external-api/v2/invoices | Invoices
[**get_legal_entities**](DefaultApi.md#get_legal_entities) | **GET** /external-api/v2/legal_entities | Legal entities
[**get_legal_entity**](DefaultApi.md#get_legal_entity) | **GET** /external-api/v2/legal_entities/{id} | Legal entity
[**get_offer_context**](DefaultApi.md#get_offer_context) | **GET** /external-api/v2/offers/{id}/context | Offers Context
[**get_offer_contexts**](DefaultApi.md#get_offer_contexts) | **GET** /external-api/v2/offers/{id}/contexts | Offers Contexts
[**get_offer_contexts_shortened**](DefaultApi.md#get_offer_contexts_shortened) | **GET** /external-api/v2/offers/{id}/contexts/shortened | Offers Contexts
[**get_offers**](DefaultApi.md#get_offers) | **GET** /external-api/v2/offers | Offers
[**get_operator_tickets**](DefaultApi.md#get_operator_tickets) | **GET** /external-api/v2/exploitation/operator/{id}/tickets | Exploitation Operator Tickets
[**get_price_list**](DefaultApi.md#get_price_list) | **GET** /external-api/v2/price_lists/{id} | Price List
[**get_price_list_items**](DefaultApi.md#get_price_list_items) | **GET** /external-api/v2/price_lists_items | Price List Items
[**get_price_list_offers**](DefaultApi.md#get_price_list_offers) | **GET** /external-api/v2/price_lists/{id}/offers | Price List Offers
[**get_price_lists**](DefaultApi.md#get_price_lists) | **GET** /external-api/v2/price_lists | Price Lists
[**get_process**](DefaultApi.md#get_process) | **GET** /external-api/v2/exploitation/operator/{id}/process/{processId} | Exploitation Process
[**get_public_attachments**](DefaultApi.md#get_public_attachments) | **GET** /external-api/v2/attachments/public | Attachments Public
[**get_running_workflows**](DefaultApi.md#get_running_workflows) | **GET** /external-api/v2/workflows/running | Workflows running
[**get_service**](DefaultApi.md#get_service) | **GET** /external-api/v2/services/{id} | Service
[**get_service_contract**](DefaultApi.md#get_service_contract) | **GET** /external-api/v2/service_contracts/{id} | Service Contract
[**get_service_contract_by_name**](DefaultApi.md#get_service_contract_by_name) | **GET** /external-api/v2/service_contracts_by_name/{service_name} | Service Contract by name
[**get_service_contract_operational_status_by_name**](DefaultApi.md#get_service_contract_operational_status_by_name) | **GET** /external-api/v2/service_contracts_by_name/{service_name}/operational_status | Get service contract operational status
[**get_service_contracts**](DefaultApi.md#get_service_contracts) | **GET** /external-api/v2/service_contracts | Service Contracts
[**get_services**](DefaultApi.md#get_services) | **GET** /external-api/v2/services | Services
[**get_ticket**](DefaultApi.md#get_ticket) | **GET** /external-api/v2/exploitation/operator/{id}/tickets/{ref} | Exploitation Ticket
[**get_tickets**](DefaultApi.md#get_tickets) | **GET** /external-api/v2/exploitation/tickets | Exploitation Tickets
[**get_workflow**](DefaultApi.md#get_workflow) | **GET** /external-api/v2/workflow/{id} | Workflow
[**open_ticket**](DefaultApi.md#open_ticket) | **POST** /external-api/v2/exploitation/operator/{id}/tickets | Exploitation Tickets
[**remove_commercial_offer_section**](DefaultApi.md#remove_commercial_offer_section) | **DELETE** /external-api/v2/commercial_offers/{id}/sections/{sectionId} | Remove Commercial Offer Section
[**rename_commercial_offer_section**](DefaultApi.md#rename_commercial_offer_section) | **POST** /external-api/v2/commercial_offers/{id}/sections/{sectionId}/rename | Rename Commercial Offer Section
[**run_process**](DefaultApi.md#run_process) | **POST** /external-api/v2/exploitation/operator/{id}/process/{processId} | Exploitation Process
[**run_workflow**](DefaultApi.md#run_workflow) | **POST** /external-api/v2/workflow/{id} | Workflow
[**search**](DefaultApi.md#search) | **GET** /external-api/v2/search | Search
[**set_commercial_offer_section_offer**](DefaultApi.md#set_commercial_offer_section_offer) | **POST** /external-api/v2/commercial_offers/{id}/sections/{sectionId}/offer | Set Commercial Offer Section Offer
[**set_service_contract_vlan**](DefaultApi.md#set_service_contract_vlan) | **POST** /external-api/v2/service_contracts/{id}/vlan | Service Contract set vlan
[**sign_commercial_offer**](DefaultApi.md#sign_commercial_offer) | **POST** /external-api/v2/commercial_offers/{id}/sign | Sign Commercial Offer
[**submit_commercial_offer**](DefaultApi.md#submit_commercial_offer) | **POST** /external-api/v2/commercial_offers/{id}/submit | Submit Commercial Offer
[**update_commercial_offer_section_items**](DefaultApi.md#update_commercial_offer_section_items) | **POST** /external-api/v2/commercial_offers/{id}/sections/{sectionId}/update_items | Update Commercial Offer Section Items


# **add_service_contract_comment**
> CreateCommercialOffer201Response add_service_contract_comment(id, add_service_contract_comment=add_service_contract_comment)

Service Contract add comment

Add service contract comment

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.add_service_contract_comment import AddServiceContractComment
from prizz_extranet.models.create_commercial_offer201_response import CreateCommercialOffer201Response
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    id = 56 # int | service contract identifier
    add_service_contract_comment = prizz_extranet.AddServiceContractComment() # AddServiceContractComment |  (optional)

    try:
        # Service Contract add comment
        api_response = api_instance.add_service_contract_comment(id, add_service_contract_comment=add_service_contract_comment)
        print("The response of DefaultApi->add_service_contract_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_service_contract_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| service contract identifier | 
 **add_service_contract_comment** | [**AddServiceContractComment**](AddServiceContractComment.md)|  | [optional] 

### Return type

[**CreateCommercialOffer201Response**](CreateCommercialOffer201Response.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | comment added |  -  |
**400** | bad request |  -  |
**401** | need authentication |  -  |
**403** | forbidden |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_commercial_offer**
> CreateCommercialOffer201Response create_commercial_offer(create_commercial_offer)

Commercial Offers

Créer un devis

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.create_commercial_offer import CreateCommercialOffer
from prizz_extranet.models.create_commercial_offer201_response import CreateCommercialOffer201Response
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    create_commercial_offer = prizz_extranet.CreateCommercialOffer() # CreateCommercialOffer | 

    try:
        # Commercial Offers
        api_response = api_instance.create_commercial_offer(create_commercial_offer)
        print("The response of DefaultApi->create_commercial_offer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_commercial_offer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_commercial_offer** | [**CreateCommercialOffer**](CreateCommercialOffer.md)|  | 

### Return type

[**CreateCommercialOffer201Response**](CreateCommercialOffer201Response.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | devis créé |  -  |
**400** | bad request |  -  |
**401** | need authentication |  -  |
**403** | access denied |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_commercial_offer_section**
> CreateCommercialOffer201Response create_commercial_offer_section(id, create_commercial_offer_section)

Commercial Offer Sections

Ajouter une section à un devis

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.create_commercial_offer201_response import CreateCommercialOffer201Response
from prizz_extranet.models.create_commercial_offer_section import CreateCommercialOfferSection
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    id = 56 # int | identifiant du devis
    create_commercial_offer_section = prizz_extranet.CreateCommercialOfferSection() # CreateCommercialOfferSection | 

    try:
        # Commercial Offer Sections
        api_response = api_instance.create_commercial_offer_section(id, create_commercial_offer_section)
        print("The response of DefaultApi->create_commercial_offer_section:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_commercial_offer_section: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| identifiant du devis | 
 **create_commercial_offer_section** | [**CreateCommercialOfferSection**](CreateCommercialOfferSection.md)|  | 

### Return type

[**CreateCommercialOffer201Response**](CreateCommercialOffer201Response.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | section créée |  -  |
**400** | bad request |  -  |
**401** | need authentication |  -  |
**403** | access denied |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_eligibility**
> CreateEligibility create_eligibility(client_id, address=address, lat=lat, lon=lon)

Create Eligibility

Eligibility request for your user. One eligibility is made for each company allowed to your user

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.create_eligibility import CreateEligibility
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    client_id = 56 # int | client to test
    address = 'address_example' # str | address to test (optional)
    lat = 3.4 # float | latitude for tests by lon,lat (optional)
    lon = 3.4 # float | longitude for tests by lon,lat (optional)

    try:
        # Create Eligibility
        api_response = api_instance.create_eligibility(client_id, address=address, lat=lat, lon=lon)
        print("The response of DefaultApi->create_eligibility:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_eligibility: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| client to test | 
 **address** | **str**| address to test | [optional] 
 **lat** | **float**| latitude for tests by lon,lat | [optional] 
 **lon** | **float**| longitude for tests by lon,lat | [optional] 

### Return type

[**CreateEligibility**](CreateEligibility.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | eligibility created |  -  |
**400** | bad request |  -  |
**401** | need authentication |  -  |
**403** | forbidden |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ticket_operator**
> CreateOperator create_ticket_operator(id)

Exploitation Operator Tickets

Créer un opérateur

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.create_operator import CreateOperator
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    id = 56 # int | identifiant de l'opérateur

    try:
        # Exploitation Operator Tickets
        api_response = api_instance.create_ticket_operator(id)
        print("The response of DefaultApi->create_ticket_operator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_ticket_operator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| identifiant de l&#39;opérateur | 

### Return type

[**CreateOperator**](CreateOperator.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | opérateur créé |  -  |
**401** | need authentication |  -  |
**403** | forbidden |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_workflow**
> GetWorkflow create_workflow(create_workflow)

Workflows

Create workflow

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.create_workflow import CreateWorkflow
from prizz_extranet.models.get_workflow import GetWorkflow
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    create_workflow = prizz_extranet.CreateWorkflow() # CreateWorkflow | 

    try:
        # Workflows
        api_response = api_instance.create_workflow(create_workflow)
        print("The response of DefaultApi->create_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_workflow** | [**CreateWorkflow**](CreateWorkflow.md)|  | 

### Return type

[**GetWorkflow**](GetWorkflow.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | workflow created |  -  |
**400** | bad request |  -  |
**401** | need authentication |  -  |
**403** | forbidden |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **eligibility_history**
> EligibilityHistory200Response eligibility_history(page=page, items_per_page=items_per_page)

Eligibility History

View last executed eligibilities

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.eligibility_history200_response import EligibilityHistory200Response
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    page = 56 # int |  (optional)
    items_per_page = 56 # int |  (optional)

    try:
        # Eligibility History
        api_response = api_instance.eligibility_history(page=page, items_per_page=items_per_page)
        print("The response of DefaultApi->eligibility_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->eligibility_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **items_per_page** | **int**|  | [optional] 

### Return type

[**EligibilityHistory200Response**](EligibilityHistory200Response.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | eligibilities |  -  |
**401** | need authentication |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fast_order**
> CreateCommercialOffer201Response fast_order(elig_ctx_id, fast_order)

Fast order with eligiblity result

Créer un devis à partir d'un résultat d'éligibilité

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.create_commercial_offer201_response import CreateCommercialOffer201Response
from prizz_extranet.models.fast_order import FastOrder
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    elig_ctx_id = 56 # int | identifiant du contexte d'éligibilité
    fast_order = prizz_extranet.FastOrder() # FastOrder | 

    try:
        # Fast order with eligiblity result
        api_response = api_instance.fast_order(elig_ctx_id, fast_order)
        print("The response of DefaultApi->fast_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->fast_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **elig_ctx_id** | **int**| identifiant du contexte d&#39;éligibilité | 
 **fast_order** | [**FastOrder**](FastOrder.md)|  | 

### Return type

[**CreateCommercialOffer201Response**](CreateCommercialOffer201Response.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | section créée |  -  |
**400** | bad request |  -  |
**401** | need authentication |  -  |
**403** | access denied |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_tokens**
> GetApiTokens200Response get_api_tokens(page=page, items_per_page=items_per_page)

User Api Tokens

Récupérer les clés d'api pour un utilisateur

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.get_api_tokens200_response import GetApiTokens200Response
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    page = 56 # int |  (optional)
    items_per_page = 56 # int |  (optional)

    try:
        # User Api Tokens
        api_response = api_instance.get_api_tokens(page=page, items_per_page=items_per_page)
        print("The response of DefaultApi->get_api_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_api_tokens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **items_per_page** | **int**|  | [optional] 

### Return type

[**GetApiTokens200Response**](GetApiTokens200Response.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | liste des clés d&#39;api de l&#39;utilisateur |  -  |
**401** | need authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachment**
> Attachment get_attachment(id)

Attachment

Get attachment

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.attachment import Attachment
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    id = 56 # int | attachment id

    try:
        # Attachment
        api_response = api_instance.get_attachment(id)
        print("The response of DefaultApi->get_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| attachment id | 

### Return type

[**Attachment**](Attachment.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | attachment |  -  |
**401** | need authentication |  -  |
**403** | forbidden |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_legal_entities**
> GetClientLegalEntities200Response get_client_legal_entities(page=page, items_per_page=items_per_page, sort_id=sort_id, legal_entity_id=legal_entity_id)

Client legal entities

company list owned

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.get_client_legal_entities200_response import GetClientLegalEntities200Response
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    page = 56 # int |  (optional)
    items_per_page = 56 # int |  (optional)
    sort_id = 'sort_id_example' # str |  (optional)
    legal_entity_id = 56 # int |  (optional)

    try:
        # Client legal entities
        api_response = api_instance.get_client_legal_entities(page=page, items_per_page=items_per_page, sort_id=sort_id, legal_entity_id=legal_entity_id)
        print("The response of DefaultApi->get_client_legal_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_client_legal_entities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **items_per_page** | **int**|  | [optional] 
 **sort_id** | **str**|  | [optional] 
 **legal_entity_id** | **int**|  | [optional] 

### Return type

[**GetClientLegalEntities200Response**](GetClientLegalEntities200Response.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | company list |  -  |
**401** | need authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_legal_entity**
> ClientLegalEntity get_client_legal_entity(id)

Client legal entity

Get customer company details

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.client_legal_entity import ClientLegalEntity
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    id = 56 # int | identifier

    try:
        # Client legal entity
        api_response = api_instance.get_client_legal_entity(id)
        print("The response of DefaultApi->get_client_legal_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_client_legal_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| identifier | 

### Return type

[**ClientLegalEntity**](ClientLegalEntity.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | customer company details |  -  |
**401** | need authentification |  -  |
**403** | forbidden |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comment_thread**
> CommentThread get_comment_thread(id)

Comment thread

Get comment thread

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.comment_thread import CommentThread
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    id = 56 # int | thread id

    try:
        # Comment thread
        api_response = api_instance.get_comment_thread(id)
        print("The response of DefaultApi->get_comment_thread:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_comment_thread: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| thread id | 

### Return type

[**CommentThread**](CommentThread.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | thread |  -  |
**400** | bad request |  -  |
**401** | need authentication |  -  |
**403** | unauthorized |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comment_threads**
> List[CommentThread] get_comment_threads(entity_class, entity_id)

Comment threads

Get comment threads

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.comment_thread import CommentThread
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    entity_class = 'entity_class_example' # str | thread linked entity class
    entity_id = 56 # int | thread linked entity id

    try:
        # Comment threads
        api_response = api_instance.get_comment_threads(entity_class, entity_id)
        print("The response of DefaultApi->get_comment_threads:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_comment_threads: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_class** | **str**| thread linked entity class | 
 **entity_id** | **int**| thread linked entity id | 

### Return type

[**List[CommentThread]**](CommentThread.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | thread |  -  |
**401** | need authentication |  -  |
**403** | forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_commercial_offer**
> CommercialOffer get_commercial_offer(id)

Commercial Offer

Récupérer le détail d'un devis

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.commercial_offer import CommercialOffer
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    id = 56 # int | identifiant du devis

    try:
        # Commercial Offer
        api_response = api_instance.get_commercial_offer(id)
        print("The response of DefaultApi->get_commercial_offer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_commercial_offer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| identifiant du devis | 

### Return type

[**CommercialOffer**](CommercialOffer.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | détail du devis |  -  |
**401** | need authentication |  -  |
**403** | forbidden |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_commercial_offer_by_name**
> CommercialOffer get_commercial_offer_by_name(offer_name)

Commercial Offer by reference CPTXXXXXX, CPIXXXXXX

Get commercial offer by reference

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.commercial_offer import CommercialOffer
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    offer_name = 'offer_name_example' # str | commercial offer name string

    try:
        # Commercial Offer by reference CPTXXXXXX, CPIXXXXXX
        api_response = api_instance.get_commercial_offer_by_name(offer_name)
        print("The response of DefaultApi->get_commercial_offer_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_commercial_offer_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_name** | **str**| commercial offer name string | 

### Return type

[**CommercialOffer**](CommercialOffer.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | détail du devis |  -  |
**401** | need authentication |  -  |
**403** | forbidden |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_commercial_offer_item**
> CommercialOfferItem get_commercial_offer_item(id)

Commercial Offer Item

Get commercial offer item

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.commercial_offer_item import CommercialOfferItem
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    id = 56 # int | commercial offer item identifier

    try:
        # Commercial Offer Item
        api_response = api_instance.get_commercial_offer_item(id)
        print("The response of DefaultApi->get_commercial_offer_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_commercial_offer_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| commercial offer item identifier | 

### Return type

[**CommercialOfferItem**](CommercialOfferItem.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | commercial offer item |  -  |
**401** | need authentication |  -  |
**403** | forbidden |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_commercial_offer_pdf**
> bytearray get_commercial_offer_pdf(id)

Commercial Offer PDF

Récupérer le PDF d'un devis

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    id = 56 # int | identifiant du devis

    try:
        # Commercial Offer PDF
        api_response = api_instance.get_commercial_offer_pdf(id)
        print("The response of DefaultApi->get_commercial_offer_pdf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_commercial_offer_pdf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| identifiant du devis | 

### Return type

**bytearray**

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | pdf du devis |  -  |
**401** | need authentication |  -  |
**403** | forbidden |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_commercial_offer_section**
> CommercialOfferSection get_commercial_offer_section(id)

Commercial Offer Section

Get commercial offer section

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.commercial_offer_section import CommercialOfferSection
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    id = 56 # int | commercial offer section identifier

    try:
        # Commercial Offer Section
        api_response = api_instance.get_commercial_offer_section(id)
        print("The response of DefaultApi->get_commercial_offer_section:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_commercial_offer_section: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| commercial offer section identifier | 

### Return type

[**CommercialOfferSection**](CommercialOfferSection.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | commercial offer section |  -  |
**401** | need authentication |  -  |
**403** | forbidden |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_commercial_offers**
> GetCommercialOffers200Response get_commercial_offers(page=page, items_per_page=items_per_page, sort_id=sort_id, sort_create_date=sort_create_date, legal_entity_id=legal_entity_id, client_legal_entity_id=client_legal_entity_id, sections_offer_id=sections_offer_id, status=status, create_date_from=create_date_from, create_date_to=create_date_to)

Commercial Offers

Récupérer une liste de devis

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.get_commercial_offers200_response import GetCommercialOffers200Response
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    page = 56 # int |  (optional)
    items_per_page = 56 # int |  (optional)
    sort_id = 'sort_id_example' # str |  (optional)
    sort_create_date = 'sort_create_date_example' # str |  (optional)
    legal_entity_id = 56 # int |  (optional)
    client_legal_entity_id = 56 # int |  (optional)
    sections_offer_id = 56 # int |  (optional)
    status = 'status_example' # str |  (optional)
    create_date_from = '2013-10-20' # date |  (optional)
    create_date_to = '2013-10-20' # date |  (optional)

    try:
        # Commercial Offers
        api_response = api_instance.get_commercial_offers(page=page, items_per_page=items_per_page, sort_id=sort_id, sort_create_date=sort_create_date, legal_entity_id=legal_entity_id, client_legal_entity_id=client_legal_entity_id, sections_offer_id=sections_offer_id, status=status, create_date_from=create_date_from, create_date_to=create_date_to)
        print("The response of DefaultApi->get_commercial_offers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_commercial_offers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **items_per_page** | **int**|  | [optional] 
 **sort_id** | **str**|  | [optional] 
 **sort_create_date** | **str**|  | [optional] 
 **legal_entity_id** | **int**|  | [optional] 
 **client_legal_entity_id** | **int**|  | [optional] 
 **sections_offer_id** | **int**|  | [optional] 
 **status** | **str**|  | [optional] 
 **create_date_from** | **date**|  | [optional] 
 **create_date_to** | **date**|  | [optional] 

### Return type

[**GetCommercialOffers200Response**](GetCommercialOffers200Response.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | liste des devis |  -  |
**401** | need authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user**
> User get_current_user()

User

Récupérer le détail de l'utilisateur connecté

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.user import User
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)

    try:
        # User
        api_response = api_instance.get_current_user()
        print("The response of DefaultApi->get_current_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_current_user: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | détail de l&#39;utilisateur connecté |  -  |
**401** | need authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_eligibility**
> GetEligibility get_eligibility(id)

Get Eligibility

Get eligibility result

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.get_eligibility import GetEligibility
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    id = 56 # int | process identifier

    try:
        # Get Eligibility
        api_response = api_instance.get_eligibility(id)
        print("The response of DefaultApi->get_eligibility:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_eligibility: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| process identifier | 

### Return type

[**GetEligibility**](GetEligibility.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Eligibility |  -  |
**401** | need authentication |  -  |
**403** | forbidden |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_attachments**
> GetPublicAttachments200Response get_entity_attachments(entity_id, entity_type)

Attachements entity

Get entity linked attachments

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.get_public_attachments200_response import GetPublicAttachments200Response
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    entity_id = 56 # int | attached entity id
    entity_type = 'entity_type_example' # str | attached entity type

    try:
        # Attachements entity
        api_response = api_instance.get_entity_attachments(entity_id, entity_type)
        print("The response of DefaultApi->get_entity_attachments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_entity_attachments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **int**| attached entity id | 
 **entity_type** | **str**| attached entity type | 

### Return type

[**GetPublicAttachments200Response**](GetPublicAttachments200Response.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | attachments list |  -  |
**400** | bad request |  -  |
**401** | need authentication |  -  |
**403** | forbidden |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice**
> Invoice get_invoice(id)

Invoice

Récupérer le détail d'une facture

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.invoice import Invoice
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    id = 56 # int | identifiant de la facture

    try:
        # Invoice
        api_response = api_instance.get_invoice(id)
        print("The response of DefaultApi->get_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| identifiant de la facture | 

### Return type

[**Invoice**](Invoice.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | détail de la facture |  -  |
**401** | need authentication |  -  |
**403** | forbidden |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_detail**
> InvoiceDetail get_invoice_detail(id)

Invoice Detail

Get invoice detail

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.invoice_detail import InvoiceDetail
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    id = 56 # int | invoice detail identifier

    try:
        # Invoice Detail
        api_response = api_instance.get_invoice_detail(id)
        print("The response of DefaultApi->get_invoice_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_invoice_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| invoice detail identifier | 

### Return type

[**InvoiceDetail**](InvoiceDetail.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ivnoice detail |  -  |
**401** | need authentication |  -  |
**403** | forbidden |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_pdf**
> bytearray get_invoice_pdf(id)

Invoice Pdf

Récupérer le pdf d'une facture

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    id = 56 # int | identifiant de la facture

    try:
        # Invoice Pdf
        api_response = api_instance.get_invoice_pdf(id)
        print("The response of DefaultApi->get_invoice_pdf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_invoice_pdf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| identifiant de la facture | 

### Return type

**bytearray**

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | pdf de la facture |  -  |
**401** | need authentication |  -  |
**403** | forbidden |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices**
> GetInvoices200Response get_invoices(page=page, items_per_page=items_per_page, sort_id=sort_id, sort_create_date=sort_create_date, client_legal_entity_id=client_legal_entity_id, legal_entity_id=legal_entity_id, month=month, year=year)

Invoices

Récupérer une liste de factures

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.get_invoices200_response import GetInvoices200Response
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    page = 56 # int |  (optional)
    items_per_page = 56 # int |  (optional)
    sort_id = 'sort_id_example' # str |  (optional)
    sort_create_date = 'sort_create_date_example' # str |  (optional)
    client_legal_entity_id = 56 # int |  (optional)
    legal_entity_id = 56 # int |  (optional)
    month = 56 # int |  (optional)
    year = 56 # int |  (optional)

    try:
        # Invoices
        api_response = api_instance.get_invoices(page=page, items_per_page=items_per_page, sort_id=sort_id, sort_create_date=sort_create_date, client_legal_entity_id=client_legal_entity_id, legal_entity_id=legal_entity_id, month=month, year=year)
        print("The response of DefaultApi->get_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_invoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **items_per_page** | **int**|  | [optional] 
 **sort_id** | **str**|  | [optional] 
 **sort_create_date** | **str**|  | [optional] 
 **client_legal_entity_id** | **int**|  | [optional] 
 **legal_entity_id** | **int**|  | [optional] 
 **month** | **int**|  | [optional] 
 **year** | **int**|  | [optional] 

### Return type

[**GetInvoices200Response**](GetInvoices200Response.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | liste des factures |  -  |
**401** | need authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_legal_entities**
> GetLegalEntities200Response get_legal_entities(page=page, items_per_page=items_per_page, sort_id=sort_id)

Legal entities

Récupérer une liste de sociétés

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.get_legal_entities200_response import GetLegalEntities200Response
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    page = 56 # int |  (optional)
    items_per_page = 56 # int |  (optional)
    sort_id = 'sort_id_example' # str |  (optional)

    try:
        # Legal entities
        api_response = api_instance.get_legal_entities(page=page, items_per_page=items_per_page, sort_id=sort_id)
        print("The response of DefaultApi->get_legal_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_legal_entities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **items_per_page** | **int**|  | [optional] 
 **sort_id** | **str**|  | [optional] 

### Return type

[**GetLegalEntities200Response**](GetLegalEntities200Response.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | liste des sociétés |  -  |
**401** | need authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_legal_entity**
> LegalEntity get_legal_entity(id)

Legal entity

Récupérer le détail d'une société

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.legal_entity import LegalEntity
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    id = 56 # int | identifiant de la société

    try:
        # Legal entity
        api_response = api_instance.get_legal_entity(id)
        print("The response of DefaultApi->get_legal_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_legal_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| identifiant de la société | 

### Return type

[**LegalEntity**](LegalEntity.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | détail de la société |  -  |
**401** | need authentication |  -  |
**403** | forbidden |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_offer_context**
> OfferContext get_offer_context(id, items, distance=distance)

Offers Context

Get an offer context

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.offer_context import OfferContext
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    id = 56 # int | 
    items = [56] # List[int] | price list items ids
    distance = 56 # int | distance for L2 basic offer (optional)

    try:
        # Offers Context
        api_response = api_instance.get_offer_context(id, items, distance=distance)
        print("The response of DefaultApi->get_offer_context:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_offer_context: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **items** | [**List[int]**](int.md)| price list items ids | 
 **distance** | **int**| distance for L2 basic offer | [optional] 

### Return type

[**OfferContext**](OfferContext.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | offer context |  -  |
**401** | need authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_offer_contexts**
> List[OfferContext] get_offer_contexts(id, price_list, groups=groups, autofill_offer=autofill_offer, items=items, distance=distance)

Offers Contexts

Get all prices combinations for an offer and a price list

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.offer_context import OfferContext
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    id = 56 # int | 
    price_list = 56 # int | 
    groups = ['groups_example'] # List[str] | group list (e.g. bandwith, commitment, ...) (optional)
    autofill_offer = True # bool | add default products for each missing required groups to get a valid offer (optional)
    items = [56] # List[int] | determined items id to avoid combination with (e.g. FAS which are determined during eligibility) (optional)
    distance = 56 # int | estimate of the extension of our network to be built (optional)

    try:
        # Offers Contexts
        api_response = api_instance.get_offer_contexts(id, price_list, groups=groups, autofill_offer=autofill_offer, items=items, distance=distance)
        print("The response of DefaultApi->get_offer_contexts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_offer_contexts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **price_list** | **int**|  | 
 **groups** | [**List[str]**](str.md)| group list (e.g. bandwith, commitment, ...) | [optional] 
 **autofill_offer** | **bool**| add default products for each missing required groups to get a valid offer | [optional] 
 **items** | [**List[int]**](int.md)| determined items id to avoid combination with (e.g. FAS which are determined during eligibility) | [optional] 
 **distance** | **int**| estimate of the extension of our network to be built | [optional] 

### Return type

[**List[OfferContext]**](OfferContext.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | offer contexts |  -  |
**401** | need authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_offer_contexts_shortened**
> List[OfferContextShortened] get_offer_contexts_shortened(id, price_list, groups=groups, autofill_offer=autofill_offer, items=items, distance=distance)

Offers Contexts

Get all prices combinations for an offer and a price list (shortened)

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.offer_context_shortened import OfferContextShortened
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    id = 56 # int | 
    price_list = 56 # int | 
    groups = ['groups_example'] # List[str] | group list (e.g. bandwith, commitment, ...) (optional)
    autofill_offer = True # bool | add default products for each missing required groups to get a valid offer (optional)
    items = [56] # List[int] | determined items id to avoid combination with (e.g. FAS which are determined during eligibility) (optional)
    distance = 56 # int | estimate of the extension of our network to be built (optional)

    try:
        # Offers Contexts
        api_response = api_instance.get_offer_contexts_shortened(id, price_list, groups=groups, autofill_offer=autofill_offer, items=items, distance=distance)
        print("The response of DefaultApi->get_offer_contexts_shortened:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_offer_contexts_shortened: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **price_list** | **int**|  | 
 **groups** | [**List[str]**](str.md)| group list (e.g. bandwith, commitment, ...) | [optional] 
 **autofill_offer** | **bool**| add default products for each missing required groups to get a valid offer | [optional] 
 **items** | [**List[int]**](int.md)| determined items id to avoid combination with (e.g. FAS which are determined during eligibility) | [optional] 
 **distance** | **int**| estimate of the extension of our network to be built | [optional] 

### Return type

[**List[OfferContextShortened]**](OfferContextShortened.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | offer contexts shortened |  -  |
**401** | need authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_offers**
> List[Offer] get_offers(ids=ids, codes=codes)

Offers

Récupérer une liste d'offres

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.offer import Offer
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    ids = [56] # List[int] | identifiant de l'offre (optional)
    codes = ['codes_example'] # List[str] | nom de l'offre (optional)

    try:
        # Offers
        api_response = api_instance.get_offers(ids=ids, codes=codes)
        print("The response of DefaultApi->get_offers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_offers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**List[int]**](int.md)| identifiant de l&#39;offre | [optional] 
 **codes** | [**List[str]**](str.md)| nom de l&#39;offre | [optional] 

### Return type

[**List[Offer]**](Offer.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | liste des offres |  -  |
**401** | need authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_operator_tickets**
> List[Ticket] get_operator_tickets(id)

Exploitation Operator Tickets

Lister les tickets pour l'opérateur

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.ticket import Ticket
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    id = 56 # int | identifiant de l'opérateur

    try:
        # Exploitation Operator Tickets
        api_response = api_instance.get_operator_tickets(id)
        print("The response of DefaultApi->get_operator_tickets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_operator_tickets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| identifiant de l&#39;opérateur | 

### Return type

[**List[Ticket]**](Ticket.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | liste des tickets |  -  |
**401** | need authentication |  -  |
**403** | forbidden |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_list**
> PriceList get_price_list(id)

Price List

Récupérer un catalogue

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.price_list import PriceList
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    id = 56 # int | identifiant du catalogue

    try:
        # Price List
        api_response = api_instance.get_price_list(id)
        print("The response of DefaultApi->get_price_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_price_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| identifiant du catalogue | 

### Return type

[**PriceList**](PriceList.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | catalogue |  -  |
**401** | need authentication |  -  |
**403** | forbidden |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_list_items**
> List[PriceListItem] get_price_list_items(ids)

Price List Items

Récupérer une liste d'éléments d'un catalogue

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.price_list_item import PriceListItem
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    ids = [56] # List[int] | identifiant de l'élément de catalogue

    try:
        # Price List Items
        api_response = api_instance.get_price_list_items(ids)
        print("The response of DefaultApi->get_price_list_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_price_list_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**List[int]**](int.md)| identifiant de l&#39;élément de catalogue | 

### Return type

[**List[PriceListItem]**](PriceListItem.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | liste des offres du catalogue |  -  |
**401** | need authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_list_offers**
> PricesListOffers get_price_list_offers(id)

Price List Offers

Récupérer la liste des offres associées à un catalogue

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.prices_list_offers import PricesListOffers
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    id = 56 # int | identifiant du catalogue

    try:
        # Price List Offers
        api_response = api_instance.get_price_list_offers(id)
        print("The response of DefaultApi->get_price_list_offers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_price_list_offers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| identifiant du catalogue | 

### Return type

[**PricesListOffers**](PricesListOffers.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | liste des offres du catalogue |  -  |
**401** | need authentication |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_lists**
> List[PriceList] get_price_lists(ids)

Price Lists

Récupérer une liste de catalogues

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.price_list import PriceList
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    ids = [56] # List[int] | identifiant de catalogue

    try:
        # Price Lists
        api_response = api_instance.get_price_lists(ids)
        print("The response of DefaultApi->get_price_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_price_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**List[int]**](int.md)| identifiant de catalogue | 

### Return type

[**List[PriceList]**](PriceList.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | liste des catalogue |  -  |
**401** | need authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_process**
> Process get_process(id, process_id)

Exploitation Process

Detail d'un worklow de ticket

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.process import Process
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    id = 56 # int | identifiant de l'opérateur
    process_id = 56 # int | identifiant du process

    try:
        # Exploitation Process
        api_response = api_instance.get_process(id, process_id)
        print("The response of DefaultApi->get_process:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_process: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| identifiant de l&#39;opérateur | 
 **process_id** | **int**| identifiant du process | 

### Return type

[**Process**](Process.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | process |  -  |
**401** | need authentication |  -  |
**403** | forbidden |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_attachments**
> GetPublicAttachments200Response get_public_attachments()

Attachments Public

Get public attachments

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.get_public_attachments200_response import GetPublicAttachments200Response
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)

    try:
        # Attachments Public
        api_response = api_instance.get_public_attachments()
        print("The response of DefaultApi->get_public_attachments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_public_attachments: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetPublicAttachments200Response**](GetPublicAttachments200Response.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | attachments list |  -  |
**401** | need authentication |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_running_workflows**
> GetRunningWorkflows200Response get_running_workflows(contexts=contexts, states=states)

Workflows running

Get running workflows

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.get_running_workflows200_response import GetRunningWorkflows200Response
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    contexts = 'contexts_example' # str | context names (optional)
    states = 'states_example' # str | states (optional)

    try:
        # Workflows running
        api_response = api_instance.get_running_workflows(contexts=contexts, states=states)
        print("The response of DefaultApi->get_running_workflows:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_running_workflows: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contexts** | **str**| context names | [optional] 
 **states** | **str**| states | [optional] 

### Return type

[**GetRunningWorkflows200Response**](GetRunningWorkflows200Response.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | running workflows |  -  |
**401** | need authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service**
> Service get_service(id)

Service

Récupérer le détail d'un service

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.service import Service
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    id = 56 # int | identifiant du service

    try:
        # Service
        api_response = api_instance.get_service(id)
        print("The response of DefaultApi->get_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| identifiant du service | 

### Return type

[**Service**](Service.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | détail du service |  -  |
**401** | need authentication |  -  |
**403** | forbidden |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_contract**
> ServiceContract get_service_contract(id)

Service Contract

Récupérer le détail d'un pack de services

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.service_contract import ServiceContract
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    id = 56 # int | identifiant du pack de services

    try:
        # Service Contract
        api_response = api_instance.get_service_contract(id)
        print("The response of DefaultApi->get_service_contract:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_service_contract: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| identifiant du pack de services | 

### Return type

[**ServiceContract**](ServiceContract.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | détail du pack de services |  -  |
**401** | need authentication |  -  |
**403** | forbidden |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_contract_by_name**
> ServiceContract get_service_contract_by_name(service_name)

Service Contract by name

Récupérer le détail d'un pack de services

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.service_contract import ServiceContract
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    service_name = 'service_name_example' # str | identifiant du pack de services

    try:
        # Service Contract by name
        api_response = api_instance.get_service_contract_by_name(service_name)
        print("The response of DefaultApi->get_service_contract_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_service_contract_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| identifiant du pack de services | 

### Return type

[**ServiceContract**](ServiceContract.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | détail du pack de services |  -  |
**401** | need authentication |  -  |
**403** | forbidden |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_contract_operational_status_by_name**
> OperationalStatus get_service_contract_operational_status_by_name(service_name)

Get service contract operational status

Le statut présenté est un état consolidé du résultat de plusieurs tests et de mesures en différents points du réseau effectué périodiquement. Les valeurs de status disponibles sont : - `ok` : votre service est produit normalement - `warning` : le service laisse penser qu'il nécessite une attention particulière (exemple: uptime faible) - `critical` : le service est interrompu - `unknown` : nous n'avons pas pu remonter l'état du service  L'attribut lastCheck vous indique quand le service a été testé pour la dernière fois 

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.operational_status import OperationalStatus
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    service_name = 'service_name_example' # str | identifiant du contrat de services

    try:
        # Get service contract operational status
        api_response = api_instance.get_service_contract_operational_status_by_name(service_name)
        print("The response of DefaultApi->get_service_contract_operational_status_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_service_contract_operational_status_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| identifiant du contrat de services | 

### Return type

[**OperationalStatus**](OperationalStatus.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | état opérationel |  -  |
**401** | need authentication |  -  |
**403** | forbidden or operationnal status not shared  Le statut opérationnel n&#39;est pas partagé pour ce contrat de service. Ouverture après un RDV technique pour échanger sur les procédures d&#39;exploitation. |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_contracts**
> GetServiceContracts200Response get_service_contracts(page=page, items_per_page=items_per_page, sort_id=sort_id, sort_status=sort_status, status=status, legal_entity_id=legal_entity_id)

Service Contracts

Récupérer une liste de packs de services

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.get_service_contracts200_response import GetServiceContracts200Response
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    page = 56 # int |  (optional)
    items_per_page = 56 # int |  (optional)
    sort_id = 'sort_id_example' # str |  (optional)
    sort_status = 'sort_status_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    legal_entity_id = 56 # int |  (optional)

    try:
        # Service Contracts
        api_response = api_instance.get_service_contracts(page=page, items_per_page=items_per_page, sort_id=sort_id, sort_status=sort_status, status=status, legal_entity_id=legal_entity_id)
        print("The response of DefaultApi->get_service_contracts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_service_contracts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **items_per_page** | **int**|  | [optional] 
 **sort_id** | **str**|  | [optional] 
 **sort_status** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **legal_entity_id** | **int**|  | [optional] 

### Return type

[**GetServiceContracts200Response**](GetServiceContracts200Response.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | liste des packs de services |  -  |
**401** | need authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_services**
> GetServices200Response get_services(page=page, items_per_page=items_per_page, sort_id=sort_id, legal_entity_id=legal_entity_id)

Services

Récupérer une liste de services

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.get_services200_response import GetServices200Response
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    page = 56 # int |  (optional)
    items_per_page = 56 # int |  (optional)
    sort_id = 'sort_id_example' # str |  (optional)
    legal_entity_id = 56 # int |  (optional)

    try:
        # Services
        api_response = api_instance.get_services(page=page, items_per_page=items_per_page, sort_id=sort_id, legal_entity_id=legal_entity_id)
        print("The response of DefaultApi->get_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_services: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **items_per_page** | **int**|  | [optional] 
 **sort_id** | **str**|  | [optional] 
 **legal_entity_id** | **int**|  | [optional] 

### Return type

[**GetServices200Response**](GetServices200Response.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | liste des services |  -  |
**401** | need authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ticket**
> OperatorTicket get_ticket(id, ref)

Exploitation Ticket

Récupérer le détail d'un ticket

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.operator_ticket import OperatorTicket
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    id = 56 # int | identifiant de l'opérateur
    ref = 'ref_example' # str | numero du ticket

    try:
        # Exploitation Ticket
        api_response = api_instance.get_ticket(id, ref)
        print("The response of DefaultApi->get_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_ticket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| identifiant de l&#39;opérateur | 
 **ref** | **str**| numero du ticket | 

### Return type

[**OperatorTicket**](OperatorTicket.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | détail du ticket |  -  |
**401** | need authentication |  -  |
**403** | forbidden |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tickets**
> List[Ticket] get_tickets(sort_date_creation=sort_date_creation, etat=etat, operator=operator, show_archived=show_archived)

Exploitation Tickets

Lister les tickets

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.ticket import Ticket
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    sort_date_creation = 'sort_date_creation_example' # str |  (optional)
    etat = 'etat_example' # str |  (optional)
    operator = 56 # int |  (optional)
    show_archived = False # bool |  (optional) (default to False)

    try:
        # Exploitation Tickets
        api_response = api_instance.get_tickets(sort_date_creation=sort_date_creation, etat=etat, operator=operator, show_archived=show_archived)
        print("The response of DefaultApi->get_tickets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_tickets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort_date_creation** | **str**|  | [optional] 
 **etat** | **str**|  | [optional] 
 **operator** | **int**|  | [optional] 
 **show_archived** | **bool**|  | [optional] [default to False]

### Return type

[**List[Ticket]**](Ticket.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | liste des tickets |  -  |
**401** | need authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow**
> Workflow get_workflow(id)

Workflow

get workflow

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.workflow import Workflow
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    id = 56 # int | workflow id

    try:
        # Workflow
        api_response = api_instance.get_workflow(id)
        print("The response of DefaultApi->get_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| workflow id | 

### Return type

[**Workflow**](Workflow.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | workflow |  -  |
**401** | need authentication |  -  |
**403** | forbidden |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_ticket**
> CreateTicket open_ticket(id, service_id=service_id)

Exploitation Tickets

Ouvrir un ticket pour l'opérateur

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.create_ticket import CreateTicket
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    id = 56 # int | identifiant de l'opérateur
    service_id = 56 # int | identifiant du service (optional)

    try:
        # Exploitation Tickets
        api_response = api_instance.open_ticket(id, service_id=service_id)
        print("The response of DefaultApi->open_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->open_ticket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| identifiant de l&#39;opérateur | 
 **service_id** | **int**| identifiant du service | [optional] 

### Return type

[**CreateTicket**](CreateTicket.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ticket créé |  -  |
**401** | need authentication |  -  |
**403** | forbidden |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_commercial_offer_section**
> remove_commercial_offer_section(id, section_id)

Remove Commercial Offer Section

Supprimer une section

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    id = 56 # int | identifiant du devis
    section_id = 56 # int | identifiant de la section

    try:
        # Remove Commercial Offer Section
        api_instance.remove_commercial_offer_section(id, section_id)
    except Exception as e:
        print("Exception when calling DefaultApi->remove_commercial_offer_section: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| identifiant du devis | 
 **section_id** | **int**| identifiant de la section | 

### Return type

void (empty response body)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | section supprimée |  -  |
**400** | bad request |  -  |
**401** | need authentification |  -  |
**403** | access denied |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_commercial_offer_section**
> CreateCommercialOffer201Response rename_commercial_offer_section(id, section_id, rename_commercial_offer_section)

Rename Commercial Offer Section

Renommer une section

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.create_commercial_offer201_response import CreateCommercialOffer201Response
from prizz_extranet.models.rename_commercial_offer_section import RenameCommercialOfferSection
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    id = 56 # int | identifiant du devis
    section_id = 56 # int | identifiant de la section
    rename_commercial_offer_section = prizz_extranet.RenameCommercialOfferSection() # RenameCommercialOfferSection | 

    try:
        # Rename Commercial Offer Section
        api_response = api_instance.rename_commercial_offer_section(id, section_id, rename_commercial_offer_section)
        print("The response of DefaultApi->rename_commercial_offer_section:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->rename_commercial_offer_section: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| identifiant du devis | 
 **section_id** | **int**| identifiant de la section | 
 **rename_commercial_offer_section** | [**RenameCommercialOfferSection**](RenameCommercialOfferSection.md)|  | 

### Return type

[**CreateCommercialOffer201Response**](CreateCommercialOffer201Response.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | section renommée |  -  |
**400** | bad request |  -  |
**401** | need authentification |  -  |
**403** | access denied |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_process**
> Process run_process(id, process_id, files=files, transition_class=transition_class)

Exploitation Process

Executer un process

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.process import Process
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    id = 56 # int | identifiant de l'opérateur
    process_id = 56 # int | identifiant du process
    files = None # List[bytearray] |  (optional)
    transition_class = 'transition_class_example' # str |  (optional)

    try:
        # Exploitation Process
        api_response = api_instance.run_process(id, process_id, files=files, transition_class=transition_class)
        print("The response of DefaultApi->run_process:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->run_process: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| identifiant de l&#39;opérateur | 
 **process_id** | **int**| identifiant du process | 
 **files** | **List[bytearray]**|  | [optional] 
 **transition_class** | **str**|  | [optional] 

### Return type

[**Process**](Process.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | process |  -  |
**401** | need authentication |  -  |
**403** | forbidden |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_workflow**
> GetWorkflow run_workflow(id, files=files)

Workflow

run workflow

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.get_workflow import GetWorkflow
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    id = 56 # int | workflow id
    files = None # List[bytearray] |  (optional)

    try:
        # Workflow
        api_response = api_instance.run_workflow(id, files=files)
        print("The response of DefaultApi->run_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->run_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| workflow id | 
 **files** | **List[bytearray]**|  | [optional] 

### Return type

[**GetWorkflow**](GetWorkflow.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | workflow |  -  |
**400** | bad request |  -  |
**401** | need authentification |  -  |
**403** | forbidden |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> List[Search200ResponseInner] search(q, legal_entity_id=legal_entity_id, client_legal_entity_id=client_legal_entity_id)

Search

Perform search

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.search200_response_inner import Search200ResponseInner
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    q = 'q_example' # str | text to search for
    legal_entity_id = 56 # int | identifier to filter results (optional)
    client_legal_entity_id = 56 # int | identifier to filter results (optional)

    try:
        # Search
        api_response = api_instance.search(q, legal_entity_id=legal_entity_id, client_legal_entity_id=client_legal_entity_id)
        print("The response of DefaultApi->search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| text to search for | 
 **legal_entity_id** | **int**| identifier to filter results | [optional] 
 **client_legal_entity_id** | **int**| identifier to filter results | [optional] 

### Return type

[**List[Search200ResponseInner]**](Search200ResponseInner.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | résultat de la recherche |  -  |
**400** | bad request |  -  |
**401** | need authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_commercial_offer_section_offer**
> CreateCommercialOffer201Response set_commercial_offer_section_offer(id, section_id, set_commercial_offer_section_offer)

Set Commercial Offer Section Offer

Appliquer une offre à une section

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.create_commercial_offer201_response import CreateCommercialOffer201Response
from prizz_extranet.models.set_commercial_offer_section_offer import SetCommercialOfferSectionOffer
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    id = 56 # int | identifiant du devis
    section_id = 56 # int | identifiant de la section
    set_commercial_offer_section_offer = prizz_extranet.SetCommercialOfferSectionOffer() # SetCommercialOfferSectionOffer | 

    try:
        # Set Commercial Offer Section Offer
        api_response = api_instance.set_commercial_offer_section_offer(id, section_id, set_commercial_offer_section_offer)
        print("The response of DefaultApi->set_commercial_offer_section_offer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->set_commercial_offer_section_offer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| identifiant du devis | 
 **section_id** | **int**| identifiant de la section | 
 **set_commercial_offer_section_offer** | [**SetCommercialOfferSectionOffer**](SetCommercialOfferSectionOffer.md)|  | 

### Return type

[**CreateCommercialOffer201Response**](CreateCommercialOffer201Response.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | offre appliquée |  -  |
**400** | bad request |  -  |
**401** | need authentication |  -  |
**403** | access denied |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_service_contract_vlan**
> CreateCommercialOffer201Response set_service_contract_vlan(id, set_service_contract_vlan_request)

Service Contract set vlan

Set service contract vlan

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.create_commercial_offer201_response import CreateCommercialOffer201Response
from prizz_extranet.models.set_service_contract_vlan_request import SetServiceContractVlanRequest
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    id = 56 # int | service contract identifier
    set_service_contract_vlan_request = prizz_extranet.SetServiceContractVlanRequest() # SetServiceContractVlanRequest | 

    try:
        # Service Contract set vlan
        api_response = api_instance.set_service_contract_vlan(id, set_service_contract_vlan_request)
        print("The response of DefaultApi->set_service_contract_vlan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->set_service_contract_vlan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| service contract identifier | 
 **set_service_contract_vlan_request** | [**SetServiceContractVlanRequest**](SetServiceContractVlanRequest.md)|  | 

### Return type

[**CreateCommercialOffer201Response**](CreateCommercialOffer201Response.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | vlan assigned |  -  |
**400** | bad request |  -  |
**401** | need authentication |  -  |
**403** | forbidden |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sign_commercial_offer**
> SignCommercialOffer200Response sign_commercial_offer(id, sign_commercial_offer=sign_commercial_offer)

Sign Commercial Offer

Signer un devis

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.sign_commercial_offer import SignCommercialOffer
from prizz_extranet.models.sign_commercial_offer200_response import SignCommercialOffer200Response
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    id = 56 # int | identifiant du devis
    sign_commercial_offer = prizz_extranet.SignCommercialOffer() # SignCommercialOffer |  (optional)

    try:
        # Sign Commercial Offer
        api_response = api_instance.sign_commercial_offer(id, sign_commercial_offer=sign_commercial_offer)
        print("The response of DefaultApi->sign_commercial_offer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->sign_commercial_offer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| identifiant du devis | 
 **sign_commercial_offer** | [**SignCommercialOffer**](SignCommercialOffer.md)|  | [optional] 

### Return type

[**SignCommercialOffer200Response**](SignCommercialOffer200Response.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | devis validé |  -  |
**400** | bad request |  -  |
**401** | need authentication |  -  |
**403** | access denied |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_commercial_offer**
> CreateCommercialOffer201Response submit_commercial_offer(id)

Submit Commercial Offer

Valider un devis

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.create_commercial_offer201_response import CreateCommercialOffer201Response
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    id = 56 # int | identifiant du devis

    try:
        # Submit Commercial Offer
        api_response = api_instance.submit_commercial_offer(id)
        print("The response of DefaultApi->submit_commercial_offer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->submit_commercial_offer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| identifiant du devis | 

### Return type

[**CreateCommercialOffer201Response**](CreateCommercialOffer201Response.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | devis validé |  -  |
**400** | bad request |  -  |
**401** | need authentication |  -  |
**403** | access denied |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_commercial_offer_section_items**
> CreateCommercialOffer201Response update_commercial_offer_section_items(id, section_id, update_commercial_offer_section_items)

Update Commercial Offer Section Items

Update items in commercial offer section

### Example

* Api Key Authentication (tokenAuth):
* Bearer Authentication (bearerAuth):

```python
import prizz_extranet
from prizz_extranet.models.create_commercial_offer201_response import CreateCommercialOffer201Response
from prizz_extranet.models.update_commercial_offer_section_items import UpdateCommercialOfferSectionItems
from prizz_extranet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.tests.prizz-telecom.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = prizz_extranet.Configuration(
    host = "https://my.tests.prizz-telecom.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = prizz_extranet.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with prizz_extranet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prizz_extranet.DefaultApi(api_client)
    id = 56 # int | identifiant du devis
    section_id = 56 # int | identifiant de la section
    update_commercial_offer_section_items = prizz_extranet.UpdateCommercialOfferSectionItems() # UpdateCommercialOfferSectionItems | 

    try:
        # Update Commercial Offer Section Items
        api_response = api_instance.update_commercial_offer_section_items(id, section_id, update_commercial_offer_section_items)
        print("The response of DefaultApi->update_commercial_offer_section_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_commercial_offer_section_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| identifiant du devis | 
 **section_id** | **int**| identifiant de la section | 
 **update_commercial_offer_section_items** | [**UpdateCommercialOfferSectionItems**](UpdateCommercialOfferSectionItems.md)|  | 

### Return type

[**CreateCommercialOffer201Response**](CreateCommercialOffer201Response.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | section updated |  -  |
**400** | bad request |  -  |
**401** | need authentification |  -  |
**403** | access denied |  -  |
**404** | resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

