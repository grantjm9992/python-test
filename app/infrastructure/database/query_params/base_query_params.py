from typing import Any, Dict, List

from abc import ABC, abstractmethod

class BaseQueryParams(ABC):
    ORDER_KEY = 'orderBy'
    ORDER_TYPE = 'orderType'

    def __init__(self, query_params: Dict[str, Any]):
        self.query_params = query_params
        self.map_query_params()

    @abstractmethod
    def map(self) -> Dict[str, str]:
        pass

    @abstractmethod
    def operators(self) -> Dict[str, str]:
        pass

    def map_query_params(self):
        final_params = {}
        mapped_fields = self.map()
        operators = self.operators()

        for key, value in self.query_params:
            if value is None:
                continue
            if key in mapped_fields:
                mapped_field = mapped_fields[key]
                if key in operators:
                    operator = operators[key]
                    try:
                        if mapped_field not in final_params:
                            final_params[mapped_field] = {}
                        final_params[mapped_field][operator] = value
                        if operator == '$regex':
                            final_params[mapped_field]['$options'] = "i"
                    except Exception as e:
                        pass
                else:
                    final_params[mapped_field] = value

        self.query_params = final_params

    def get_query_params(self) -> Dict[str, Any]:
        return self.query_params

    def get_order(self) -> str:
        return self.order

    def get_order_type(self) -> str:
        return self.order_type
