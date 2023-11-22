from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-item', create_item, name='create_item'),
    path('get-item/', get_item_json, name='get_item_json'),
    path('create-item-ajax/', add_item_ajax, name='add_item_ajax'),
    path('add_item_amount/<int:item_id>', add_item_amount, name='add_item_amount'),
    path('add_amount_ajax', add_amount_ajax, name='add_amount_ajax'),
    path('dec_item_amount/<int:item_id>', dec_item_amount, name='dec_item_amount'),
    path('dec_amount_ajax', dec_amount_ajax, name='dec_amount_ajax'),
    path('remove_item/<int:item_id>', remove_item, name='remove_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('remove_item_ajax/', remove_item_ajax, name="remove_item_ajax"),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]