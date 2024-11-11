from typing import Any, Callable, cast, Dict, List, Optional, Tuple, Type, Union
from app.infrastructure.database.query_params.base_query_params import BaseQueryParams

class GarmentSearchQueryParams(BaseQueryParams):
    PRODUCT_TITLE = 'product_title'
    PRODUCT_CATEGORIES = 'product_categories'
    SIZE = 'size'
    MIN_PRICE = 'min_price'
    MAX_PRICE = 'max_price'
    GENDER = 'gender'
    BRAND = 'brand'

    def map(self):
        return {
            self.PRODUCT_TITLE: 'product_title',
            self.PRODUCT_CATEGORIES: 'product_categories',
            self.SIZE: 'size',
            self.MIN_PRICE: 'price',
            self.MAX_PRICE: 'price',
            self.GENDER: 'gender',
            self.BRAND: 'brand'
        }

    def operators(self):
        return {
            self.PRODUCT_CATEGORIES: '$regex',
            self.PRODUCT_TITLE: '$regex',
            self.MIN_PRICE: '$gte',
            self.MAX_PRICE: '$lte',
        }
