
BASE_URL = "/domain_name/product"

PRODUCT_API_URLS = {
    "LIST_PRODUCTS": f"{BASE_URL}/list", # display 10 product/page
    "ADD_PRODUCT": f"{BASE_URL}/add", 
    "PRODUCT_INFO": f"{BASE_URL}/{{pid}}/info",     # needs slug to access specific produuct
    "UPDATE_PRODUCT": f"{BASE_URL}/{{pid}}/update",  # needs slug here also
}