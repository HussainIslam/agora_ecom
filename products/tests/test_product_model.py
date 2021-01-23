from django.test import TestCase

from products.models import Product, P_Color, P_Size, P_Category, P_Brand

class ProductsTestClass(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        '''
        Setup testing data for Product model
        '''
        # Creating brand
        cls.brand = P_Brand.objects.create(
            brand_name="Gucci",
            brand_description="Luxary brand",
            brand_website="http://example.com/"
        )

        # Creating category
        cls.categ = P_Category.objects.create(
            category_name = "Shirt",
            category_description = "Shirts for men",
            parent_category = None
        )

        # Creating 3 sizes: large, medium, and small
        cls.size_large = P_Size.objects.create(
            category = cls.categ,
            value = "Large"
        )
        cls.size_med = P_Size.objects.create(
            category = cls.categ,
            value = "Medium"
        )
        cls.size_small = P_Size.objects.create(
            category = cls.categ,
            value = "Small"
        )

        # Creating color
        cls.color_white = P_Color.objects.create(
            color_name = "white",
            color_code_hex = "FFFFFF"
        )
        cls.color_black = P_Color.objects.create(
            color_name = "black",
            color_code_hex = "000000"
        )

        # Creating product
        cls.product = Product.objects.create(
            product_name = "Beach shirt",
            description = "Men's shirt for summer",
            note = "",
            price = 100.00,
            unit_of_measurement = "",
            quantity_in_stock = 15,
            quantity_in_transit = 10,
            quantity_ordered = 0,
            quantity_per_unit = 1,
            weight = 2.3,
            dimension = "none",
            rating = 4.9,
            ranking = 1,
            is_taxable = True,
            tax_rate = 0.13,
            brand = cls.brand
        )
        cls.product.colors.add(cls.color_white, cls.color_black)
        cls.product.categories.add(cls.categ)
        cls.product.sizes.add(cls.size_large, cls.size_small)
        
    def get_label(self, field_name):
        return self.product._meta.get_field(field_name).verbose_name

    def test_product_name_label(self):
        self.assertEqual(self.get_label('product_name'), 'product name')
    
    def test_description_label(self):
        self.assertEqual(self.get_label('description'), 'description')

    def test_note_label(self):
        self.assertEqual(self.get_label('note'), 'note')

    def test_price_label(self):
        self.assertEqual(self.get_label('price'), 'price')

    def test_unit_of_measure_label(self):
        self.assertEqual(self.get_label('unit_of_measurement'), 'unit of measurement')

    def test_quantity_stock_label(self):
        self.assertEqual(self.get_label('quantity_in_stock'), 'quantity in stock')

    def test_quantity_transit_label(self):
        self.assertEqual(self.get_label('quantity_in_transit'), 'quantity in transit')

    def test_quantity_ordered_label(self):
        self.assertEqual(self.get_label('quantity_ordered'), 'quantity ordered')

    def test_quantity_unit_label(self):
        self.assertEqual(self.get_label('quantity_per_unit'), 'quantity per unit')

    def test_weight_label(self):
        self.assertEqual(self.get_label('weight'), 'weight')

    def test_dimension_label(self):
        self.assertEqual(self.get_label('dimension'), 'dimension')

    def test_rating_label(self):
        self.assertEqual(self.get_label('rating'), 'rating')

    def test_ranking_label(self):
        self.assertEqual(self.get_label('ranking'), 'ranking')

    def test_is_taxable_label(self):
        self.assertEqual(self.get_label('is_taxable'), 'is taxable')

    def test_tax_rate_label(self):
        self.assertEqual(self.get_label('tax_rate'), 'tax rate')

    def test_colors_label(self):
        self.assertEqual(self.get_label('colors'), 'colors')

    def test_sizes_label(self):
        self.assertEqual(self.get_label('sizes'), 'sizes')

    def test_categories_label(self):
        self.assertEqual(self.get_label('categories'), 'categories')

    def test_brand_label(self):
        self.assertEqual(self.get_label('brand'), 'brand')
