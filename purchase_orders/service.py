from .model import PurchaseOrderModel
from flask import jsonify
from .exception import QuantityException

class PurchaseOrderService:
	#esta é uma funçaão privada
	def _check_quantity(self, quantity):
		if quantity < 50 or quantity > 150:
			raise QuantityException('A quantidade deve ser entre 50 e 150 items')



	def find_all(self):
		purchase_orders = PurchaseOrderModel.find_all()
		return [p.as_dict() for p in purchase_orders]
		

	def create(self,**kwargs):
		self._check_quantity(kwargs['quantity'])
		purchase_order = PurchaseOrderModel(**kwargs)
		purchase_order.save()

		return purchase_order.as_dict()


	def find_by_id(self, id):
		purchase_order = PurchaseOrderModel.find_by_id(id)
		if purchase_order:
			return purchase_order.as_dict()
		return jsonify({'message':'Pedido de id {} não encontrado'.format(id)})
