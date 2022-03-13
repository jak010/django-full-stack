from django.test import TestCase

import pytest

# refer: https://jonnung.dev/django/2018/12/30/pytest-django/

from customer.domain.model import Customers


# Django Model Test

@pytest.fixture
def customer(db):
    return Customers.objects.create(
        customerNumber=999,
        customerName='tester')


def test_customer_exist(customer):
    # filter 는 queryset 을 반환
    assert Customers.objects.filter(customerNumber=999).exists()


def test_customer_check_name(customer):
    # get 는 object 을 반환
    assert Customers.objects.get(customerNumber=999) \
               .customerName == 'tester'


## Example

# Create your tests here.

@pytest.fixture
def example_fixture():
    return "example"


@pytest.fixture(params=[1, 2])
def example_fixture2(request):
    return request.param

# def test_example(example_fixture):
#     # pytest.fixture decorator 가 붙은 함수는 변수 처럼 사용할 수 있음
#     # - `@property` 느낌으로 보면될 듯
#
#     assert example_fixture == 'example'
#
#
# def test_example2(example_fixture2):
#     # pytest.fixture 는 params에 key 로 값을 여러개 사용할 수 있음
#     assert example_fixture2 == 1
#
#
# @pytest.mark.parametrize('number', [1, 2, 3, 4, 5])
# def test_example3(number):
#     assert number > 0
