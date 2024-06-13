import pytest 
from purchase_orders.service import PurchaseOrderService
from purchase_orders.exception import QuantityException

@pytest.mark.nocleardb
def test_check_quantity_minimum():
	with pytest.raises(QuantityException) as ex:
		PurchaseOrderService()._check_quantity(49)
	assert ex.value.code == 400
	assert ex.value.description =='A quantidade deve ser entre 50 e 150 items'



@pytest.mark.nocleardb
def test_check_quantity_maximun():
	with pytest.raises(QuantityException) as ex:
		PurchaseOrderService()._check_quantity(151)
	assert ex.value.code == 400
	assert ex.value.description =='A quantidade deve ser entre 50 e 150 items'


