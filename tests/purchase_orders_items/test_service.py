from purchase_orders_items.services import PurchaseOrdersItemsService
import pytest



def test_check_maximun_po_quantity(seed_db):
	with pytest.raises(QuantityException) as ex:
		PurchaseOrderService()._check_item_quantity(seed_db['purchase_order'].id,49)
	assert ex.value.code == 400
	assert ex.value.description =='Você somente pode adicionar mais 20 itens'




