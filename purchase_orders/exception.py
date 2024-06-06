from werkzeug.exceptions import HTTPException

class Quantityexception(HTTPException):
	code = 400
