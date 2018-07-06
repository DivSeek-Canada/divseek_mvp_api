# swagger_client.DefaultApi

All URIs are relative to *https://petstore.swagger.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_germplasm**](DefaultApi.md#get_germplasm) | **GET** /germplasm/ | Returns all germplasm we have
[**get_germplasm_by_id**](DefaultApi.md#get_germplasm_by_id) | **GET** /germplasm/{id} | Returns all germplasm we have
[**get_germplasm_by_taxon**](DefaultApi.md#get_germplasm_by_taxon) | **GET** /germplasm/taxon/{id} | Returns all germplasm we have by taxon
[**get_locus_by_qtl**](DefaultApi.md#get_locus_by_qtl) | **GET** /locus/qtl/{id} | Returns all phenotypes for a germplasm that we have
[**get_locus_by_taxon**](DefaultApi.md#get_locus_by_taxon) | **GET** /locus/taxon/{id} | Returns all phenotypes for a germplasm that we have
[**get_qt_ls**](DefaultApi.md#get_qt_ls) | **GET** /qtl/ | Returns all the QTLs (Quantitative Trait Loci) we have
[**get_qtl_by_germplasm_trait**](DefaultApi.md#get_qtl_by_germplasm_trait) | **GET** /qtl/taxon/{taxonId}/trait/{traitId} | Returns all phenotypes for a germplasm that we have
[**get_taxonomy**](DefaultApi.md#get_taxonomy) | **GET** /taxon/ | Returns all germplasm we have
[**get_taxonomy_by_id**](DefaultApi.md#get_taxonomy_by_id) | **GET** /taxon/{id} | Returns all germplasm we have
[**get_traits**](DefaultApi.md#get_traits) | **GET** /trait/ | Returns all phenotypes we have
[**get_traits_by_germplasm**](DefaultApi.md#get_traits_by_germplasm) | **GET** /trait/germplasm/{germplasmId} | Returns all phenotypes for a germplasm that we have


# **get_germplasm**
> list[Germplasm] get_germplasm()

Returns all germplasm we have

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Returns all germplasm we have
    api_response = api_instance.get_germplasm()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_germplasm: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Germplasm]**](Germplasm.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_germplasm_by_id**
> Germplasm get_germplasm_by_id(id)

Returns all germplasm we have

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Unique database ID for the germplasm

try:
    # Returns all germplasm we have
    api_response = api_instance.get_germplasm_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_germplasm_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique database ID for the germplasm | 

### Return type

[**Germplasm**](Germplasm.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_germplasm_by_taxon**
> Germplasm get_germplasm_by_taxon(id)

Returns all germplasm we have by taxon

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Unique database ID for the taxon

try:
    # Returns all germplasm we have by taxon
    api_response = api_instance.get_germplasm_by_taxon(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_germplasm_by_taxon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique database ID for the taxon | 

### Return type

[**Germplasm**](Germplasm.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_locus_by_qtl**
> Locus get_locus_by_qtl(id)

Returns all phenotypes for a germplasm that we have

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Unique database ID for the QTL

try:
    # Returns all phenotypes for a germplasm that we have
    api_response = api_instance.get_locus_by_qtl(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_locus_by_qtl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique database ID for the QTL | 

### Return type

[**Locus**](Locus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_locus_by_taxon**
> list[Locus] get_locus_by_taxon(id)

Returns all phenotypes for a germplasm that we have

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Unique database ID for the taaon

try:
    # Returns all phenotypes for a germplasm that we have
    api_response = api_instance.get_locus_by_taxon(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_locus_by_taxon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique database ID for the taaon | 

### Return type

[**list[Locus]**](Locus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_qt_ls**
> list[QTL] get_qt_ls()

Returns all the QTLs (Quantitative Trait Loci) we have

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Returns all the QTLs (Quantitative Trait Loci) we have
    api_response = api_instance.get_qt_ls()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_qt_ls: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[QTL]**](QTL.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_qtl_by_germplasm_trait**
> list[QTL] get_qtl_by_germplasm_trait(germplasm_id, trait_id)

Returns all phenotypes for a germplasm that we have

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
germplasm_id = 'germplasm_id_example' # str | Unique database ID for the germplasm
trait_id = 'trait_id_example' # str | Unique database ID for the trait in question

try:
    # Returns all phenotypes for a germplasm that we have
    api_response = api_instance.get_qtl_by_germplasm_trait(germplasm_id, trait_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_qtl_by_germplasm_trait: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **germplasm_id** | **str**| Unique database ID for the germplasm | 
 **trait_id** | **str**| Unique database ID for the trait in question | 

### Return type

[**list[QTL]**](QTL.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_taxonomy**
> list[Taxonomy] get_taxonomy()

Returns all germplasm we have

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Returns all germplasm we have
    api_response = api_instance.get_taxonomy()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_taxonomy: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Taxonomy]**](Taxonomy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_taxonomy_by_id**
> Taxonomy get_taxonomy_by_id(id)

Returns all germplasm we have

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Unique database ID for the taxonomy

try:
    # Returns all germplasm we have
    api_response = api_instance.get_taxonomy_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_taxonomy_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique database ID for the taxonomy | 

### Return type

[**Taxonomy**](Taxonomy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_traits**
> list[Phenotype] get_traits()

Returns all phenotypes we have

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Returns all phenotypes we have
    api_response = api_instance.get_traits()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_traits: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Phenotype]**](Phenotype.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_traits_by_germplasm**
> list[Phenotype] get_traits_by_germplasm(germplasm_id)

Returns all phenotypes for a germplasm that we have

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
germplasm_id = 'germplasm_id_example' # str | Unique database ID for the germplasm

try:
    # Returns all phenotypes for a germplasm that we have
    api_response = api_instance.get_traits_by_germplasm(germplasm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_traits_by_germplasm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **germplasm_id** | **str**| Unique database ID for the germplasm | 

### Return type

[**list[Phenotype]**](Phenotype.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

