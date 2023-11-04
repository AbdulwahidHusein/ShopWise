from drf_yasg import openapi

api_info = openapi.Info(
    title="Shop Wise API",
    default_version='v1',
    description="An API for Shopwise Platform",
    terms_of_service="https://www.example.com/terms/",
    contact=openapi.Contact(email="contact@example.com"),
    license=openapi.License(name="BSD License"),

)
