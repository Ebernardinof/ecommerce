from django import template
from cart.models import Order

register = template.Library()


@register.filter(name='cart_total')
def cart_total(user):
    order = Order.objects.filter(user=user, ordered=False)

    if order.exists():
        return order[0].orderitems.count()
    else:
        return 0
