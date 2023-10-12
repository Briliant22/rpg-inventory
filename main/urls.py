from django.urls import path
from main.views import show_main, create_item, add_item_amount, dec_item_amount, remove_item\
    ,register, login_user, logout_user, get_item_json, add_item_ajax\
    ,show_xml, show_json, show_xml_by_id, show_json_by_id

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
    path('dec_item_amount/<int:item_id>', dec_item_amount, name='dec_item_amount'),
    path('remove_item/<int:item_id>', remove_item, name='remove_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
]